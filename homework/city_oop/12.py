import json
with open('city.json', 'r', encoding="utf-8") as file:
   print(json.loads(file.read()))
