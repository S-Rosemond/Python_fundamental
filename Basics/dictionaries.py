array = ['red', 'white', 'blue', 'white', 'blue', 'red', 'blue']
# initialize an obj/dictionary
obj = dict()

# histogram shortcut
for el in array:
    obj[el] = obj.get(el, 0) + 1

print(obj)

# sorting
# sorted([(key,value) for key, value in obj.items()]) 