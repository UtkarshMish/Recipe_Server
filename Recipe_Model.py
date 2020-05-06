#!/usr/bin/env python
# coding: utf-8

from pandas import json_normalize, DataFrame
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Recommender:
    query = ""

    def __init__(self, cuisine_list, query):
        self.query = query
        self.recipes = json_normalize(cuisine_list)
        ingredients = []
        for ing in self.recipes['ingredients']:
            ingredients.append({"name": [i['name'] for i in ing]})
        ingredients = DataFrame(ingredients)
        # ### Analyzing recipe
        self.recipes['ingredients'] = ingredients
        matrix = []
        for i in range(ingredients.size):
            matrix.append([" ".join(ing) for ing in ingredients.values[i]])
        matrix = [" ".join(a) for a in matrix]
        self.label = TfidfVectorizer(decode_error="replace",
                                     stop_words='english',
                                     lowercase=True,
                                     analyzer="word")
        matrix = self.label.fit_transform(matrix)
        # feature_names = label.get_feature_names() # TO GET FEATURE NAMES
        matrix = matrix.todense()
        self.matrix = matrix.tolist()

    def guide_predictor(self):
        recipe_id = []
        # df = DataFrame(x, columns=feature_names) # MAKE RECIPE INGREDIENT AS DATA FRAME
        # sim = cosine_similarity(df) # Similarity between ingredient
        search_query = self.label.transform([self.query])
        cosine_similarities = cosine_similarity(search_query,
                                                self.matrix).flatten()
        related_product_indices = cosine_similarities.argsort()[:-6:-1]

        for r in related_product_indices:
            recipe_id.append(self.recipes.values[r][0])
        return recipe_id
