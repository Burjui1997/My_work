from abc import ABC, abstractmethod
import json
import csv


class File(ABC):
    def __init__(self,filename):
        self.filename = filename

    @abstractmethod
    def read_file(self, filepath):
        pass

    @abstractmethod
    def write_file(self, filepath):
        pass

    @abstractmethod
    def append_file(self, filepath):
        pass


class CsvFileHandler(File):
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
