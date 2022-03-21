import json, random

# This line opens a new json file. That new json file is clearly named 'new_file.json'.
f = open('new_file.json')

x = {i: random.randint(0, 100) for i in range(100)}

json.dump(x, f)