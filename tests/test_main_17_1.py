import pytest
from main_17_1 import Product, Smartphone, LawnGrass, Category


class TestProduct:
    """Тесты для класса Product"""

    def test_product_creation(self):
        """Тест создания продукта с корректными параметрами"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        assert product.name == "Телефон"
        assert product.description == "Смартфон"
        assert product.price == 50000.0
        assert product.quantity == 10

    def test_product_zero_quantity(self):
        """Тест создания продукта с нулевым количеством"""
        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
            Product("Бракованный", "Товар", 1000.0, 0)

    def test_price_setter_negative(self):
        """Тест установки отрицательной цены"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        product.price = -1000
        assert product.price == 50000.0  # Цена не должна измениться

    def test_price_setter_zero(self):
        """Тест установки нулевой цены"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        product.price = 0
        assert product.price == 50000.0  # Цена не должна измениться

    def test_str_method(self):
        """Тест строкового представления"""
        product = Product("Телефон", "Смартфон", 50000.0, 10)
        assert str(product) == "Телефон, 50000.0 руб. Остаток: 10 шт."

    def test_add_method(self):
        """Тест сложения продуктов"""
        p1 = Product("Товар1", "Описание", 100.0, 5)
        p2 = Product("Товар2", "Описание", 200.0, 3)
        assert p1 + p2 == 100.0 * 5 + 200.0 * 3

    def test_add_method_different_classes(self):
        """Тест сложения продуктов разных классов"""
        p1 = Product("Товар1", "Описание", 100.0, 5)
        p2 = Smartphone("Товар2", "Описание", 200.0, 3, "high", "X", "128GB", "black")
        with pytest.raises(TypeError, match="Нельзя складывать объекты разных классов"):
            p1 + p2


class TestSmartphone:
    """Тесты для класса Smartphone"""

    def test_smartphone_creation(self):
        """Тест создания смартфона"""
        phone = Smartphone("iPhone", "Смартфон", 100000.0, 5, "high", "15", "256GB", "black")
        assert phone.name == "iPhone"
        assert phone.price == 100000.0
        assert phone.efficiency == "high"
        assert phone.model == "15"
        assert phone.memory == "256GB"
        assert phone.color == "black"


class TestLawnGrass:
    """Тесты для класса LawnGrass"""

    def test_lawn_grass_creation(self):
        """Тест создания газонной травы"""
        grass = LawnGrass("Трава", "Газонная", 500.0, 100, "Россия", "2 недели", "зеленый")
        assert grass.name == "Трава"
        assert grass.price == 500.0
        assert grass.country == "Россия"
        assert grass.germination_period == "2 недели"
        assert grass.color == "зеленый"


class TestCategory:
    """Тесты для класса Category"""

    @pytest.fixture
    def sample_products(self):
        """Фикстура с тестовыми продуктами"""
        return [
            Product("Товар1", "Описание1", 100.0, 5),
            Product("Товар2", "Описание2", 200.0, 3),
            Product("Товар3", "Описание3", 300.0, 2)
        ]

    def test_category_creation(self, sample_products):
        """Тест создания категории"""
        category = Category("Категория", "Описание", sample_products)
        assert category.name == "Категория"
        assert len(category._Category__products) == 3

    def test_empty_category(self):
        """Тест создания пустой категории"""
        category = Category("Пустая", "Категория", [])
        assert len(category._Category__products) == 0

    def test_middle_price(self, sample_products):
        """Тест расчета средней цены"""
        category = Category("Категория", "Описание", sample_products)
        assert category.middle_price() == (100.0 + 200.0 + 300.0) / 3

    def test_middle_price_empty(self):
        """Тест расчета средней цены для пустой категории"""
        category = Category("Пустая", "Категория", [])
        assert category.middle_price() == 0.0

    def test_add_product(self):
        """Тест добавления продукта в категорию"""
        category = Category("Категория", "Описание", [])
        product = Product("Товар", "Описание", 100.0, 5)
        category.add_product(product)
        assert len(category._Category__products) == 1

    def test_add_invalid_product(self):
        """Тест добавления невалидного продукта"""
        category = Category("Категория", "Описание", [])
        with pytest.raises(TypeError, match="Можно добавить только объект класса Product или его наследника"):
            category.add_product("Не продукт")

    def test_str_method(self, sample_products):
        """Тест строкового представления категории"""
        category = Category("Категория", "Описание", sample_products)
        assert str(category) == "Категория, количество продуктов: 10 шт."

    def test_products_property(self, sample_products):
        """Тест свойства products"""
        category = Category("Категория", "Описание", sample_products)
        products_str = category.products
        assert "Товар1, 100.0 руб. Остаток: 5 шт." in products_str
        assert "Товар2, 200.0 руб. Остаток: 3 шт." in products_str
        assert "Товар3, 300.0 руб. Остаток: 2 шт." in products_str
