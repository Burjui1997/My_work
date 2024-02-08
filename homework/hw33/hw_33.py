import sqlite3 as sq
import json


def read_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return


def read_sql_queries(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return


def execute_query(query, db_path):
    with sq.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()


def execute_many_queries(queries, params, db_path):
    with sq.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.executemany(queries, params)
        conn.commit()


def fetch_data(query, db_path):
    with sq.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()


def get_city_data(city_name, db_path):
    query = f'''
       SELECT * FROM city
       JOIN subject ON city.subject_id = subject.id
       JOIN district ON city.district_id = district.id
       WHERE city_name = '{city_name}'
       '''
    return fetch_data(query, db_path)


def main():
    db_path = 'cities.db'
    sql_file_path = 'queries.sql'
    json_file_path = 'cities.json'

    # Чтение и выполнение SQL-запросов из файла
    sql_queries_row = read_sql_queries(sql_file_path)
    sql_queries = sql_queries_row.split(';')

    for query in sql_queries:
        execute_query(query, db_path)

    # Чтение данных из JSON
    cities_data = read_json(json_file_path)

    # Подготовка данных для вставки в БД
    cities = [(city['name'], city['coords']['lat'], city['coords']['lon'],
               city['population'], city['subject'], city['district']) for city in cities_data]

    subjects = [(city['subject'],) for city in cities_data]
    districts = [(city['district'],) for city in cities_data]

    # Запрос для query-параметров execute_many_queries (для вставки данных в таблицу subject)
    insert_subject_query = '''
    INSERT INTO subject (subject_name)
    VALUES (?)
    '''

    execute_many_queries(insert_subject_query, subjects, db_path)

    # Запрос для query-параметров execute_many_queries (для вставки данных в таблицу district)
    insert_district_query = '''
    INSERT INTO district (district_name)
    VALUES (?)
    '''

    execute_many_queries(insert_district_query, districts, db_path)

    # Запрос для query-параметров execute_many_queries (для вставки данных в таблицу city)
    insert_city_query = '''
    INSERT INTO city (city_name, lat, lon, population, subject_id, district_id)
    VALUES (?, ?, ?, ?,
        (SELECT id FROM subject WHERE subject_name = ?),
        (SELECT id FROM district WHERE district_name = ?))
    '''

    execute_many_queries(insert_city_query, cities, db_path)
    print(get_city_data('Москва', db_path))


if __name__ == '__main__':
    main()
