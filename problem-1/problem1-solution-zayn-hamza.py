def validateRecipe(fridge, ingredients):
    fridge = set(fridge)
    ingredients = set(ingredients)
    is_valid = ingredients.issubset(fridge)
    return is_valid


frg = ["mango", "orange", "banana", "apple", "cake"]
ingrdnts_1 = ["mango", "orange", "banana"]
ingrdnts_2 = ["mango", "orange", "milk"]


print(validateRecipe(frg, ingrdnts_1))
print(validateRecipe(frg, ingrdnts_2))
