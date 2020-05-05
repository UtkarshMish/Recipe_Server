#!/usr/bin/env python
# coding: utf-8

import json

from pandas import json_normalize, DataFrame
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def predictor(query):
    with open("./data/all_recipes.json") as recipe_data:
        recipes = json.load(recipe_data)
    recipes = json_normalize(recipes)

    ingredients = []
    for ing in recipes['ingredients']:
        ingredients.append({"name": [i['name'] for i in ing]})
    ingredients = DataFrame(ingredients)

    # ### Analyzing recipe

    recipes['ingredients'] = ingredients
    x = []
    for i in range(ingredients.size):
        x.append([" ".join(ing) for ing in ingredients.values[i]])
    x = [" ".join(a) for a in x]
    label = TfidfVectorizer(decode_error="replace", stop_words='english', lowercase=True)
    x = label.fit_transform(x)
    # feature_names = label.get_feature_names() # TO GET FEATURE NAMES
    x = x.todense()
    x = x.tolist()
    # df = DataFrame(x, columns=feature_names) # MAKE RECIPE INGREDIENT AS DATA FRAME
    # sim = cosine_similarity(df) # Similarity between ingredient
    search_query = label.transform([query])
    cosine_similarities = cosine_similarity(search_query, x).flatten()
    related_product_indices = cosine_similarities.argsort()[:-6:-1]
    recipe_id = []
    for r in related_product_indices:
        recipe_id.append(recipes.values[r][0])
    return recipe_id
