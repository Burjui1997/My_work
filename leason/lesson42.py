from marshmallow import Schema, fields, ValidationError
from marshmallow_dataclass import class_schema
from dataclasses import dataclass
from marvel import small_dict, full_dict
import json
"""
schema - базовый схема валидации
fields - поле валидации
ValidationError - ошибка валидации
"""

# marvel_films = [
#     {
#         'title': 'Железный человек',
#         'year': 2008
#     },
#     {
#         'title': 'Невероятный Халк',
#         'year': 2008
#     },
#     {
#         'title': 'Железный человек 2',
#         'year': 2010
#     },
#     {
#         'title': "2022",
#         'year': 2022
#     }
# ]

marvel_films_json = """
[
    {
        "title": "The Avengers",
        "year": 2012
    },
    {
        "title": "Avengers: Age of Ultron",
        "year": 2015
    },
    {
        "title": "Человек-паук: Вдали от дома",
        "year": "2023"
    }
]
"""


res = []
for film in full_dict.values():
    res.append(film)
with open('../homework/data/marvel.json', 'w', encoding='utf-8') as file:
    json.dump(res, file, indent=4, ensure_ascii=False)

@dataclass
class Movie:
    title: str
    year: int
    director: str
    screenwriter: str
    producer: str
    stage: str

    def __str__(self):
        return f'{self.title} {self.year}'

    def __repr__(self):
        return f'{self.title} {self.year}'


FilmSchema = class_schema(Movie)

try:
    films = FilmSchema(many=True).load(res)

except ValidationError as err:
    print(err.messages)

films = []
for film in films:
    films.append(film)
print(films)
# [print(type(film)) for film in films]





# @dataclass
# class Movie:
#     title: str
#     year: int
#
#     def __str__(self):
#         return f'{self.title} {self.year}'
#
#     def __repr__(self):
#         return f'{self.title} {self.year}'
#
#
# FilmSchema = class_schema(Movie)
#
#
# try:
#     films = FilmSchema(many=True).loads(marvel_films_json)
#
#
# except ValidationError as err:
#     print(err.messages)
#
# # [print(type(film)) for film in films]
#
#
# film_lst = FilmSchema(many=True)
# film_json = film_lst.dumps(films)
# print(film_json)
# class FilmSchema(Schema):
#     title = fields.String(required=True)
#     year = fields.Integer(required=True)
#
#
# schema = FilmSchema()
#
# try:
#     schema.load(marvel_films, many=True)
# except ValidationError as e:
#     print(e.messages)

# class MovieSchema(Schema):
#     title = fields.String(required=True)
#     year = fields.Integer(required=True)
#
#
# schema = MovieSchema()
#
# # for key, value in small_dict.items():
# #     try:
# #         schema.load({'title': key, 'year': value})
# #     except ValidationError as e:
# #         print(e)
# try:
#     schema.load(full_dict, many=True)
# except ValidationError as e:
#     print(e.messages)
