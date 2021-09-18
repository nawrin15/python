import sys


my_tuple6 = (0, 1, 2, "hello", True)
my_list = [0, 1, 2, "hello", True]

print(sys.getsizeof(my_tuple6), "bytes --> tuple") #88 bytes = tuple
print(sys.getsizeof(my_list), "bytes --> list") #104 bytes = list

import timeit

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5, 6]", number=1000000)) #0.18645660000038333
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5, 6)", number=1000000)) #0.023996497999178246
