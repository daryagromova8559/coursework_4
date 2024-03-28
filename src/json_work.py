import json

from src.abstract_json import AbstrJson
from src.config import DATA


class JsonWork(AbstrJson):
    def __init__(self):
        self.file_path = DATA

    def write_file(self, vacansy):
        """Создание json файла с найдеными вакансиями"""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(vacansy, ensure_ascii=False))

    def read_file(self):
        """Чтение файла с поиском вакансий"""
        with open(DATA, 'r', encoding='utf-8') as f:
            rd_vacansy = json.load(f)
            return rd_vacansy

    def del_file(self, del_file):
        """Удаление информации"""
        pass
