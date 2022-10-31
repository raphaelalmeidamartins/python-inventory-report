import statistics
import datetime


class SimpleReport:
    def generate_date_object(date_string: str):
        return datetime.datetime(
            year=int(date_string[0:4]),
            month=int(date_string[5:7]),
            day=int(date_string[8:10]),
        )

    @classmethod
    def generate(self, products: list[dict]):
        man_dates = [
            self.generate_date_object(product["data_de_fabricacao"])
            for product in products
        ]
        exp_dates = [
            self.generate_date_object(product["data_de_validade"])
            for product in products
        ]
        companies = [product["nome_da_empresa"] for product in products]

        oldest_man_date = min(man_dates).strftime("%Y-%m-%d")
        closest_exp_date = min(exp_dates).strftime("%Y-%m-%d")

        return (
            f"Data de fabricação mais antiga: {oldest_man_date}\n"
            f"Data de validade mais próxima: {closest_exp_date}\n"
            f"Empresa com mais produtos: {statistics.mode(companies)}"
        )

    # @classmethod
    # def __generate_date_object(cls, date_string: str):
    #     return datetime.datetime(
    #         year=int(date_string[0:4]),
    #         month=int(date_string[5:7]),
    #         day=int(date_string[8:10]),
    #     )
