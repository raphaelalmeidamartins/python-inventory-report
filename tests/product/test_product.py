from inventory_report.inventory.product import Product


def test_cria_produto():
    mock_product = {
        "id": 1,
        "nome_da_empresa": "Elma Chips",
        "nome_do_produto": "Batata Frita Ondulada Original Ruffles 76g",
        "data_de_fabricacao": "2022/10/30",
        "data_de_validade": "2023/02/30",
        "numero_de_serie": "1S26 2B4K 69WX UY57",
        "instrucoes_de_armazenamento": "Guarde em local arejado.",
    }

    produto = Product(**mock_product)

    for key, value in mock_product.items():
        assert getattr(produto, key) == value
