import csv

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def read(file_path):
    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",", quotechar='"')
        docs_list = list(reader)

    return docs_list


class Inventory:
    @staticmethod
    def import_data(file_path: str, report_type: str):

        docs_list = read(file_path)

        if report_type == "simples":
            return SimpleReport.generate(docs_list)

        if report_type == "completo":
            return CompleteReport.generate(docs_list)

        raise ValueError(
            "Invalid report type, it needs to be 'simples' or 'completo'"
        )
