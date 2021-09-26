from app.models.Recipe import Recipe

import pickle
from typing import Any, Dict, List, Optional
import numpy as np
from lightfm import LightFM
from pandas import json_normalize, DataFrame
from scipy.sparse import coo_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def hybrid_recommender(recipe: DataFrame, model: LightFM, data, recipe_ids):
    scores = list()
    if len(recipe_ids) == 0:
        recipe_ids = recipe["id"].to_list()

    for index in range(len(recipe_ids)):
        scores.append(model.predict(index, np.arange(data), num_threads=4))
    scores = np.array([max(i) for i in zip(*scores)])
    recipe_indexes = [i for i in np.argsort(-scores)[:-6:-1]]
    recipe_object_id = recipe["id"].tolist()
    return [recipe_object_id[indx] for indx in recipe_indexes]


def vectorizer(matrix):
    label = TfidfVectorizer(decode_error="replace",
                            stop_words='english',
                            lowercase=True,
                            analyzer="word")
    matrix = label.fit_transform(matrix)
    feature_names = label.get_feature_names()  # TO GET FEATURE NAMES
    matrix = matrix.todense()
    matrix = matrix.tolist()
    return matrix, feature_names, label


class Recommender:
    query = ""

    def __init__(self, cuisine_list: List[dict], query: Optional[Dict[str,
                                                                      Any]]):
        self.query = query
        self.recipes = json_normalize(cuisine_list)

    def form_matrix(self):
        ingredients = []
        matrix = []
        for ing in self.recipes['ingredients']:
            ingredients.append({"name": [i for i in ing]})
        ingredients = DataFrame(ingredients)
        # ### Analyzing recipe
        for i in range(ingredients.size):
            matrix.append([" ".join(ing) for ing in ingredients.values[i]])
        matrix = [" ".join(a) for a in matrix]
        return matrix

    def cosine_sim(self, matrix):
        matrix, feature_names, label = vectorizer(matrix)
        search_query = label.transform([self.query])
        cosine_similarities = cosine_similarity(search_query, matrix).flatten()
        return matrix, cosine_similarities.argsort()[:-5:-1], feature_names

    def guide_predictor(self):
        recipes_list = []
        matrix = self.form_matrix()
        matrix, related_product_indices, _ = self.cosine_sim(matrix)
        for r in related_product_indices:
            recipes_list.append(self.recipes.values[r][0])
        return recipes_list

    def user_like_recommend(self):
        model_recipe = None
        if not self.recipes.empty:
            self.query = [
                index for index, item in enumerate(self.recipes['id']._values)
                if item in self.query
            ]
        try:
            with open("models/recipe_model.pickle", "rb") as handle:
                model_recipe = pickle.load(handle)
        except FileNotFoundError:
            model_recipe = LightFM(learning_schedule='adadelta',
                                   loss='warp-kos')
            matrix = self.form_matrix()
            matrix, feature_names, label = vectorizer(matrix)
            df = DataFrame(matrix, columns=feature_names)
            '''CHANGE ID HERE to float type'''
            column_series = [i for i in range(len(self.recipes['id']))]

            df.insert(0, "id", column_series)
            data = coo_matrix(df, dtype=np.float32)
            model_recipe.fit(data, epochs=30, num_threads=4)
        scores = hybrid_recommender(self.recipes, model_recipe,
                                    self.recipes["id"].size, self.query)
        return DataFrame(
            self.recipes[self.recipes["id"].isin(scores)].values,
            columns=self.recipes.columns).to_dict(orient='records')
