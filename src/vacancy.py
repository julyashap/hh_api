class Vacancy():
    """Класс для обработки вакансии"""

    @classmethod
    def cast_to_object_list(cls, vacancies_list):
        """Класс-метод для создания списка объектов Vacancy из списка вакансий в формате JSON"""

        vacancies_object_list = []

        for vacancy in vacancies_list:
            vacancy_object = cls(vacancy['name'], vacancy['url'], vacancy['salary'], vacancy['experience']['name'])
            vacancies_object_list.append(vacancy_object)

        return vacancies_object_list

    def __init__(self, name: str, url: str, salary, experience):
        """Конструктор класса Vacancy"""

        if not name:
            raise ValueError("Название вакансии должно быть указано!")
        self.name = name

        if not url:
            raise ValueError("URL-адрес вакансии должен быть указан!")
        self.url = url

        if not salary:
            self.__salary = {"from": 0}
        elif isinstance(salary, (int, float)):
            self.__salary = {"from": salary}
        elif isinstance(salary, str):
            self.__salary = {"to": float(salary.split("-")[1]), "from": float(salary.split("-")[0])}

        if not experience:
            self.experience = 0
        self.experience = experience

    @property
    def get_salary(self) -> dict:
        """Геттер для зарплаты"""

        return self.__salary

    @get_salary.setter
    def set_salary(self, salary):
        """Сеттер для зарплаты"""

        if isinstance(salary, (int, float)):
            self.__salary = {"from": salary}
        elif isinstance(salary, str):
            self.__salary = {"to": float(salary.split("-")[1]), "from": float(salary.split("-")[0])}

    def __le__(self, other) -> bool:
        """Магический метод для сравнения 'меньше или равно' зарплат"""

        return self.__salary['from'] <= other.salary['from']

    def __ge__(self, other) -> bool:
        """Магический метод для сравнения 'больше или равно' зарплат"""

        return self.__salary['from'] >= other.salary['from']

    def __repr__(self):
        """Магический метод для отображения созданного экземпляра класса Vacancy"""

        return f"Vacancy('{self.name}', '{self.url}', {self.__salary}, '{self.experience}')"
