from src.hh import HH
from src.vacancy import Vacancy
from src.json_vacancy_saver import JSONVacancySaver


def top_n_vacancies(number: int, vacancies_list: list) -> list:
    if len(vacancies_list) <= number:
        return vacancies_list

    top_n_vacancies_list = [vacancies_list[i] for i in range(number)]
    return top_n_vacancies_list


def filter_vacancies(filter_words: list, vacancies_list: list) -> list:
    filtered_vacancies = []

    if not filter_words:
        return vacancies_list

    for vacancy in vacancies_list:
        if vacancy.responsibility == "Описание не указано":
            continue

        elif sum([filter_word.lower() in vacancy.responsibility.lower() for filter_word in filter_words]) > 0:
            filtered_vacancies.append(vacancy)

    return filtered_vacancies


def get_vacancies_by_salary(salary_range, vacancies_list: list) -> list:
    ranged_vacancies = []

    for vacancy in vacancies_list:
        if salary_range.isdigit():
            if int(salary_range) <= vacancy.get_salary['from']:
                ranged_vacancies.append(vacancy)
        else:
            if vacancy.get_salary.get('to') is not None and int(salary_range.split("-")[0]) \
                    >= vacancy.get_salary['from'] and vacancy.get_salary['to'] <= int(salary_range.split("-")[1]) \
                    or vacancy.get_salary.get('to') is not None and vacancy.get_salary['to'] <= \
                    int(salary_range.split("-")[1]) or int(salary_range.split("-")[0]) >= vacancy.get_salary['from']:

                ranged_vacancies.append(vacancy)

    return ranged_vacancies


def sort_vacancies(vacancies_list: list) -> list:
    sorted_vacancies = sorted(vacancies_list)

    return sorted_vacancies


def user_interaction():
    search_query = input("Введите поисковый запрос: ").strip()
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий через пробел: ").strip().split()
    salary_range = input("Введите минимальную зарплату или диапазон зарплат через '-': ").strip()

    hh_api = HH()
    vacancies = hh_api.load_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(vacancies)

    filtered_vacancies = filter_vacancies(filter_words, vacancies_list)
    ranged_vacancies = get_vacancies_by_salary(salary_range, filtered_vacancies)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = top_n_vacancies(top_n, sorted_vacancies)

    json_vacancy_saver = JSONVacancySaver()

    for index, top_vacancy in enumerate(top_vacancies):
        print(f"{index + 1}. {top_vacancy}")
        json_vacancy_saver.add_vacancy(top_vacancy)
    json_vacancy_saver.add_vacancies_to_json()
