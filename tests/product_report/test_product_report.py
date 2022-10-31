from inventory_report.inventory.product import Product


def test_relatorio_produto():
    mock = {
        "id": 1,
        "nome_da_empresa": "Elma Chips",
        "nome_do_produto": "Batata Frita Ondulada Original Ruffles 76g",
        "data_de_fabricacao": "2022/10/30",
        "data_de_validade": "2023/02/30",
        "numero_de_serie": "1S26 2B4K 69WX UY57",
        "instrucoes_de_armazenamento": "Guarde em local arejado.",
    }

    product = Product(**mock)

    expected = (
        f"O produto {mock['nome_do_produto']}"
        f" fabricado em {mock['data_de_fabricacao']}"
        f" por {mock['nome_da_empresa']} com validade"
        f" até {mock['data_de_validade']}"
        f" precisa ser armazenado {mock['instrucoes_de_armazenamento']}."
    )

    assert repr(product) == expected
