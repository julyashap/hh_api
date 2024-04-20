from abc import ABC, abstractmethod


class VacancySaver(ABC):
    """Абстрактный класс для сохранения данных о вакансии"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        """Абстрактный метод для добавления вакансии в список вакансий"""
        pass

    @abstractmethod
    def add_vacancies_to_json(self):
        """Абстрактный метод для добавления вакансии в файловую структуру"""
        pass

    @abstractmethod
    def get_vacancy(self, name_of_vacancy, url_of_vacancy):
        """Абстрактный метод для получения вакансии по названию и url-адресу"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """Абстрактный метод для удаления вакансии из файловой структуры"""
        pass
