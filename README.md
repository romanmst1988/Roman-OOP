# Каталог товаров

Проект представляет собой систему управления категориями и товарами с возможностью загрузки данных из JSON-файла.

## Функциональность

- Создание категорий товаров
- Управление товарами внутри категорий
- Автоматический подсчет количества категорий и товаров
- Загрузка данных из JSON-файла
- Валидация входных данных

## Классы

### `Product`

Класс для представления товара:

```python
class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
```

### `Category`
Класс для представления категории товаров:

```python
class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
```

## Функции
load_data_from_json(file_path: str) -> List[Category]
Загружает данные из JSON-файла и создает объекты категорий и товаров.

# Параметры:

file_path - путь к JSON-файлу

# Возвращает:

Список объектов Category

# Формат JSON-файла:

```json
[
    {
        "name": "Название категории",
        "description": "Описание категории",
        "products": [
            {
                "name": "Товар 1",
                "description": "Описание товара",
                "price": "100.0",
                "quantity": "5"
            }
        ]
    }
]
```

## Пример использования
python
# Загрузка данных из файла
categories = load_data_from_json('products.json')

# Вывод информации
for category in categories:
    print(category)
    for product in category.products:
        print(f"  {product}")

print(f"\nВсего категорий: {Category.category_count}")
print(f"Всего товаров: {Product.product_count}")

## Требования
Python 3.7+

Нет внешних зависимостей

## Установка
Клонировать репозиторий

Скачать файл products.json с данными по этой ссылке: https://drive.google.com/file/d/1fTgJX1_-rI2JbuM2He6OPyU_N5PyePsd/view

## Запустить скрипт:

bash
python main.py
## Тестирование
Для запуска тестов:

bash
pytest tests.py -v
