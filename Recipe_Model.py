from functools import reduce
import sys

import numpy as np
from lightfm import LightFM
from pandas import json_normalize, DataFrame
from scipy.sparse import coo_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from random import randint


def hybrid_recommender(model, data, recipe_ids):
    scores = list()
    n_recipe, n_ing = data.shape
    if len(recipe_ids) == 0:
        recipe_ids = [randint(1, n_recipe)]

    for reci_id in recipe_ids:
        scores.append(model.predict(reci_id, np.arange(n_ing)))
    scores = reduce(lambda a, b: a + b, scores)
    return scores


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
            ingredients.append({"name": [i['name'] for i in ing]})
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
        model_recipe = LightFM(learning_schedule='adadelta', loss='warp')
        matrix = self.form_matrix()
        matrix, feature_names, label = vectorizer(matrix)
        df = DataFrame(matrix, columns=feature_names)
        df.insert(0, "id", self.recipes['id'])
        data = coo_matrix(df, dtype=np.float32)
        model_recipe.fit(data, epochs=30)
        scores = hybrid_recommender(model_recipe, data, self.query)
        x = df['id'][np.argsort(-scores)][:-5:-1]
        return DataFrame(
            self.recipes.values[x],
            columns=self.recipes.columns).to_dict(orient='records')
