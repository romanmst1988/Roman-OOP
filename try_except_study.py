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


try: # пример
    a, b = input("Введите числа: ").split()
    a, b = int(a), int(b)
    result = a / b
except ValueError as e: # правильный тип данных
    print(e)
except ZeroDivisionError as e:
    print(e) # деление на ноль
else:
    print(result) # если нет исключений
finally:
    print("Выполнение завершено") # выполняется в любом случае финал



