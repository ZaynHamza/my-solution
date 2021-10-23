def add(fridge, textbox):
    textbox = textbox.split(" ")

    if len(textbox) == 2:
        textbox = {textbox[0]: int(textbox[1])}
        fridge.update(textbox)
        return fridge

    else:
        return "Input is not valid"


fridge = {'tomato': 2, 'onion': 3, 'olives': 1}
textbox_1 = "banana 3"
textbox_2 = "banana 3 packages"

print(add(fridge, textbox_1))
print(add(fridge, textbox_2))
