# print((lambda srtring: srtring == srtring[::-1])("level"))
#
# is_int = lambda number: int(number) if number.isdigit() else None
#
# print(is_int('fdfd'))
#
#
# names = ("Игорь", "Иван", "Саша")
# ages = (20, 30, 25, 30, 30, 30, 30, 30, 30, 30, 30)
#
# user_input = list(map(lambda name,age:f'{name}-{age}',names,ages))
# print(user_input)
#
# sugar_bombs = ['конфеты', 'печенье', 'пирожное', 'торт', 'мороженое', 'пончик', 'булочка', 'блинчик', 'пончик']
# menu = ['печенье', 'омлет', 'кофе', 'сыр']
#
# no_shugar = lambda product: product not in sugar_bombs
# print(list(filter(no_shugar, menu)))
#
# persons_dict = {
#     'Иван': 20,
#     'Петр': 30,
#     'Анна': 25,
#     'Аня': 25,
# }
#
# print(dict(filter(lambda x: 'нн' in x[0].lower(), persons_dict.items())))


def get_username() -> str:
    """
    Функция запрашивает имя пользователя и возвращает его
    :return:
    """
    username = input('Введите имя: ')
    return username


def get_hello_message(username: str) -> str:
    return f'Привет {username}'


def print_hello_message(hello_message: str) -> None:
    print(hello_message)


def run() -> None:
    username = get_username()
    hello_message = get_hello_message(username)
    print_hello_message(hello_message)


run()