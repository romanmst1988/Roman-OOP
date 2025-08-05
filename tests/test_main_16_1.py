import pytest

from main_16_1 import Category, LawnGrass, Product, Smartphone


class TestProduct:
    """Тесты для класса Product"""

    def test_product_initialization(self):
        """Тест инициализации продукта"""
        product = Product("Телевизор", "4K OLED", 100000.0, 5)
        assert product.name == "Телевизор"
        assert product.description == "4K OLED"
        assert product.price == 100000.0
        assert product.quantity == 5

    def test_product_str(self):
        """Тест строкового представления продукта"""
        product = Product("Телевизор", "4K OLED", 100000.0, 5)
        assert str(product) == "Телевизор, 100000.0 руб. Остаток: 5 шт."

    def test_product_add(self):
        """Тест сложения продуктов"""
        product1 = Product("Телевизор", "4K OLED", 100000.0, 2)
        product2 = Product("Телевизор", "4K OLED", 150000.0, 3)
        assert product1 + product2 == (100000.0 * 2) + (150000.0 * 3)

    def test_product_add_different_classes(self):
        """Тест сложения продуктов разных классов"""
        product = Product("Телевизор", "4K OLED", 100000.0, 2)
        smartphone = Smartphone("iPhone", "Pro", 200000.0, 1, 95.0, "15", 256, "Black")
        with pytest.raises(TypeError):
            product + smartphone

    def test_price_setter_negative(self):
        """Тест установки отрицательной цены"""
        product = Product("Телевизор", "4K OLED", 100000.0, 5)
        product.price = -50000.0
        assert product.price == 100000.0  # Цена не должна измениться

    def test_price_setter_lower_price_confirmation(self, monkeypatch):
        """Тест подтверждения понижения цены"""
        product = Product("Телевизор", "4K OLED", 100000.0, 5)

        # Эмулируем ввод 'y' (подтверждение)
        monkeypatch.setattr("builtins.input", lambda _: "y")
        product.price = 90000.0
        assert product.price == 90000.0

        # Эмулируем ввод 'n' (отмена)
        monkeypatch.setattr("builtins.input", lambda _: "n")
        product.price = 80000.0
        assert product.price == 90000.0  # Цена осталась прежней

    def test_new_product_duplicate(self):
        """Тест создания нового продукта с дубликатом"""
        existing_products = [Product("Телевизор", "4K OLED", 100000.0, 5)]
        new_product_data = {"name": "Телевизор", "description": "8K QLED", "price": "150000.0", "quantity": "3"}
        new_product = Product.new_product(new_product_data, existing_products)
        assert new_product.price == 150000.0  # Выбрана максимальная цена

    def test_new_product_no_duplicate(self):
        """Тест создания нового продукта без дубликатов"""
        existing_products = [Product("Телевизор", "4K OLED", 100000.0, 5)]
        new_product_data = {"name": "Смартфон", "description": "OLED", "price": "80000.0", "quantity": "10"}
        new_product = Product.new_product(new_product_data, existing_products)
        assert new_product.name == "Смартфон"
        assert new_product not in existing_products


class TestCategory:
    """Тесты для класса Category"""

    def test_category_initialization(self):
        """Тест инициализации категории"""
        product = Product("Телевизор", "4K OLED", 100000.0, 5)
        category = Category("Электроника", "Техника", [product])
        assert category.name == "Электроника"
        assert category.description == "Техника"
        assert len(category._Category__products) == 1
        assert category._Category__products_count == 1

    def test_category_str(self):
        """Тест строкового представления категории"""
        product1 = Product("Телевизор", "4K OLED", 100000.0, 5)
        product2 = Product("Ноутбук", "16GB RAM", 150000.0, 3)
        category = Category("Электроника", "Техника", [product1, product2])
        assert str(category) == "Электроника, количество продуктов: 8 шт."

    def test_add_product(self):
        """Тест добавления продукта в категорию"""
        Category.product_count = 0  # Сбрасываем счетчик перед тестом
        category = Category("Электроника", "Техника", [])
        product = Product("Телевизор", "4K OLED", 100000.0, 5)
        category.add_product(product)
        assert len(category._Category__products) == 1
        assert Category.product_count == 1

    def test_add_invalid_product(self):
        """Тест добавления невалидного продукта (не Product)"""
        category = Category("Электроника", "Техника", [])
        with pytest.raises(TypeError):
            category.add_product("Not a product")


class TestSmartphone:
    """Тесты для класса Smartphone"""

    def test_smartphone_initialization(self):
        """Тест инициализации смартфона"""
        smartphone = Smartphone("iPhone", "Pro", 200000.0, 1, 95.0, "15", 256, "Black")
        assert smartphone.name == "iPhone"
        assert smartphone.price == 200000.0
        assert smartphone.efficiency == 95.0
        assert smartphone.model == "15"
        assert smartphone.memory == 256
        assert smartphone.color == "Black"


class TestLawnGrass:
    """Тесты для класса LawnGrass"""

    def test_lawn_grass_initialization(self):
        """Тест инициализации газонной травы"""
        grass = LawnGrass("Трава", "Зеленая", 500.0, 10, "Россия", "7 дней", "Зеленый")
        assert grass.name == "Трава"
        assert grass.price == 500.0
        assert grass.country == "Россия"
        assert grass.germination_period == "7 дней"
        assert grass.color == "Зеленый"
