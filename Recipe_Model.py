from functools import reduce
import sys
import pickle
import numpy as np
from lightfm import LightFM
from pandas import json_normalize, DataFrame
from scipy.sparse import coo_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from random import randint


def hybrid_recommender(model, data, recipe_ids):
    scores = list()
    if len(recipe_ids) == 0:
        recipe_ids = [randint(1, data)]

    for reci_id in recipe_ids:
        scores.append(model.predict(reci_id, np.arange(data), num_threads=4))
    scores = np.array([max(i) for i in zip(*scores)])
    return [i for i in np.argsort(-scores) if i not in recipe_ids][:-5:-1]


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

    def __init__(self, cuisine_list, query):
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
        recipe_id = []
        # df = DataFrame(x, columns=feature_names) # MAKE RECIPE INGREDIENT AS DATA FRAME
        # sim = cosine_similarity(df) # Similarity between ingredient
        matrix = self.form_matrix()
        matrix, related_product_indices, features = self.cosine_sim(matrix)
        for r in related_product_indices:
            recipe_id.append(self.recipes.values[r][0])
        return recipe_id

    def user_like_recommend(self):
        self.query = [index for index, item in enumerate(
            self.recipes['id']._values) if item in self.query]
        try:
            with open("models/recipe_model.pickle", "rb") as handle:
                model_recipe = pickle.load(handle)
        except FileNotFoundError as f:
            model_recipe = LightFM(
                learning_schedule='adadelta', loss='warp-kos')
            matrix = self.form_matrix()
            matrix, feature_names, label = vectorizer(matrix)
            df = DataFrame(matrix, columns=feature_names)
            df.insert(0, "id", self.recipes['id'])
            data = coo_matrix(df, dtype=np.float32)
            model_recipe.fit(data, epochs=30, num_threads=4)
        scores = hybrid_recommender(
            model_recipe, self.recipes["id"].size, self.query)
        return DataFrame(
            self.recipes.values[scores],
            columns=self.recipes.columns).to_dict(orient='records')
