import pytest

from main_15_1 import Category, Product


def test_product_initialization():
    """Тест инициализации продукта"""
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_str():
    """Тест строкового представления продукта"""
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert str(product) == "Test Product, 100.0 руб. Остаток: 10 шт."


def test_product_add():
    """Тест сложения продуктов (по стоимости всех единиц)"""
    product1 = Product("Product 1", "Desc 1", 100.0, 5)
    product2 = Product("Product 2", "Desc 2", 200.0, 3)
    assert product1 + product2 == (100.0 * 5) + (200.0 * 3)


def test_product_price_setter_negative():
    """Тест установки отрицательной цены"""
    product = Product("Test Product", "Test Description", 100.0, 10)
    product.price = -50.0  # Попытка установить отрицательную цену
    assert product.price == 100.0  # Цена не должна измениться


def test_product_price_setter_decrease_with_confirmation(monkeypatch):
    """Тест понижения цены с подтверждением"""
    product = Product("Test Product", "Test Description", 100.0, 10)

    # Симулируем ввод 'y' (подтверждение понижения цены)
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 80.0
    assert product.price == 80.0

    # Симулируем ввод 'n' (отмена понижения цены)
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 70.0
    assert product.price == 80.0  # Цена осталась прежней


def test_new_product_creation():
    """Тест создания нового продукта через классовый метод"""
    product_data = {"name": "New Product", "description": "New Description", "price": "150.0", "quantity": "20"}
    product = Product.new_product(product_data, [])
    assert product.name == "New Product"
    assert product.price == 150.0
    assert product.quantity == 20


def test_new_product_duplicate_merge():
    """Тест объединения дубликатов при создании продукта"""
    existing_product = Product("Existing Product", "Old Description", 100.0, 5)
    product_data = {
        "name": "Existing Product",  # То же имя, что и у existing_product
        "description": "New Description",
        "price": "120.0",
        "quantity": "10",
    }
    updated_product = Product.new_product(product_data, [existing_product])
    assert updated_product.quantity == 10  # Количество обновилось
    assert updated_product.price == 120.0  # Цена обновилась (выбрана максимальная)


def test_category_initialization():
    """Тест инициализации категории"""
    product = Product("Test Product", "Test Description", 100.0, 10)
    category = Category("Test Category", "Test Description", [product])
    assert category.name == "Test Category"
    assert len(category._Category__products) == 1
    assert Category.category_count > 0
    assert Category.product_count > 0


def test_category_str():
    """Тест строкового представления категории"""
    product = Product("Test Product", "Test Description", 100.0, 10)
    category = Category("Test Category", "Test Description", [product])
    assert str(category) == "Test Category, количество продуктов: 10 шт."


def test_category_add_product():
    """Тест добавления продукта в категорию"""
    category = Category("Test Category", "Test Description", [])
    product = Product("Test Product", "Test Description", 100.0, 10)
    category.add_product(product)
    assert len(category._Category__products) == 1


def test_category_add_invalid_product():
    """Тест попытки добавить неверный тип в категорию"""
    category = Category("Test Category", "Test Description", [])
    with pytest.raises(TypeError, match="Можно добавить только объект класса Product или его наследника"):
        category.add_product("Not a product")  # Передаем строку вместо Product


if __name__ == "__main__":
    pytest.main()
