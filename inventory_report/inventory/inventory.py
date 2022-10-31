from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    __read_strategies = {
        "csv": CsvImporter.import_data,
        "json": JsonImporter.import_data,
        "xml": XmlImporter.import_data,
    }

    __report_strategies = {
        "simples": SimpleReport,
        "completo": CompleteReport,
    }

    @classmethod
    def import_data(cls, file_path, report_type):
        file_extension = file_path.split(".")[-1]

        valid_extensions = list(cls.__read_strategies.keys())

        if file_extension not in valid_extensions:
            raise ValueError("Arquivo inválido")

        docs_list = cls.__read_strategies[file_extension](file_path)

        report_types = list(cls.__report_strategies.keys())

        if report_type not in report_types:
            raise ValueError(
                f"Invalid report type, "
                f"it needs to be one of the following {report_types}"
            )

        return cls.__report_strategies[report_type].generate(docs_list)
