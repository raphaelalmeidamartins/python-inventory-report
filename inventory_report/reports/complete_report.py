import datetime
import statistics
from collections import Counter


class CompleteReport:
    @classmethod
    def generate(cls, products):
        man_dates = [
            cls.__generate_date_object(product["data_de_fabricacao"])
            for product in products
        ]
        exp_dates = [
            cls.__generate_date_object(product["data_de_validade"])
            for product in products
        ]
        companies = [product["nome_da_empresa"] for product in products]

        oldest_man_date = min(man_dates).strftime("%Y-%m-%d")
        closest_exp_date = min(exp_dates).strftime("%Y-%m-%d")

        report = (
            f"Data de fabricação mais antiga: {oldest_man_date}\n"
            f"Data de validade mais próxima: {closest_exp_date}\n"
            f"Empresa com mais produtos: {statistics.mode(companies)}\n"
            f"Produtos estocados por empresa:\n"
        )

        # Danillo Gonçalves da T19A me deu a dica de usar a classe Counter

        qnty_per_company = Counter(companies)

        for company, quantity in qnty_per_company.items():
            report += f"- {company}: {quantity}\n"

        return report

    @classmethod
    def __generate_date_object(cls, date_string):
        return datetime.datetime(
            year=int(date_string[0:4]),
            month=int(date_string[5:7]),
            day=int(date_string[8:10]),
        )
