from marvel import full_dict
from pprint import pprint

input_list = input("Введите цифры через пробел: ").split()
converted_list = list(map(lambda x: int(x) if x.isdigit() else None, input_list))

filtered_dict = dict(filter(lambda item: item[0] in converted_list, full_dict.items()))

director_set = {value['director'] for value in full_dict.values()}

str_dict = {key: str(value) if key == 'year' else value for key, value in full_dict.items()}

filtered_startswith_ch = dict(filter(lambda item: item[1]['title'].startswith('Ч'), full_dict.items()))

pprint(f"Результат задания 2: {converted_list}")
pprint(f"Результат задания 3: {filtered_dict}")
pprint(f"Результат задания 4: {director_set}")
pprint(f"Результат задания 5: {str_dict}")
pprint(f"Результат задания 6: {filtered_startswith_ch}")

