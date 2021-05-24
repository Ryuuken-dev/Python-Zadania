"""
Przygotuj klasę File, która będzie posiadała następujące metody statyczne:
    - usunięcie konkretnego pliku
    - pobranie listy zawierającej wszystkie linie pliku
    - Zwróci True/False w zależności od tego czy plik istnieje
"""
from os import path
from os import remove


class File:
    @staticmethod
    def delete(filename: str):
        remove(filename)

    @staticmethod
    def read_file(filename: str):
        data = []
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip('\n')
                data.append(line)
        return data

    @staticmethod
    def exists(filename: str):
        return path.isfile(filename)


def test_if_file_not_exists():
    file = 'datas.txt'

    result = File.exists(file)

    assert result == False


def test_if_file_exists():
    file = 'names.txt'

    result = File.exists(file)

    assert result == True


def test_if_file_data_is_reading():
    file = 'names.txt'

    result = File.read_file(file)

    assert result == ['Alicja', 'Aurelia', 'Anastazja', 'Mieczysław', 'Stanisław', 'Ambroży']


def test_if_file_is_removed():
    file = 'names.txt'

    File.delete(file)
    result = File.exists(file)

    assert result == False