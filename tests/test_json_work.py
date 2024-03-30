import pytest

from src.json_work import JsonWork
from src.requests_hh import RequestHH


@pytest.fixture
def json_work():
    json_list = JsonWork()
    return json_list


@pytest.fixture
def req_hh():
    hh_list = RequestHH('Прокурор')
    return hh_list


def test_init1(req_hh, json_work):
    req_hh.status_api()
    req_hh.save_info()
    assert req_hh.__len__() == 1


def test_init2(json_work, req_hh):
    assert json_work.read_file() == [
        {'id': '95713924', 'premium': False, 'name': 'Помощник прокурора (кадровый резерв)', 'department': None,
         'has_test': False, 'response_letter_required': False,
         'area': {'id': '131', 'name': 'Симферополь', 'url': 'https://api.hh.ru/areas/131'},
         'salary': {'from': 70000, 'to': None, 'currency': 'RUR', 'gross': True},
         'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None,
         'published_at': '2024-03-28T15:38:29+0300', 'created_at': '2024-03-28T15:38:29+0300', 'archived': False,
         'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=95713924',
         'show_logo_in_search': None, 'insider_interview': None,
         'url': 'https://api.hh.ru/vacancies/95713924?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/95713924',
         'relations': [], 'employer': {'id': '3128277', 'name': 'Прокуратура Республики Крым',
                                       'url': 'https://api.hh.ru/employers/3128277',
                                       'alternate_url': 'https://hh.ru/employer/3128277',
                                       'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/3430910.png',
                                                     '90': 'https://img.hhcdn.ru/employer-logo/3430909.png',
                                                     'original': 'https://img.hhcdn.ru/employer-logo-original/747487.png'},
                                       'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3128277',
                                       'accredited_it_employer': False, 'trusted': True}, 'snippet': {
            'requirement': '1) надзор за соблюдением Конституции РФ и исполнением законов, прав и свобод человека и гражданина. - наличие высшего юридического образования по...',
            'responsibility': 'Прокуратурой Республики Крым на систематической основе проводится отбор кандидатов для постановки в кадровый резерв для последующего рассмотрения вопроса приема на...'},
         'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
         'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
         'professional_roles': [{'id': '146', 'name': 'Юрист'}], 'accept_incomplete_resumes': False,
         'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
         'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
         'adv_context': None}]
