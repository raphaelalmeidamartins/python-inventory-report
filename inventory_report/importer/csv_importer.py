import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path: str):
        if not file_path.endswith('csv'):
            raise ValueError("Arquivo inválido")

        with open(file_path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            docs_list = list(reader)

        return docs_list
