import re

read_file = 'text.txt'
# compile = set regex, then use search or findall, match = single match
regex = re.compile('sit')

with open(read_file) as fh:
    array = re.findall(regex, fh.read())

print(array)

obj = {}

for el in array:
    obj[el] = obj.get(el, 0) + 1
    
print(obj)


