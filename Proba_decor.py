import random

def my_decorator(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        result_int = int(result)
        return result_int

    return inner
@my_decorator
def get_rand_numbers():
    return random.randint(1, 100) / random.randint(1, 100)

print(get_rand_numbers())


# def printing(func):
#     def inner(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"Func {func} called with result: {result}")
#         return result
#
#     return inner
# @printing #использую декоратор для add_one без использования new_f
# def add_one(x):
#     return x + 1
#
# # new_f = printing(add_one)
# # y = new_f(20)
# """Использую декоратор"""
#
# y = add_one(10) #не использую декоратор
#
# print(y)


