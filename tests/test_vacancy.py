import pytest
from src.vacancy import Vacancy


@pytest.fixture()
def vacancy_exmpl_from_to():
    return Vacancy('name', 'url', {'from': 10000, 'to': 35000},
                   'Lorem ipsum dolor sit amet consectetur adipisicing elit.')


@pytest.fixture()
def vacancy_exmpl_to():
    return Vacancy('name1', 'url1', {'from': None, 'to': 35000},
                   'Lorem ipsum dolor sit amet consectetur adipisicing elit.')


@pytest.fixture()
def vacancy_exmpl_from():
    return Vacancy('name2', 'url2', {'from': 10000, 'to': None},
                   'Lorem ipsum dolor sit amet consectetur adipisicing elit.')


@pytest.fixture()
def vacancy_exmpl_from_to_none():
    return Vacancy('name3', 'url3', {'from': None, 'to': None}, 'None')


@pytest.fixture()
def vacancy_exmpl_none():
    return Vacancy('name4', 'url4', None, None)


def test_init(vacancy_exmpl_from_to, vacancy_exmpl_to, vacancy_exmpl_from, vacancy_exmpl_none,
              vacancy_exmpl_from_to_none):
    assert vacancy_exmpl_from_to.name == 'name'
    with pytest.raises(ValueError, match="Название вакансии должно быть указано!"):
        Vacancy(None, 'url', {'from': 10000, 'to': 35000}, 'Text')

    assert vacancy_exmpl_from_to.url == 'url'
    with pytest.raises(ValueError, match="URL-адрес вакансии должен быть указан!"):
        Vacancy('name', None, {'from': 10000, 'to': 35000}, 'Text')

    assert str(vacancy_exmpl_from_to.get_salary) == "{'from': 10000, 'to': 35000}"
    assert str(vacancy_exmpl_to.get_salary) == "{'from': 0, 'to': 35000}"
    assert str(vacancy_exmpl_from.get_salary) == "{'from': 10000}"
    assert str(vacancy_exmpl_from_to_none.get_salary) == "{'from': 0, 'to': 0}"
    assert str(vacancy_exmpl_none.get_salary) == "{'from': 0, 'to': 0}"

    assert vacancy_exmpl_from_to.responsibility == "Lorem ipsum dolor sit amet consectetur adipisicing elit."
    assert vacancy_exmpl_from_to_none.responsibility == "Описание не указано"
    assert vacancy_exmpl_none.responsibility == "Описание не указано"


def test_get_salary(vacancy_exmpl_from_to):
    assert str(vacancy_exmpl_from_to.get_salary) == "{'from': 10000, 'to': 35000}"
    assert type(vacancy_exmpl_from_to.get_salary) == dict


def test_eq(vacancy_exmpl_from_to, vacancy_exmpl_from):
    bool_value = vacancy_exmpl_from_to == vacancy_exmpl_from

    assert bool_value is True


def test_ne(vacancy_exmpl_from_to, vacancy_exmpl_from):
    bool_value = vacancy_exmpl_from_to != vacancy_exmpl_from

    assert bool_value is False


def test_lt(vacancy_exmpl_to, vacancy_exmpl_from):
    bool_value = vacancy_exmpl_to < vacancy_exmpl_from

    assert bool_value is True


def test_gt(vacancy_exmpl_to, vacancy_exmpl_from):
    bool_value = vacancy_exmpl_to > vacancy_exmpl_from

    assert bool_value is False


def test_le(vacancy_exmpl_to, vacancy_exmpl_from):
    bool_value = vacancy_exmpl_to <= vacancy_exmpl_from

    assert bool_value is True


def test_ge(vacancy_exmpl_to, vacancy_exmpl_from):
    bool_value = vacancy_exmpl_to >= vacancy_exmpl_from

    assert bool_value is False


def test_repr(vacancy_exmpl_from_to):
    assert repr(vacancy_exmpl_from_to) == "Vacancy('name', 'url', {'from': 10000, 'to': 35000}, " \
                                          "'Lorem ipsum dolor sit amet consectetur adipisicing elit.')"


def test_str(vacancy_exmpl_from_to, vacancy_exmpl_from, vacancy_exmpl_to, vacancy_exmpl_none):
    assert str(vacancy_exmpl_from_to) == "Название: name, зарплата: 10000 - 35000, описание: Lorem ipsum dolor sit " \
                                         "amet consectetur adipisicing elit.\nСсылка: url"
    assert str(vacancy_exmpl_from) == "Название: name2, зарплата от 10000, описание: Lorem ipsum dolor sit " \
                                      "amet consectetur adipisicing elit.\nСсылка: url2"
    assert str(vacancy_exmpl_to) == "Название: name1, зарплата до 35000, описание: Lorem ipsum dolor sit " \
                                    "amet consectetur adipisicing elit.\nСсылка: url1"
    assert str(vacancy_exmpl_none) == "Название: name4, зарплата не указана :(, описание: Описание не указано" \
                                      "\nСсылка: url4"


def test_cast_to_object_list():
    list_to_cast = [{'name': 'name', 'url': 'url', 'salary': {'from': None, 'to': 20000},
                    'snippet': {'responsibility': 'Text'}},
                    {'name': 'name1', 'url': 'url1', 'salary': {'from': None, 'to': 20000},
                     'snippet': {'responsibility': 'Text'}}]

    object_list = Vacancy.cast_to_object_list(list_to_cast)

    for vacancy in object_list:
        assert type(vacancy) == Vacancy
