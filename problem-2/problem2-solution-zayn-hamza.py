def validateRecipeWithQuantity(fridge, ingredients):
    is_valid = ingredients.items() <= fridge.items()
    return is_valid


ingredients_1 = {'tomato': 2, 'onion': 3}
ingredients_2 = {'tomato': 2, 'milk': 3}
fridge = {'tomato': 2, 'onion': 3, 'olives': 1}

print(validateRecipeWithQuantity(fridge, ingredients_1))
print(validateRecipeWithQuantity(fridge, ingredients_2))
