from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    products_list = [
        {
            "id": "1",
            "nome_do_produto": "Nicotine Polacrilex",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2021-02-18",
            "data_de_validade": "2023-09-17",
            "numero_de_serie": "CR25 1551 4467 2549 4402 1",
            "instrucoes_de_armazenamento": "instrucao 1",
        },
        {
            "id": "2",
            "nome_do_produto": "fentanyl citrate",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2020-12-06",
            "data_de_validade": "2023-12-25",
            "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
            "instrucoes_de_armazenamento": "instrucao 2",
        },
        {
            "id": "3",
            "nome_do_produto": "NITROUS OXIDE",
            "nome_da_empresa": "Galena Biopharma",
            "data_de_fabricacao": "2020-12-22",
            "data_de_validade": "2024-11-07",
            "numero_de_serie": "CZ09 8588 0858 8435 9140 2695",
            "instrucoes_de_armazenamento": "instrucao 3",
        },
        {
            "id": "4",
            "nome_do_produto": "Norepinephrine Bitartrate",
            "nome_da_empresa": "Cantrell Drug Company",
            "data_de_fabricacao": "2020-12-24",
            "data_de_validade": "2025-08-19",
            "numero_de_serie": "MT04 VJPY 0772 3DCE K8U3 WIVL VV3K AEN",
            "instrucoes_de_armazenamento": "instrucao 4",
        },
        {
            "id": "5",
            "nome_do_produto": "ACETAMINOPHEN, PHENYLEPHRINE HYDROCHLORIDE",
            "nome_da_empresa": "Moore Medical LLC",
            "data_de_fabricacao": "2021-04-14",
            "data_de_validade": "2025-01-14",
            "numero_de_serie": "LV23 ELDS 2GD5 X19P VCSI K",
            "instrucoes_de_armazenamento": "instrucao 5",
        },
        {
            "id": "6",
            "nome_do_produto": "Silicea Belladonna",
            "nome_da_empresa": "Cantrell Drug Company",
            "data_de_fabricacao": "2021-07-18",
            "data_de_validade": "2024-10-05",
            "numero_de_serie": "FR57 7414 7254 046O IHVX AV6L H71",
            "instrucoes_de_armazenamento": "instrucao 6",
        },
        {
            "id": "7",
            "nome_do_produto": "Spironolactone",
            "nome_da_empresa": "REMEDYREPACK",
            "data_de_fabricacao": "2021-07-17",
            "data_de_validade": "2023-11-18",
            "numero_de_serie": "SM28 B981 5118 903W JY0C 5KVO 3QD",
            "instrucoes_de_armazenamento": "instrucao 7",
        },
        {
            "id": "8",
            "nome_do_produto": "Aspirin",
            "nome_da_empresa": "Galena Biopharma",
            "data_de_fabricacao": "2021-02-22",
            "data_de_validade": "2024-03-14",
            "numero_de_serie": "KZ63 800H NM4B ZOWB YYUI",
            "instrucoes_de_armazenamento": "instrucao 8",
        },
        {
            "id": "9",
            "nome_do_produto": "eucalyptus globulus",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2020-09-06",
            "data_de_validade": "2024-05-21",
            "numero_de_serie": "GT74 LHWJ FCXL JNQT ZCXM 4761 GWSP",
            "instrucoes_de_armazenamento": "instrucao 9",
        },
        {
            "id": "10",
            "nome_do_produto": "Titanium Dioxide",
            "nome_da_empresa": "Target Corporation",
            "data_de_fabricacao": "2020-12-08",
            "data_de_validade": "2023-12-08",
            "numero_de_serie": "FR29 5791 5333 58XR G4PR IG28 D08",
            "instrucoes_de_armazenamento": "instrucao 10",
        },
    ]

    colored_keys = [
        "\033[32mData de fabricação mais antiga:\033[0m",
        "\033[32mData de validade mais próxima:\033[0m",
        "\033[32mEmpresa com mais produtos:\033[0m",
    ]

    colored_values = [
        "\033[36m2020-09-06\033[0m",
        "\033[36m2023-09-17\033[0m",
        "\033[31mTarget Corporation\033[0m",
    ]

    expected_simple_report = (
        f"{colored_keys[0]} {colored_values[0]}\n"
        f"{colored_keys[1]} {colored_values[1]}\n"
        f"{colored_keys[2]} {colored_values[2]}"
    )

    expected_complete_report = (
        f"{colored_keys[0]} {colored_values[0]}\n"
        f"{colored_keys[1]} {colored_values[1]}\n"
        f"{colored_keys[2]} {colored_values[2]}\n"
        "Produtos estocados por empresa:\n"
        "- Target Corporation: 4\n"
        "- Galena Biopharma: 2\n"
        "- Cantrell Drug Company: 2\n"
        "- Moore Medical LLC: 1\n"
        "- REMEDYREPACK: 1\n"
    )

    colored_simple_report = ColoredReport(SimpleReport).generate(products_list)
    colored_complete_report = ColoredReport(CompleteReport).generate(
        products_list
    )

    assert colored_simple_report == expected_simple_report
    assert colored_complete_report == expected_complete_report
