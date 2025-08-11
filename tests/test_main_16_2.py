import pytest

from main_16_2 import BaseProduct, Category, LawnGrass, Product, Smartphone


class TestProduct:
    def test_product_creation(self):
        """Тест создания продукта"""
        product = Product("Test", "Test desc", 100.0, 10)
        assert product.name == "Test"
        assert product.description == "Test desc"
        assert product.price == 100.0
        assert product.quantity == 10

    def test_product_str(self):
        """Тест строкового представления продукта"""
        product = Product("Test", "Test desc", 100.0, 10)
        assert str(product) == "Test, 100.0 руб. Остаток: 10 шт."

    # def test_product_repr(self):
    #     """Тест repr продукта"""
    #     product = Product("Test", "Test desc", 100.0, 10)
    #     assert repr(product) == "Product(_Product__price=100.0, name='Test', description='Test desc', quantity=10)"

    def test_price_setter_negative(self, capsys):
        """Тест установки отрицательной цены"""
        product = Product("Test", "Test desc", 100.0, 10)
        product.price = -50
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 100.0

    def test_price_setter_decrease_confirmation(self, monkeypatch):
        """Тест подтверждения понижения цены"""
        product = Product("Test", "Test desc", 100.0, 10)

        # Симулируем ввод 'n' (не подтверждаем понижение цены)
        monkeypatch.setattr("builtins.input", lambda _: "n")
        product.price = 80.0
        assert product.price == 100.0

        # Симулируем ввод 'y' (подтверждаем понижение цены)
        monkeypatch.setattr("builtins.input", lambda _: "y")
        product.price = 80.0
        assert product.price == 80.0

    def test_add_products(self):
        """Тест сложения продуктов"""
        product1 = Product("Test1", "Desc1", 100.0, 5)
        product2 = Product("Test2", "Desc2", 200.0, 3)
        assert product1 + product2 == 100.0 * 5 + 200.0 * 3

    def test_add_different_classes(self):
        """Тест сложения разных классов"""
        product = Product("Test", "Desc", 100.0, 5)
        other = Smartphone("Smart", "Desc", 200.0, 3, "High", "X", "128GB", "Black")
        with pytest.raises(TypeError, match="Нельзя складывать объекты разных классов"):
            product + other

    def test_new_product_creation(self):
        """Тест создания нового продукта через классовый метод"""
        product_data = {"name": "New Product", "description": "New Desc", "price": "150.0", "quantity": "7"}
        product = Product.new_product(product_data, [])
        assert isinstance(product, Product)
        assert product.name == "New Product"
        assert product.price == 150.0
        assert product.quantity == 7

    def test_new_product_existing(self, capsys):
        """Тест создания нового продукта, когда такой уже существует"""
        existing_product = Product("Existing", "Desc", 100.0, 5)
        product_data = {"name": "Existing", "description": "New Desc", "price": "120.0", "quantity": "3"}
        result = Product.new_product(product_data, [existing_product])
        captured = capsys.readouterr()
        assert "Товар Existing уже существует" in captured.out
        assert result == existing_product
        assert existing_product.quantity == 8
        assert existing_product.price == 120.0


class TestSmartphone:
    def test_smartphone_creation(self):
        """Тест создания смартфона"""
        smartphone = Smartphone("Galaxy", "Desc", 1000.0, 10, "High", "S23", "256GB", "Black")
        assert smartphone.name == "Galaxy"
        assert smartphone.price == 1000.0
        assert smartphone.quantity == 10
        assert smartphone.efficiency == "High"
        assert smartphone.model == "S23"
        assert smartphone.memory == "256GB"
        assert smartphone.color == "Black"


class TestLawnGrass:
    def test_lawn_grass_creation(self):
        """Тест создания газонной травы"""
        grass = LawnGrass("Premium", "Desc", 50.0, 100, "Russia", "14 days", "Green")
        assert grass.name == "Premium"
        assert grass.price == 50.0
        assert grass.quantity == 100
        assert grass.country == "Russia"
        assert grass.germination_period == "14 days"
        assert grass.color == "Green"


class TestCategory:
    def test_category_creation(self):
        """Тест создания категории"""
        product = Product("Test", "Desc", 100.0, 5)
        category = Category("Test Category", "Test Desc", [product])
        assert category.name == "Test Category"
        assert category.description == "Test Desc"
        assert len(category._Category__products) == 1
        assert category._Category__products_count == 1

    def test_category_str(self):
        """Тест строкового представления категории"""
        product1 = Product("Test1", "Desc1", 100.0, 5)
        product2 = Product("Test2", "Desc2", 200.0, 3)
        category = Category("Test", "Desc", [product1, product2])
        assert str(category) == "Test, количество продуктов: 8 шт."

    def test_products_property(self):
        """Тест свойства products"""
        product1 = Product("Test1", "Desc1", 100.0, 5)
        product2 = Product("Test2", "Desc2", 200.0, 3)
        category = Category("Test", "Desc", [product1, product2])
        expected_output = "Test1, 100.0 руб. Остаток: 5 шт.\n" "Test2, 200.0 руб. Остаток: 3 шт.\n"
        assert category.products == expected_output

    def test_add_product(self):
        """Тест добавления продукта в категорию"""
        product = Product("Test", "Desc", 100.0, 5)
        category = Category("Test", "Desc", [])
        category.add_product(product)
        assert len(category._Category__products) == 1
        assert category._Category__products[0] == product

    def test_add_non_product(self):
        """Тест добавления не-продукта в категорию"""
        category = Category("Test", "Desc", [])
        with pytest.raises(TypeError, match="Можно добавить только объект класса Product или его наследника"):
            category.add_product("Not a product")

    def test_category_counters(self):
        """Тест счетчиков категорий и продуктов"""
        # Сбросим счетчики для чистого теста
        Category.category_count = 0
        Category.product_count = 0

        product1 = Product("Test1", "Desc1", 100.0, 5)
        product2 = Product("Test2", "Desc2", 200.0, 3)
        category1 = Category("Cat1", "Desc", [product1, product2])
        category2 = Category("Cat2", "Desc", [])

        assert Category.category_count == 2
        assert Category.product_count == 2


class TestBaseProduct:
    def test_abstract_methods(self):
        """Тест, что BaseProduct действительно абстрактный"""
        with pytest.raises(TypeError):
            BaseProduct("Test", "Desc", 100.0, 5)
