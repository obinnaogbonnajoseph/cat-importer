from typing import List

from .ImportInterface import ImportInterface
from .Cat import Cat
from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter
from .PDFImporter import PDFImporter


class Importer(ImportInterface):
    importers: List[ImportInterface] = [DocxImporter, CSVImporter, PDFImporter]

    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        """Parses a file to return a list of Cat objects

        Args:
            path (str): file path

        Returns:
            List[Cat]: list of Cat objects
        """
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
