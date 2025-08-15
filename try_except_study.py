# # исключение по несуществующей переменной
# try:
#     print(a)
# except NameError:
#     print("Ошибка: переменная a не определена")
# # исключение по делению на ноль
# try:
#     1 / 0
# except ZeroDivisionError:
#     print("Ошибка: деление на ноль")
# # исключение по неверному типу данных
# try:
#     open("some_file")
# except FileNotFoundError:
#     print("Ошибка: файл не найден")


# try: # пример
#     a, b = input("Введите числа: ").split()
#     a, b = int(a), int(b)
#     result = a / b
# except ValueError as e: # правильный тип данных
#     print(e)
# except ZeroDivisionError as e:
#     print(e) # деление на ноль
# else:
#     print(result) # если нет исключений
# finally:
#     print("Выполнение завершено") # выполняется в любом случае финал

# class MyClass:
#     def func1(self):
#         try:
#            1 / 0
#         except ZeroDivisionError as e:
#             print(e)
#         print("Работает метод func1")
#
#     def func2(self):
#         self.func1()
#         try:
#             print(a)
#         except NameError:
#             print("Нет такой переменной")
#         print("Работает метод func2")
#
#     def func3(self):
#         self.func2()
#         print("Работает метод func3")
#
# if __name__ == "__main__":
#     my_object = MyClass()
#     my_object.func3()


class ShellException(Exception): # Базовый класс для исключений
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Ошибка обработки скрипта"

    def __str__(self):
        return self.message


class ShellEmptyException(ShellException):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Скрипт пустой"

class ShellShebangException(ShellException):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Отсутствует шебанг"


class ShellScript: # интерфейс, который передаем пользователю
    def __init__(self, content):
        if not content:
            raise ShellEmptyException()
        elif content[0:2] != "#!":
            raise ShellShebangException()
        self.eval()

    def eval(self):
        pass


if __name__ == "__main__":
    # bash_content = ""
    bash_content = "!/bin/bash"
    try:
        shell_script = ShellScript(bash_content)
    except ShellEmptyException as e:
        print(e)
        print("Передайте не пустой файл скрипта")
    except ShellShebangException as e:
        print(e)
        print("Валидация на шебанг не пройдена")
