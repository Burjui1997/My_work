from cities import cities


def start_game(cities):  # Создаем функцию которая инициализирует старт игры
    set_city = set()
    for city in cities:
        set_city.add(city['name'])
    return set_city


def user_turn(set_city):  # Создаем функцию пользовательского ввода с циклом
    user_input = input('Введите город: ').capitalize()
    while True:
        match user_input:
            case 'Стоп' | 'стоп':
                print('Вы проиграли')
                break
            case user_input if user_input not in set_city:
                print('Такого города нет, пока!')
                break
            case _:
                set_city.remove(user_input)
                last_letter = user_input[-1].upper()
                return last_letter


def bot_turn(set_city, last_letter):  # Функция ввода бота с циклом
    bot_city = None
    for city in set_city:
        if city.startswith(last_letter):
            bot_city = city
            set_city.remove(city)
            break
    return bot_city


def main():  # Создаем основную функцию игры
    set_city = start_game(cities)
    print('Игра началась')

    while True:
        last_letter = user_turn(set_city)
        if last_letter is None:
            break

        bot_city = bot_turn(set_city, last_letter)

        if bot_city is None:
            print(f'У меня нет такого города на букву {last_letter}, я проиграл')
            break

        print(f'Мой город {bot_city}. Ваш ход:')

    print('Игра окончена')
