from abc import ABC, abstractmethod


class APIVacancies(ABC):
    """Абстрактный класс для работы с API сайтов с вакансиями"""

    @abstractmethod
    def __init__(self):
        """Конструктор класса"""
        pass

    @abstractmethod
    def load_vacancies(self, keyword: str) -> list:
        """Метод для получения списка вакансий по запросу"""
        pass
