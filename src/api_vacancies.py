from abc import ABC, abstractmethod


class APIVacancies(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword: str) -> list:
        pass
