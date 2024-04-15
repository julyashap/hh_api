class Vacancy:
    """Класс для обработки вакансии"""

    def __init__(self, name: str, url: str, salary, employment: str):
        """Конструктор класса Vacancy"""

        self.validate_data(name, url, salary, employment)

        self.name = name
        self.url = url

        if isinstance(salary, float):
            self.__salary = {"from": salary}
        elif isinstance(salary, str):
            if salary == '':
                self.__salary = {"from": 0}
            self.__salary = {"to": float(salary.split("-")[1]), "from": float(salary.split("-")[0])}

        self.employment = {"name": employment}

    @staticmethod
    def validate_data(name, url, salary, employment):
        """Метод, проверяющий входные данные на соответствие типам"""

        if not isinstance(name, str):
            raise ValueError("Название вакансии должно быть строкой!")
        elif not isinstance(url, str):
            raise ValueError("Ссылка на вакансию должна быть строкой!")
        elif not isinstance(employment, str):
            raise ValueError("Параметр занятости должен быть строкой!")
        elif not isinstance(salary, (float, str)):
            raise ValueError("Зарплата должна быть только типа float или str!")

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
