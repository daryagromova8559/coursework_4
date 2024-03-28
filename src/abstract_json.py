from abc import ABC, abstractmethod


class AbstrJson(ABC):
    @abstractmethod
    def write_file(self, vacancy):
        """Создание json файла с найдеными вакансиями"""
        pass

    @abstractmethod
    def read_file(self):
        """Чтение файла с поиском вакансий"""
        pass

    @abstractmethod
    def del_file(self, del_file):
        """Удаление информации"""
        pass
