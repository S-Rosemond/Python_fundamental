import xml.etree.ElementTree as ET

obj ={}

# obj used as ref/hoist
def lookup(entry, key, obj=obj):
    found = False
    prev = None
    for child in entry:
        if found: 
            obj[prev] = child.text
            return
        if child.tag == 'key' and child.text == key:
            obj[child.text] = obj.get(child.text, None)
            prev = child.text
            found = True
    return None

# path filler
read_file = 'path'

tree = ET.parse(read_file)
# array to traverse
array = tree.findall('dict/dict/dict')
# final arr of obj
final_array = list()

for el in array:
    lookup(el, 'any field')
    lookup(el, 'any field')
    lookup(el, 'any field')
    lookup(el, 'any field')
    # Python version of spread operator {**copy_from_obj} two * for obj, [*copy_from_list] one * for array
    final_array.append({**obj})

print(final_array)
obj = {}