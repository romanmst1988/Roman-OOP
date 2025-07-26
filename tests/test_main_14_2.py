from unittest.mock import patch

import pytest

from main_14_2 import Category, Product  # Замените your_module на имя вашего файла


class TestProduct:
    @pytest.fixture
    def sample_product(self):
        return Product("Test Product", "Test Description", 100.0, 10)

    def test_initialization(self, sample_product):
        assert sample_product.name == "Test Product"
        assert sample_product.description == "Test Description"
        assert sample_product.price == 100.0
        assert sample_product.quantity == 10

    def test_price_property(self, sample_product):
        assert sample_product.price == 100.0

    def test_price_setter_valid(self, sample_product):
        sample_product.price = 150.0
        assert sample_product.price == 150.0

    def test_price_setter_negative(self, sample_product, capsys):
        sample_product.price = -50.0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert sample_product.price == 100.0  # Цена не изменилась

    def test_price_setter_zero(self, sample_product, capsys):
        sample_product.price = 0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert sample_product.price == 100.0  # Цена не изменилась

    @patch("builtins.input", return_value="y")
    def test_price_decrease_confirmed(self, mock_input, sample_product):
        sample_product.price = 80.0
        assert sample_product.price == 80.0

    @patch("builtins.input", return_value="n")
    def test_price_decrease_rejected(self, mock_input, sample_product, capsys):
        sample_product.price = 80.0
        captured = capsys.readouterr()
        assert "Изменение цены отменено" in captured.out
        assert sample_product.price == 100.0  # Цена не изменилась

    def test_new_product_no_duplicates(self):
        product_data = {"name": "New Product", "description": "New Desc", "price": 200.0, "quantity": 5}
        product = Product.new_product(product_data, [])
        assert product.name == "New Product"
        assert product.price == 200.0

    def test_new_product_with_duplicates(self):
        existing_product = Product("Existing Product", "Old Desc", 150.0, 3)
        product_data = {"name": "Existing Product", "description": "New Desc", "price": 200.0, "quantity": 5}
        result = Product.new_product(product_data, [existing_product])
        assert result == existing_product
        assert result.quantity == 5  # Количество обновилось
        assert result.price == 200.0  # Выбрана максимальная цена


class TestCategory:
    @pytest.fixture
    def sample_category(self):
        product1 = Product("Product1", "Desc1", 100.0, 5)
        product2 = Product("Product2", "Desc2", 200.0, 10)
        return Category("Test Category", "Test Description", [product1, product2])

    def test_initialization(self, sample_category):
        assert sample_category.name == "Test Category"
        assert sample_category.description == "Test Description"
        assert len(sample_category._Category__products) == 2
        assert Category.category_count == 1
        assert Category.product_count == 2


def test():
    category = Category("Игрушки", "Категория с игрушками", [])

    with pytest.raises(TypeError):
        category.add_product("не продукт")
