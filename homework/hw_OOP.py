import csv
import json


class CsvFileHandler:
    def read_file(self, filepath, as_dict=False):
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            if as_dict:
                headers = next(reader)
                data = [dict(zip(headers, row)) for row in reader]
            else:
                data = [row for row in reader]
            return data

    def write_file(self, filepath, data, as_dict=False):
        with open(filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            if as_dict and data:
                headers = list(data[0].keys())
                writer.writerow(headers)
                for row in data:
                    writer.writerow(row.values())
            else:
                writer.writerows(data)

    def append_file(self, filepath, data, as_dict=False):
        with open(filepath, 'a', newline='') as file:
            writer = csv.writer(file)
            if as_dict and data:
                headers = list(data[0].keys())
                writer.writerow(headers)
                for row in data:
                    writer.writerow(row.values())
            else:
                writer.writerows(data)


class JsonFileHandler:
    def read_file(self, filepath, as_dict=False):
        with open(filepath, 'r') as file:
            json_data = json.load(file)
            if as_dict:
                data = [dict(entry) for entry in json_data]
            else:
                data = json_data
            return data

    def write_file(self, filepath, data, as_dict=False):
        if as_dict and data:
            json_data = [entry.items() for entry in data]
        else:
            json_data = data
        with open(filepath, 'w') as file:
            json.dump(json_data, file)

    def append_file(self, filepath, data, as_dict=False):
        raise TypeError('Добавление файла невозможно в JSON')


class TxtFileHandler:
    def read_file(self, filepath):
        with open(filepath, 'r') as file:
            data = file.readlines()
            return data

    def write_file(self, filepath, data):
        with open(filepath, 'w') as file:
            file.writelines(data)

    def append_file(self, filepath, data):
        with open(filepath, 'a') as file:
            file.writelines(data)


# Пример записи в csv

csv_handler = CsvFileHandler()
csv_handler.write_file('data.csv', [['Игорь', 'Основин ', '26'], ['Основина', 'Варвара', '24']])
csv_data = csv_handler.read_file('data.csv')
print(csv_data)

# Пример записи в JSON

json_handler = JsonFileHandler()
json_handler.write_file('data.json', [{'имя': 'Игорь', 'возраст': '26'}, {'имя': 'Варвара', 'возраст': '23'}])
json_data = json_handler.read_file('data.json')
print(json_data)

# Запись в txt формате

txt_handler = TxtFileHandler()
txt_handler.write_file('data.txt', ['Игорь\n', 'Варвара\n'])
txt_data = txt_handler.read_file('data.txt')
print(txt_data)


"""
Я очень старался это сделать сам,но без интернета  никуда, 
вроде все хорошо принтуется но в созданных файлах получается белеберда, 
как исправить код надеюсь на вас
"""
