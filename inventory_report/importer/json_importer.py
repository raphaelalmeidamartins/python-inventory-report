import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path: str):
        if not file_path.endswith("json"):
            raise ValueError("Arquivo inválido")

        with open(file_path, encoding="utf-8") as file:
            docs_list = json.load(file)

        return docs_list
