import pytest
from src.hh import HH


@pytest.fixture()
def hh_exmpl():
    return HH()


def test_init(hh_exmpl):
    assert hh_exmpl.url == 'https://api.hh.ru/vacancies'
    assert str(hh_exmpl.headers) == "{'User-Agent': 'HH-User-Agent'}"
    assert str(hh_exmpl.params) == "{'text': '', 'page': 0, 'per_page': 100}"
    assert str(hh_exmpl.vacancies) == "[]"


def test_load_vacancies(hh_exmpl):
    keyword = "python"

    assert hh_exmpl.load_vacancies(keyword)[0]['id'] == '96194079'
