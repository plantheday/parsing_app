import requests
import json

from abc import ABC, abstractmethod

class ParentApi(ABC):
    """Родительский класс,для работы с API"""

    @abstractmethod
    def get_request(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class ParentJSONSaver(ABC):
    """Родительский класс для работы с данными о вакансиях """

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def select(self):
        pass


class HeadHunterAPI(ParentApi):
    """Класс для работы с API HeadHunter"""

