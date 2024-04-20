import pytest
from src.utils import top_n_vacancies, filter_vacancies, sort_vacancies, get_vacancies_by_salary, user_interaction
from src.vacancy import Vacancy


@pytest.fixture()
def vacancies_list():
    return [
        Vacancy('name', 'url', {'from': 10500, 'to': 35000},
                'Lorem ipsum dolor sit amet consectetur adipisicing elit.'),
        Vacancy('name1', 'url1', {'from': None, 'to': 35000},
                'Lorem ipsum dolor sit amet consectetur adipisicing elit.'),
        Vacancy('name2', 'url2', {'from': 10000, 'to': None},
                'Описание не указано')
            ]


def test_top_n_vacancies(vacancies_list):
    result_of_function_1 = top_n_vacancies(2, vacancies_list)
    assert len(result_of_function_1) == 2

    result_of_function_2 = top_n_vacancies(5, vacancies_list)
    assert len(result_of_function_2) == 3


def test_filter_vacancies(vacancies_list):
    result_of_function_1 = filter_vacancies(['Lorem', 'sit'], vacancies_list)
    assert result_of_function_1[0].name == 'name'
    assert result_of_function_1[1].name == 'name1'
    assert len(result_of_function_1) == 2

    result_of_function_2 = filter_vacancies([], vacancies_list)
    assert len(result_of_function_2) == 3


def test_get_vacancies_by_salary(vacancies_list):
    result_of_function_1 = get_vacancies_by_salary('10000', vacancies_list)
    result_of_function_2 = get_vacancies_by_salary('10000-35000', vacancies_list)

    assert result_of_function_1[0].name == 'name'
    assert result_of_function_1[1].name == 'name2'

    assert result_of_function_2[0].name == 'name'


def test_sort_vacancies(vacancies_list):
    result_of_function = sort_vacancies(vacancies_list)

    assert result_of_function[0].name == 'name1'
    assert result_of_function[1].name == 'name2'
    assert result_of_function[2].name == 'name'
