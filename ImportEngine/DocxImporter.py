from typing import List
import docx

from .ImportInterface import ImportInterface
from .Cat import Cat


class DocxImporter(ImportInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        if not cls.can_ingest(path):
            raise ValueError('cannot ingest exception')

        cats = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                cats.append(ImportInterface.parse_str(para.text))

        return cats
