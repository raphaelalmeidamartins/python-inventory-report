from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor:
    __report_strategies = {
        "simples": SimpleReport,
        "completo": CompleteReport,
    }

    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, file_path, report_type):
        self.data.extend(self.importer.import_data(file_path))

        report_types = list(self.__report_strategies.keys())

        if report_type not in report_types:
            raise ValueError(
                f"Invalid report type, "
                f"it needs to be one of the following {report_types}"
            )

        return self.__report_strategies[report_type].generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
