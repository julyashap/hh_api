from src.api_vacancies import APIVacancies
import requests


class HH(APIVacancies):
    """Класс для работы с API сайта hh.ru"""

    def __init__(self):
        """Конструктор класса HH"""

        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword: str) -> list:
        """Метод для получения списка вакансий по запросу"""

        self.params['text'] = keyword

        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

        return self.vacancies
