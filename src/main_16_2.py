from abc import ABC, abstractmethod
from typing import List


class ReprMixin:
    """Миксин для вывода информации о создании объекта"""
    def __init__(self, *args, **kwargs):
        print(f"Создан объект {self.__class__.__name__} с параметрами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        super().__init__(*args, **kwargs)

    def __repr__(self):
        attrs = ', '.join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"{self.__class__.__name__}({attrs})"


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов"""
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict, existing_products: list):
        pass


class Product(BaseProduct, ReprMixin):
    """Класс продукта, наследующий от BaseProduct и ReprMixin"""
    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name=name, description=description, price=price, quantity=quantity)
        self.__price = price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) == type(other):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        raise TypeError("Нельзя складывать объекты разных классов")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        try:
            current_price = self.__price
            if new_price < current_price:
                confirmation = input(
                    f"Цена понижается с {current_price} до {new_price}."
                    f"Если хотите понизить цену введите 'y', либо вернуть текущую цену 'n': "
                )
                if confirmation.lower() != 'y':
                    print("Изменение цены отменено")
                    return
        except AttributeError:
            pass

        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, existing_products: list):
        name = product_data["name"]
        description = product_data["description"]
        price = float(product_data["price"])
        quantity = int(product_data["quantity"])

        for existing_product in existing_products:
            if existing_product.name.lower() == name.lower():
                existing_product.quantity += quantity
                existing_product.price = max(existing_product.price, price)
                print(f"Товар {name} уже существует. Объединено количество и выбрана наибольшая цена")
                return existing_product

        return cls(name, description, price, quantity)


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    name: str
    description: str
    products: List[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products) -> None:
        self.name = name
        self.description = description
        self.__products = products if products else []
        self.__products_count = len(products)

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        summ_products = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {summ_products} шт."

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только объект класса Product или его наследника")
        self.__products.append(product)
        Category.product_count += 1

if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)