class EverRange:

    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        self.current_value = -2
        return self

    def __next__(self):
        if self.current_value + 2 < self.stop:
            self.current_value += 2
            return self.current_value
        else:
            raise StopIteration

for i in EverRange(22): # next(iter_r)
    print(i) # [0, 2, 4, 6]




# class MoeRange:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#
#     def __iter__(self):
#         return self  # MoeRange — это итератор, потому что у него есть __next__
#
#     def __next__(self):  # <- Должен быть внутри класса!
#         if self.start < self.stop:
#             value = self.start
#             self.start += 1
#             return value
#         else:
#             raise StopIteration
# for i in MoeRange(0, 10):
#     print(i)