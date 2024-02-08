import jsonschema
from jsonschema import validate, ValidationError, validators
import json
from pprint import pprint
import re
from dataclasses import dataclass

# from homework.hw_sort.marvel import film_set
#
# schema = {
#     "type": "array",
#     "items": {
#         "type": "string",
#         "minLength": 3,
#         "maxLength": 100
#     }
# }
#
# film_list = list(film_set)
# try:
#     validate(instance=film_list, schema=schema)
#     print("Валидция прошла успешно")
# except ValidationError as e:
#     print("Error")
# finally:
#     print("Валидация завершнена")
users_data = [
    {
        "email": "user1@example.com",
        "username": "user1"
    },
    {
        "email": "user2@example.com",
        "username": "user2"
    },
    {
        "email": "user3@example.com",
        "username": "user3"
    },
    {
        "email": "user4",
        "username": "user4"
    },
    {
        "email": "invalid-email",
        "username": "user5"
    },
    {
        "email": "user6@example.com",
        "username": "user6"
    },
    {
        "email": "user7@example.com",
        "username": "user7"
    },
    {
        "email": "user8@example.com",
        "username": "user8"
    },
    {
        "email": "user9@example.com",
        "username": "user9"
    },
    {
        "email": "user10@example.com",
        "username": "user10"
    },
    {
        "email": "user11@example.com",
        "username": "user11"
    },
    {
        "email": "user12@example.com",
        "username": "user12"
    },
    {
        "email": "user13@example.com",
        "username": "user13"
    },
    {
        "email": "user14",
        "username": "user14"
    },
    {
        "email": "invalid-email",
        "username": "user15"
    },
    {
        "email": "user16@example.com",
        "username": "user16"
    },
    {
        "email": "user17@example.com",
        "username": "user17"
    },
    {
        "email": "user18@example.com",
        "username": "user18"
    },
    {
        "email": "user19@example.com",
        "username": "user19"
    },
    {
        "email": "user20@example.com",
        "username": "user20"
    }
]

schema = {
    "type": "object",
    "property": {
        "email": {
            "type": "string",
            "format": "email"
        },
        "username": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9_]{4,20}$"
        }
    },
    "required": ["email", "username"],
    "additionalProperties": False

}
# invalid_data = []
# valid_data = []
# for data in users_data:
#     try:
#         validate(users_data, schema, format_checker=jsonschema.FormatChecker())
#         valid_data.append(data)
#     except ValidationError as e:
#         invalid_data.append(data)
# invalid_data = []
# valid_data = []
# for user in users_data:
#     try:
#         # Делаем попытку валидировать данные по одному пользователю
#         validate(user, schema, format_checker=jsonschema.FormatChecker())
#         valid_data.append(user)
#         #  Если данные не валидны, то валидатор выкинет ошибку
#     except ValidationError as e:
#         invalid_data.append(user)
#         # print(e)
#
#
# # 3. Вывести невалидные данные в консоль
# pprint(invalid_data)
@dataclass
class User:
    email: str
    username: str

class UserValidator:
    def __init__(self,schema):
        self.schema = schema

    def validator_user(self,user, is_checker = False):
        try:
            validate(user, self.schema, format_checker = jsonschema.FormatChecker() if is_checker else None)
            return True
        except ValidationError as e:
            return False

class UserSerializer:
    def __init__(self,user_data, data_validator):
        self.user_data = user_data
        self.data_validator = data_validator