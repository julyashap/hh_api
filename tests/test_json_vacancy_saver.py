import pytest
from src.json_vacancy_saver import JSONVacancySaver
import os.path
from src.vacancy import Vacancy


@pytest.fixture()
def json_saver_exmpl():
    return JSONVacancySaver()


@pytest.fixture()
def vacancy_exmpl_from_to():
    return Vacancy('name', 'url', {'from': 10000, 'to': 35000},
                   'Lorem ipsum dolor sit amet consectetur adipisicing elit.')


@pytest.fixture()
def vacancy_exmpl_to():
    return Vacancy('name1', 'url1', {'from': None, 'to': 35000},
                   'Lorem ipsum dolor sit amet consectetur adipisicing elit.')


def test_add_vacancy(json_saver_exmpl, vacancy_exmpl_from_to, vacancy_exmpl_to):
    json_saver_exmpl.add_vacancy(vacancy_exmpl_from_to)
    json_saver_exmpl.add_vacancy(vacancy_exmpl_to)

    assert str(json_saver_exmpl.vacancies[0]) == "{'name': 'name', 'url': 'url', " \
                                                 "'salary': {'from': 10000, 'to': 35000}, " \
                                                 "'responsibility': 'Lorem ipsum dolor sit amet " \
                                                 "consectetur adipisicing elit.'}"
    assert str(json_saver_exmpl.vacancies[1]) == "{'name': 'name1', 'url': 'url1', " \
                                                 "'salary': {'from': 0, 'to': 35000}, " \
                                                 "'responsibility': 'Lorem ipsum dolor sit amet " \
                                                 "consectetur adipisicing elit.'}"

    with pytest.raises(ValueError, match="Должен быть передан объект класса Vacancy!"):
        json_saver_exmpl.add_vacancy(0)


def test_add_vacancies_to_json(json_saver_exmpl):
    path_to_file = os.path.join(json_saver_exmpl.file_with_vacancies)

    json_saver_exmpl.add_vacancies_to_json()

    with open(path_to_file, 'r') as file:
        content = file.read()

    assert content == '[{"name": "name", "url": "url", "salary": {"from": 10000, "to": 35000}, "responsibility": ' \
                      '"Lorem ipsum dolor sit amet consectetur adipisicing elit."}, {"name": "name1", "url": "url1", ' \
                      '"salary": {"from": 0, "to": 35000}, "responsibility": "Lorem ipsum dolor sit amet ' \
                      'consectetur adipisicing elit."}]'


def test_get_vacancy(json_saver_exmpl):
    assert type(json_saver_exmpl.get_vacancy('name', 'url')) == Vacancy


def test_delete_vacancy(json_saver_exmpl, vacancy_exmpl_from_to):
    path_to_file = os.path.join(json_saver_exmpl.file_with_vacancies)

    json_saver_exmpl.delete_vacancy(vacancy_exmpl_from_to)

    with open(path_to_file, 'r') as file:
        content = file.read()

    assert content == '[{"name": "name1", "url": "url1", "salary": {"from": 0, "to": 35000}, ' \
                      '"responsibility": "Lorem ipsum dolor sit amet consectetur adipisicing elit."}]'
