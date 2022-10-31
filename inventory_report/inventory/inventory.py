import csv

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type):
        with open(file_path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=",", quotechar='"')
            docs_list = list(reader)

        if report_type == "simples":
            return SimpleReport.generate(docs_list)

        if report_type == "completo":
            return CompleteReport.generate(docs_list)

        raise ValueError(
            "Invalid report type, it needs to be 'simples' or 'completo'"
        )
