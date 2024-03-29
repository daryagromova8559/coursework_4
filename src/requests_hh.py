import json
from typing import Any
from src.abstract_hh import AbstractHH
import requests

from src.json_work import JsonWork


class RequestHH(AbstractHH):

    def __init__(self, name: str):
        self.name = name
        self.status = 0  # Статус requests
        self.all_vacancy = self.get_url()

    def get_url(self) -> str | Any:
        """Поиск по названию"""
        if isinstance(self.name, str):
            keys_response = {'text': f'NAME:{self.name}', 'area': 113, 'per_page': 10, }
            info = requests.get(f'https://api.hh.ru/vacancies', keys_response)
            return json.loads(info.text)['items']

    def save_info(self) -> str or list:
        """Создание json файла с найдеными вакансиями"""

        if self.status != 200:
            print(f"Что-то пошло не так, попробуйте заново.\n Код ошибки: {self.status}")

        elif self.__len__() == 0:
            return f"Вакансии не найдены"
        else:
            save = JsonWork()
            save.write_file(self.all_vacancy)
            return self.all_vacancy

    def status_api(self):
        response = requests.get(f'https://api.hh.ru/vacancies')  # отправка GET-запроса
        self.status = response.status_code  # вывод статуса запроса
        return self.status

    def __len__(self):
        return len(self.all_vacancy)
