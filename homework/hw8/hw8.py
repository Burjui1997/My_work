from homework.hw16.marvel import small_dict
# stage = {
#     1: 'Первая фаза',
#     2: 'Вторая фаза',
#     3: 'Третья фаза',
#     4: 'Четвертая фаза',
#     5: 'Пятая фаза',
#     6: 'Шестая фаза'
# }
# try:
#     user_input = int(input('Введите фазу от 1 до 6: '))
#     if user_input > len(stage):
#         raise ValueError('Введите число в указанном диапазоне')
#     if type(user_input) != int:
#         raise TypeError('Введите корректный тип данных')
# except ValueError as error:
#     print(error)
# except TypeError as error_2:
#     print(error_2)
# else:
#     if user_input in stage.keys():
#         for key, value in full_dict.items():
#             # for inner_key, inner_value in value.items():
#             if value['stage'] == stage[user_input]:
#                 print(value)
#
#
# films_2 = {
#     'Мстители: Династия Канга': {
#         'Дата выхода': 2026,
#         'Режиссёр': 'Дестин Дэниел Креттон',
#         'Актёры': ['Бри Ларсон', 'Том Хиддлстон', 'Сэмюэл Л. Джексон', 'Бенедикт Вонг', 'Тильда Суинтон']
#     },
#     'Мстители': {
#         'Дата выхода': 2012,
#         'Режиссёр': 'Джосс Уидон',
#         'Актёры': ['Роберт Дауни мл.', 'Крис Эванс', 'Крис Хемсворт', 'Скарлетт Йоханссон', 'Джереми Реннер']
#
#     }}
#
# user_input = 'Роберт Дауни мл.'
#
# for k, v in films_2.items():
#     if user_input in v['Актёры']:
#         print(v)

# Найти все фильмы, в которых снимался Роберт Дауни мл.
# Получить на выходе print наименование фильма

def func(value, **kwargs):
    films_lst = []
    for film, year in kwargs.items():
        if search == film:
            films_lst.append(film)
    return films_lst

search_input = (input('Введите год фильма: '))

result = func(search_input, **small_dict)
print(result)
