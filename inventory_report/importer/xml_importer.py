import xmltodict

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_nath: str):
        if not file_nath.endswith("xml"):
            raise ValueError("Arquivo inválido")

        with open(file_nath, encoding="utf-8") as file:
            docs_list = xmltodict.parse(file.read())["dataset"]["record"]

        return docs_list
