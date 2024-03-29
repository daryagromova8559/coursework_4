from src.json_work import JsonWork


class Vacancy:

    def __init__(self, salary: int, city: str):
        """Инициализируем с атрибутами:
        salary - Зарплата,
        city - Город"""
        read = JsonWork()
        self.rd_vacancy = read.read_file()
        self.constr_vacancy = []  # Пустой лист для сортировки вакансий по 'городу' и 'желаемой зарплаты'
        self.count = 0  # Счетчик количества найденных вакансий
        self.salary = salary
        self.city = city
        self.found_vacancy = []  # Найденные вакансии
        self.top_salary = 0  # Наибольшая зарплата
        self.message = 'Вакансии найдены'

    def vacancy(self):
        for vacancy_d in self.rd_vacancy:
            if vacancy_d["salary"] is not None and vacancy_d["salary"]["from"] is not None:
                if vacancy_d['area']['name'] == self.city:
                    if vacancy_d['salary']['from'] >= self.salary:
                        self.found_vacancy.append(vacancy_d)
        return self.found_vacancy

    def construction(self):
        """Функция для формирования полученной информации"""
        for i in self.found_vacancy:
            if i['salary']['to'] is None:
                i['salary']['to'] = 0
            self.constr_vacancy.append(f"{self.count + 1}.{i['name']}, \nЗарплата от: {i['salary']['from']}, "
                                       f"\nЗарплата до: {i['salary']['to']}, "
                                       f"\nТребование: {i['snippet']['requirement']}, "
                                       f"\nТребуется: {i['snippet']['responsibility']}, "
                                       f"\nГород: {i['area']['name']}, "
                                       f"\nСсылка на вакансию: {i['alternate_url']}")
            self.count += 1
        return self.constr_vacancy

    def __str__(self):
        """Вывод подобранных вакансий"""
        if self.count > 0:
            print(f'Найдены вакансии в колличестве {self.count}, с максимальной зарплатой {self.top_salary} :\n')
            for v in self.constr_vacancy:
                print(f'{v}\n')
        else:
            self.message = "Вакансии не найдены."
            print(self.message)

    def top_vacancy(self):
        """Переборка зарплаты и выбор наибольшей зарблаты"""
        for i in self.found_vacancy:
            if i['salary']['from'] > self.top_salary:
                self.top_salary = i['salary']['from']
        return self.top_salary
