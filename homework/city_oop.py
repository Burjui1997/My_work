import json
import random
from typing import List, Dict, Union


class JsonFile:
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f'Файл {self.filename} не найден')
            return None
        except json.JSONDecodeError:
            print(f'Ошибка декодирования {self.filename}')
            return None

    class Cities:
        def __init__(self, city_data: List[Dict[str, str]]):
            self.city_data = [city['name'].capitalize() for city in city_data]

    class CityGame:
        def __init__(self, cities):
            self.cities = cities
            self.used_cities: List[str] = []
            self.current_city: Union[str, None] = None

        def start_game(self) -> None:
            print('Игра началась !')
            self.bot_turn()

        def your_turn(self, city_input: str) -> None:
            if city_input.lower() == 'стоп':
                print('Игра окончена!')
                return
            if self.valed_city(city_input):
                self.used_cities.append(city_input)
                self.bot_turn()
            else:
                print('Вы проиграли!')

        def bot_turn(self) -> None:
            if not self.current_city:
                available_cities = self.cities.city_data
            else:
                last_leter = self.current_city[-1].lower()
                available_cities = [city for city in self.cities.city_data if
                                    city.lower().startswith(last_leter) and city not in self.used_cities]
            if not available_cities:
                self.end_game('Вы выиграли!')
            else:
                computer_choice = random.choice(available_cities)
                print(f'Компуктер назвал: {computer_choice}')
                self.used_cities.append(computer_choice)
                self.current_city = computer_choice
                self.human_turn(input('Предлагаю вам сделать ход: '))

        def is_valid_city(self, city: str) -> bool:
            return city.lower() in [c.lower() for c in self.cities.city_data] and city not in self.used_cities

        def check_game_over(self) -> bool:
            if not self.current_city:
                return False

            last_letter = self.current_city[-1].lower()
            available_cities = [city for city in self.cities.city_data if
                                city.lower().startswith(last_letter) and city not in self.used_cities]

            return not available_cities

        def end_game(self, winner: str) -> None:
            print(f'{winner} победил!')

    class GameManager:
        def __init__(self, json_file, cities, game):
            self.json_file = json_file
            self.cities = cities
            self.game = game

        def __call__(self) -> None:
            self.run_game()
            self.display_game_result()

        def run_game(self) -> None:
            self.game.start_game()

        def display_game_result(self) -> None:
            print('Игра окончена. До новых встреч!')

    if __name__ == '__main__':
        json_file = JsonFile('city.json')
        cities = Cities(json_file.read_data())
        game = CityGame(cities)

        play_game_manager = GameManager(json_file, cities, game)
        play_game_manager()
