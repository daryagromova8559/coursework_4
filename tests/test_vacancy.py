import pytest

from src.requests_hh import RequestHH
from src.vacancy import Vacancy


@pytest.fixture
def vac():
    vacs_list = Vacancy(240_000, 'Москва')
    return vacs_list


@pytest.fixture
def req():
    re_list = RequestHH('Разработчик')
    return re_list


def test_init1(req):
    assert req.name == 'Разработчик'
    req.get_url()
    req.status_api()
    req.save_info()


def test_init2(vac):
    assert vac.salary == 240000
    assert vac.city == 'Москва'
    assert vac.vacancy() == [
        {'id': '95695925', 'premium': False, 'name': 'Junior Blockchain Developer', 'department': None,
         'has_test': False, 'response_letter_required': False,
         'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
         'salary': {'from': 250000, 'to': None, 'currency': 'RUR', 'gross': False},
         'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None,
         'published_at': '2024-03-28T13:00:21+0300', 'created_at': '2024-03-28T13:00:21+0300', 'archived': False,
         'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=95695925',
         'show_logo_in_search': None, 'insider_interview': None,
         'url': 'https://api.hh.ru/vacancies/95695925?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/95695925',
         'relations': [],
         'employer': {'id': '6076281', 'name': 'SHiFT AM', 'url': 'https://api.hh.ru/employers/6076281',
                      'alternate_url': 'https://hh.ru/employer/6076281',
                      'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/946532.png',
                                    '240': 'https://img.hhcdn.ru/employer-logo/4226665.png',
                                    '90': 'https://img.hhcdn.ru/employer-logo/4226664.png'},
                      'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=6076281',
                      'accredited_it_employer': False, 'trusted': True}, 'snippet': {
            'requirement': 'Cтэк: python / typescript / solidity / redis / PostgreSQL / mogo db / hardhat / fatsapi / asyncio / hardhat. Понимание технологических рисков DeFi, желателен опыт аудита и...',
            'responsibility': 'Развивать dApp shift.tech как в ончейн части, так и на стороне backend. Участвовать в разработке наших финансовых продуктов: смарт-контракты...'},
         'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
         'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
         'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False,
         'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
         'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
         'adv_context': None},
        {'id': '95395666', 'premium': False, 'name': 'Ведущий программист 1С, г. Москва (офис)', 'department': None,
         'has_test': False, 'response_letter_required': False,
         'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
         'salary': {'from': 460000, 'to': 517000, 'currency': 'RUR', 'gross': True},
         'type': {'id': 'open', 'name': 'Открытая'},
         'address': {'city': 'Москва', 'street': 'Киевская улица', 'building': '7к2', 'lat': 55.742098, 'lng': 37.55893,
                     'description': None, 'raw': 'Москва, Киевская улица, 7к2',
                     'metro': {'station_name': 'Киевская', 'line_name': 'Кольцевая', 'station_id': '5.49',
                               'line_id': '5', 'lat': 55.74361, 'lng': 37.56735}, 'metro_stations': [
                 {'station_name': 'Киевская', 'line_name': 'Кольцевая', 'station_id': '5.49', 'line_id': '5',
                  'lat': 55.74361, 'lng': 37.56735}], 'id': '11942015'}, 'response_url': None,
         'sort_point_distance': None, 'published_at': '2024-03-28T08:22:20+0300',
         'created_at': '2024-03-28T08:22:20+0300', 'archived': False,
         'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=95395666',
         'branding': {'type': 'CONSTRUCTOR', 'tariff': 'BASIC'}, 'show_logo_in_search': True, 'insider_interview': None,
         'url': 'https://api.hh.ru/vacancies/95395666?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/95395666',
         'relations': [],
         'employer': {'id': '195848', 'name': 'Трансстроймеханизация', 'url': 'https://api.hh.ru/employers/195848',
                      'alternate_url': 'https://hh.ru/employer/195848',
                      'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/193024.png',
                                    '240': 'https://img.hhcdn.ru/employer-logo/1081713.png',
                                    '90': 'https://img.hhcdn.ru/employer-logo/1081712.png'},
                      'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=195848',
                      'accredited_it_employer': False, 'trusted': True}, 'snippet': {
            'requirement': 'Образование выше среднего профессионального. Наличие сертификатов 1С: Специалист по платформе – приветствуется. Знание 1С:ERP (производство и ремонты) - приветствуется. ',
            'responsibility': 'Дорабатывать конфигурации под требования организации. Выяснение причин поведения программ, Поиск и исправление ошибок. Оптимизация кода/запросов. Подготовка к обновлению релизов.'},
         'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
         'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
         'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False,
         'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
         'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
         'adv_context': None}]
