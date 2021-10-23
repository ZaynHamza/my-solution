def whereIsMyFood(fridge, item):
    while True:
        if item in fridge:
            item_pos = fridge.index(item)
            return item_pos
        else:
            return -1


frg = ["mango", "orange", "banana", "apple", "cake"]

print(whereIsMyFood(frg, "banana"))
print(whereIsMyFood(frg, "milk"))
