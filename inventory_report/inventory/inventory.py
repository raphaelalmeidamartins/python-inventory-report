import csv
import json

import xmltodict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type):
        with open(file_path, encoding="utf-8") as file:
            file_extension = file_path.split(".")[-1]

            if file_extension not in ["csv", "json", "xml"]:
                raise ValueError("Invalid file extension")

            read_methods = {
                "csv": cls.__read_csv,
                "json": cls.__read_json,
                "xml": cls.__read_xml,
            }

            docs_list = read_methods[file_extension](file)

        if report_type == "simples":
            return SimpleReport.generate(docs_list)

        if report_type == "completo":
            return CompleteReport.generate(docs_list)

        raise ValueError(
            "Invalid report type, it needs to be 'simples' or 'completo'"
        )

    @classmethod
    def __read_csv(cls, file):
        reader = csv.DictReader(file, delimiter=",", quotechar='"')
        docs_list = list(reader)
        return docs_list

    @classmethod
    def __read_json(cls, file):
        docs_list = json.load(file)
        return docs_list

    @classmethod
    def __read_xml(cls, file):
        docs_list = xmltodict.parse(file.read())["dataset"]["record"]
        return docs_list
