
from marvel import film_set, small_dict
# print(film_set)
# for film in film_set:
#     print(film, end=' || ')
# while True:
#     user_input = input("Посмотрим фильм?")
#     if user_input !='нет':
#         film = film_set.pop()
#         print(f'Предлагаю посмотреть {film}')
#     else:
#         break
# is_stoped = False
# while not is_stoped:
#     user_input = input("Посмотрим фильм?")
#     if user_input !='нет':
#         film = film_set.pop()
#         print(f'Предлагаю посмотреть {film}')
#     else:
#         is_stoped = True


film_igor = {'мстители','человек-паук','тор'}
# film_alex= {'мстители','халк','Дэдпул'}
# print(film_alex.intersection(film_igor))
# print(film_igor.difference(film_alex))
# print(film_alex.symmetric_difference(film_igor))

# while True:
#     user_input = input('Введите фильмы через запятую:')
#     if user_input == 'stop':
#             break
#     user_film = set(user_input.split(','))
#     print(user_film.intersection(film_set))


# a = input('ВВедите первое число:')
# b = input('Введите второе число:')
# if a.isdigit() and b.isdigit():
#     print(int(a)/int(b))
# else:
#     print('Это не число')
#     raise ValueError ('Это не число,введите число')

# user_input = input('Введите число через запятую:')
# user_list = user_input.split(',')
# new_list = []
# for num in user_list:
#     if not num.isdigit():
#         raise TypeError
#     if int(num) % 2 != 0:
#         raise ValueError

user_input = input('введите название фильма')
for film in small_dict.values():
    year = small_dict.values()
    print(f'Фильм {user_input} вышел в {year}')