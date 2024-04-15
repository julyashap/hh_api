class Vacancy:
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

        # self.validate_data(name, url, salary, experience)

        if not name:
            raise ValueError("Название вакансии должно быть указано!")
        self.name = name

        if not url:
            raise ValueError("URL-адрес вакансии должен быть указан!")
        self.url = url

        if not salary:
            self.__salary = {"from": 0}
        elif isinstance(salary, float):
            self.__salary = {"from": salary}
        elif isinstance(salary, str):
            self.__salary = {"to": float(salary.split("-")[1]), "from": float(salary.split("-")[0])}

        if not experience:
            self.experience = 0
        self.experience = experience

    # @staticmethod
    # def validate_data(name, url, salary, experience):
    #     """Метод, проверяющий входные данные на соответствие типам"""
    #
    #     if not isinstance(name, str):
    #         raise ValueError("Название вакансии должно быть строкой!")
    #     elif not isinstance(url, str):
    #         raise ValueError("Ссылка на вакансию должна быть строкой!")
    #     elif not isinstance(experience, (float, str)):
    #         raise ValueError("Опыт работы должен быть типа float или str!")
    #     elif not isinstance(salary, (float, str)):
    #         raise ValueError("Зарплата должна быть типа float или str!")
    #
    #     pass

    @property
    def get_salary(self) -> dict:
        """Геттер для зарплаты"""

        return self.__salary

    @get_salary.setter
    def set_salary(self, salary):
        """Сеттер для зарплаты"""

        if isinstance(salary, float):
            self.__salary = {"from": salary}
        elif isinstance(salary, str):
            self.__salary = {"to": float(salary.split("-")[1]), "from": float(salary.split("-")[0])}

    def __le__(self, other) -> bool:
        """Магический метод для сравнения 'меньше или равно' зарплат"""

        return self.__salary <= other.salary

    def __ge__(self, other) -> bool:
        """Магический метод для сравнения 'больше или равно' зарплат"""

        return self.__salary >= other.salary
