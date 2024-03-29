from src.vacancy import Vacancy
from src.requests_hh import RequestHH


def main():
    print("Введите пожалуйста, вакансию которую хотели бы найти")
    user_name = input().title()
    while True:
        print("Введите пожалуйста, зарплату которую хотели бы получать")
        user_salary = int(input())
        if type(user_salary) is int:
            break
        print("Попробуйте еще!")

    while True:
        print("Введите пожалуйста, город где хотели бы найти работу")
        user_city = input().title()
        if type(user_city) is str:
            break
        print("Попробуйте еще!")
    user = Vacancy(salary=user_salary, city=user_city)
    get_api = RequestHH(name=user_name)
    get_api.get_url()
    get_api.status_api()
    get_api.save_info()
    user.vacancy()
    user.construction()
    user.top_vacancy()
    user.__str__()


if __name__ == '__main__':
    main()

    