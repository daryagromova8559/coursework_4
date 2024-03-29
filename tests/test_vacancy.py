import pytest

from src.requests_hh import RequestHH
from src.vacancy import Vacancy


@pytest.fixture
def vac():
    vacs_list = Vacancy(100_000, 'Москва')
    return vacs_list


@pytest.fixture
def req():
    re_list = RequestHH('Учитель')
    return re_list


def test_init1(req):
    assert req.name == 'Учитель'
    req.get_url()
    req.status_api()
    req.save_info()


def test_init2(vac):
    assert vac.salary == 100000
    assert vac.city == 'Москва'
    assert vac.vacancy() == [
        {'id': '95638301', 'premium': False, 'name': 'Учитель русского языка и литературы', 'department': None,
         'has_test': False, 'response_letter_required': False,
         'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
         'salary': {'from': 100000, 'to': None, 'currency': 'RUR', 'gross': True},
         'type': {'id': 'open', 'name': 'Открытая'},
         'address': {'city': 'Москва', 'street': 'Рублёвское шоссе', 'building': '24к3', 'lat': 55.745129,
                     'lng': 37.428935, 'description': None, 'raw': 'Москва, Рублёвское шоссе, 24к3', 'metro': None,
                     'metro_stations': [], 'id': '6038402'}, 'response_url': None, 'sort_point_distance': None,
         'published_at': '2024-03-28T12:49:03+0300', 'created_at': '2024-03-28T12:49:03+0300', 'archived': False,
         'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=95638301',
         'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/95638301?host=hh.ru',
         'alternate_url': 'https://hh.ru/vacancy/95638301', 'relations': [],
         'employer': {'id': '4165810', 'name': 'ГБОУ школа №1584', 'url': 'https://api.hh.ru/employers/4165810',
                      'alternate_url': 'https://hh.ru/employer/4165810', 'logo_urls': None,
                      'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=4165810',
                      'accredited_it_employer': False, 'trusted': True}, 'snippet': {
            'requirement': 'Высшее профессиональное образование или среднее профессиональное образование по направлению подготовки «Образование и педагогика» или в области, соответствующей преподаваемому предмету. ',
            'responsibility': 'Обеспечивать использование разнообразных форм, приемов, методов и средств обучения, в том числе по индивидуальным учебным планам, ускоренным курсам в рамках...'},
         'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
         'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
         'professional_roles': [{'id': '132', 'name': 'Учитель, преподаватель, педагог'}],
         'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
         'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
         'adv_context': None}]
