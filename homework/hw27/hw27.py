import json
from dataclasses import dataclass, field
from typing import List, Any, Dict, Optional, Set
from jsonschema import validate, ValidationError


class JsonFileHandler:

    def __init__(self, filepath: str):
        self.data: Optional[None, list] = None
        self.filepath = filepath

    def read_file(self) -> List[dict] | List[list]:

        with open(self.filepath, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
            return self.data

    def write_file(self, data: List[dict] | List[list]) -> None:

        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def append_file(self, data: List[list | dict]) -> None:

        if not isinstance(data, list):
            raise TypeError('Данный тип файла не поддерживает операцию дописывания')
        self.read_file()
        self.data.extend(data)
        self.write_file(self.data)

    def get_cities_set(self, cities_list: List[dict]) -> set:

        cities_set = set()
        for city in cities_list:
            cities_set.add(city['name'])

        self.write_file(list(cities_set))
        return cities_set


@dataclass(order=True)
class City:
    name: str
    subject: str = field(compare=False)
    population: int = field(compare=False)


class DataValidator:
    @staticmethod
    def validate_data(data) -> list(Dict[str, Any]):
        schema = {
            "type": "object",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "population": {"type": "integer"},
                    "subject": {"type": "string"}
                },
                "required": ["name", "population", "subject"],
                "additionalProperties": False
            }
        }
        cities_valid = []
        for item in data:
            cities_valid_temp = {}
            try:
                validate(item, schema)
                cities_valid_temp['subject'] = item['subject']
                cities_valid_temp['name'] = item['name']
                cities_valid_temp['population'] = item['population']
                cities_valid.append(cities_valid_temp)
            except ValidationError as e:
                print(f'Error {e.message}')
        return cities_valid

    # def validate_data_types(cities):
    #     for city in cities:
    #         if not isinstance(city.name, str) or not isinstance(city.population, int):
    #             raise ValueError("Неверный тип данных в датасете.")
    #         return cities

    def __init__(self, cities_list: List[dict]):
        self.cities_list = cities_list
        self.bad_letters: set = self.get_bad_letters_from_cities_list()
        print(f'Плохие буквы: {self.bad_letters}')

    def get_bad_letters_from_cities_list(self) -> set:

        first_letters = set()
        last_letters = set()

        for city in self.cities_list:
            first_letters.add(city['name'][0].lower())
            last_letters.add(city['name'][-1].lower())

        bad_cities_set = last_letters - first_letters
        return bad_cities_set

    def check_city_name(self, city_name: str) -> bool:

        if city_name[0].lower() in self.bad_letters:
            return False
        else:
            return True

    def check_city_population(self, city_population: int) -> bool:

        if not isinstance(city_population, int):
            return False
        else:
            return True

    def check_city_name_case(self, city_name: str) -> str:

        if city_name.islower():
            return city_name.title()
        else:
            return city_name

    def validate_data(self) -> List[dict]:

        validated_data = []
        for city in self.cities_list:
            if self.check_city_name(city['name']) and self.check_city_population(city['population']):
                city['name'] = self.check_city_name_case(city['name'])
                validated_data.append(city)
        return validated_data


class DataSerializer:

    def __init__(self, json_file_handler: JsonFileHandler, data_validator: DataValidator):
        self.json_file_handler = json_file_handler
        self.data_validator = data_validator
        self.__row_data: List[dict] = self.json_file_handler.read_file()
        self.__validated_data: List[dict] = self.data_validator.validate_data()
        self.serialize_data: List[City] = self.serialize_data()

    def serialize_data(self) -> List[City]:
        return [City(**city) for city in self.__validated_data]


class CityGame:
    def __init__(self, cities_obj: List[City]):
        self.cities = cities_obj
        self.cities_set: Set[str] = {city.name for city in self.cities}
        self.human_city: str = ''
        self.computer_city: str = ''

    @staticmethod
    def check_game_rules(last_city: str, new_city: str) -> bool:

        if last_city[-1].lower() == new_city[0].lower():
            return True
        else:
            return False

    def human_step(self):

        self.human_city = input('Введите город: ')
        if self.human_city == 'стоп':
            print('Вы проиграли')
            return False

        if self.human_city not in self.cities_set:
            print(f'Города {self.human_city} нет в списке. Вы проиграли')
            return False

        if self.computer_city:
            if not self.check_game_rules(self.computer_city, self.human_city):
                print(f'Вы проиграли. Ваш ответ не начинается на букву {self.computer_city[-1]}')
                return False

        self.cities_set.remove(self.human_city)
        self.human_city = self.human_city

        return True

    def computer_step(self):

        for city in self.cities:
            if city.name[0].lower() == self.human_city[-1].lower():
                self.computer_city = city.name
                self.cities_set.remove(self.computer_city)
                print(f'Компьютер назвал город {self.computer_city}')
                return True
        print('Вы выиграли. Компьютер не смог назвать город')
        return False


class GameManager:
    def __init__(self, json_file_handler: JsonFileHandler, data_validator: DataValidator,
                 data_serializer: DataSerializer, city_game_obj: CityGame):
        self.json_handler_obj: JsonFileHandler = json_file_handler
        self.data_validator_obj: DataValidator = data_validator
        self.data_serializer_obj: DataSerializer = data_serializer
        self.cities: List[City] = self.data_serializer_obj.serialize_data
        self.game: CityGame = city_game_obj

    def __call__(self):
        self.run_game()

    def run_game(self):
        while True:
            if not self.game.human_step():
                break
            if not self.game.computer_step():
                break


if __name__ == "__main__":
    json_file_handler = JsonFileHandler('cities.json')
    data_validator = DataValidator(json_file_handler.read_file())
    data_serializer = DataSerializer(json_file_handler, data_validator)
    game = CityGame(data_serializer.serialize_data)
    game_manager = GameManager(json_file_handler, data_validator, data_serializer, game)
    game_manager()
