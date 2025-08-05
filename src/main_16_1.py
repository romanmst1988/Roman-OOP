from typing import List


class Product:

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Метод возвращает строку содержимого продуктов в заданном формате"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод сложения который позволяет складывать
        товары только из одинаковых классов продуктов"""
        if isinstance(other, self.__class__):
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

        # доп.задание при понижении цены (проверка цены)
        try:
            current_price = self.__price
            if new_price < current_price:
                confirmation = input(
                    f"Цена понижается с {current_price} до {new_price}."
                    f"Если хотите понизить цену введите 'y', либо вернуть текущую цену 'n': "
                )
                if confirmation.lower() != "y":
                    print("Изменение цены отменено")
                    return
        except AttributeError:
            pass

        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, existing_products: list):
        """
        Создает новый товар с проверкой на дубликаты
        Параметры:
        - product_data: словарь с данными товара
        - existing_products: список существующих товаров для проверки
        Возвращает: объект Product
        """
        if existing_products is None:
            existing_products = []

        name = product_data["name"]
        description = product_data["description"]
        price = float(product_data["price"])
        quantity = int(product_data["quantity"])

        for existing_product in existing_products:
            if existing_product.name.lower() == name.lower():
                existing_product.quantity = quantity  # Объединяем количество
                existing_product.price = max(existing_product.price, price)  # Берём максимальную цену продукта
                print(f"Товар {name} уже существует. Объединено количество и выбрана наибольшая цена")
                return existing_product

        return cls(name, description, price, quantity)  # Если дубликатов нет - создаем новый товар


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
        self.__products_count = len(products)  # Счетчик товаров конкретной категории

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        """Метод возвращает строку содержимого категории в заданном формате"""
        summ_products = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {summ_products} шт."

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{self.name}, {product.price} руб. Остаток: {self.product_count} шт.\n"
        return products_str

    def add_product(self, product: Product) -> None:
        """метод, который добавляет продукт в категорию,
        таким образом, чтобы не было возможности добавить
        вместо продукта или его наследников любой другой объект
        """
        if not isinstance(product, Product):  # ДОБАВЛЕНО: проверка на тип
            raise TypeError("Можно добавить только объект класса Product или его наследника")

        self.__products.append(product)
        Category.product_count += 1


class Smartphone(Product):
    """Новый класс наследник класса Product"""
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

class LawnGrass(Product):
    """Новый класс наследник класса Product"""
    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

if __name__ == '__main__':
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)

    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)

    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)

    print(category_smartphones.products)

    print(Category.product_count)

    try:
        category_smartphones.add_product("Not a product")
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")
