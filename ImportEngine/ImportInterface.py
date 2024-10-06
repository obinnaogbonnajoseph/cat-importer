from abc import ABC, abstractmethod
from typing import List

from .Cat import Cat


class ImportInterface(ABC):
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the file can be parsed, based on the allowed extensions

        Args:
            path (str): file path

        Returns:
            bool: Can the file be parsed
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Cat]:
        """Abstract method to parse a file to return a list of Cat objects

        Args:
            path (str): file path

        Returns:
            List[Cat]: list of Cat objects
        """
        pass

    @staticmethod
    def parse_str(string: str) -> Cat:
        """Static method to parse a string to return a Cat object

        Args:
            string (str): String to parse: 'name, age, is_indoor'

        Returns:
            Cat: a Cat object
        """
        parse = string.split(',')
        return Cat(parse[0], int(parse[1]), bool(parse[2]))
