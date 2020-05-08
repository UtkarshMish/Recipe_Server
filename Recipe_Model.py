from functools import reduce
import sys

import numpy as np
from pandas import json_normalize, DataFrame
from scipy.sparse import coo_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


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
