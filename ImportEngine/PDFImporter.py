from typing import List
import subprocess
import os
import random

from .ImportInterface import ImportInterface
from .Cat import Cat


class PDFImporter(ImportInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        if not cls.can_ingest(path):
            raise ValueError('cannot ingest exception')

        tmp = f'./tmp/{random.randint(0,100000000)}.txt'
        subprocess.call(['pdftotext', path, tmp])

        cats = []
        with open(tmp, 'r') as file_ref:
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    cats.append(ImportInterface.parse_str(line))

            os.remove(tmp)
        return cats
