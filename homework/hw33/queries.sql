--Создание таблицы city
CREATE TABLE IF NOT EXISTS city (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_name TEXT,
    lat REAL,
    lon REAL,
    population INTEGER,
    subject_id INTEGER,
    district_id INTEGER,
    FOREIGN KEY (subject_id) REFERENCES subjects(id),
    FOREIGN KEY (district_id) REFERENCES district(id)
    );
--Создание индекса для city_name
CREATE INDEX IF NOT EXISTS ind_city_name ON city(city_name);

--Создание таблицы subject
CREATE TABLE IF NOT EXISTS subject (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_name TEXT
    );


--Создание таблицы district
CREATE TABLE IF NOT EXISTS district (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    district_name TEXT
    );
