from homework.hw.cities import cities
import json
# Флаги открытия

# message = 'Привет мир \n'
#           'Мы изучаем пайтон\n'
#
#
#
# with open("my_file.txt", "w", encoding='UTF-8') as file:
#     file.write(message)
#
# with open ("my_file.txt", "r", encoding='UTF-8') as file:
#     for line in file:
#         print(line)
#
with open("my_file.json", "w", encoding='UTF-8') as file:
    json.dump(cities,file,ensure_ascii=False, indent= 1)