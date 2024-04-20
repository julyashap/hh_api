from src.vacancy_saver import VacancySaver
from src.vacancy import Vacancy
import json


class JSONVacancySaver(VacancySaver):
    """Класс для сохранения данных о вакансии в JSON-файл"""

    file_with_vacancies = "file_with_vacancies.json"
    vacancies = []

    def add_vacancy(self, vacancy: Vacancy):
        """Метод для добавления вакансии в список вакансий"""

        if isinstance(vacancy, Vacancy):
            vacancy_dict = {'name': vacancy.name, 'url': vacancy.url,
                            'salary': vacancy.get_salary,
                            'responsibility': vacancy.responsibility}
            self.vacancies.append(vacancy_dict)
        else:
            raise ValueError("Должен быть передан объект класса Vacancy!")

    def add_vacancies_to_json(self):
        """Метод для добавления вакансии в JSON-файл"""

        with open(self.file_with_vacancies, 'w') as file:
            json.dump(self.vacancies, file)

    def get_vacancy(self, name_of_vacancy: str, url_of_vacancy: str) -> dict:
        """Метод для получения вакансии по названию и url-адресу"""

        for vacancy in self.vacancies:
            if vacancy['name'] == name_of_vacancy and vacancy['url'] == url_of_vacancy:
                return Vacancy(vacancy['name'], vacancy['url'], vacancy['salary'],
                               vacancy['responsibility'])

    def delete_vacancy(self, vacancy: Vacancy):
        """Метод для удаления вакансии из JSON-файла"""

        dict_to_remove = {'name': vacancy.name, 'url': vacancy.url,
                          'salary': vacancy.get_salary,
                          'responsibility': vacancy.responsibility}

        self.vacancies.remove(dict_to_remove)

        with open(self.file_with_vacancies, 'w') as file:
            json.dump(self.vacancies, file)
