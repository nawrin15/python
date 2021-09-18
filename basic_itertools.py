#itertools: product, permutations, combinations, accumulate, groupby and infinite iterators
from itertools import product

a = [1, 2]
b = [3, 4]
c = [5]
d = [5, 6, 9]
e = [1, 2, 3, 4]
f = [1, 2, 5, 8, 7, 6, 4]
prod = product(a, b)
print(prod)
print(list(prod))

prod1 = product(a, c, repeat=2)
print(list(prod1))


from itertools import permutations

perm =  permutations(d)
print(list(perm))

perm1 =  permutations(d, 2)
print(list(perm1))

from itertools import combinations, combinations_with_replacement

comb = combinations(d, 2)
comb1 = combinations(e, 2)
comb2 = combinations_with_replacement(e, 2)
print(list(comb))
print(list(comb1))
print(list(comb2))


from itertools import accumulate
import operator

acc = accumulate(e)
print(list(acc))

acc1 = accumulate(e, func=operator.mul)
print(list(acc1))

acc2 = accumulate(f, func=max)
print(list(acc2))

from itertools import groupby

def smaller_than_3(x):
    return x < 3


group_obj = groupby(e, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

group_obj1 = groupby(e, key=lambda x: x<3)
for key, value in group_obj1:
    print(key, list(value))


persons = [
    {'name': 'Tim', 'age': 25},
    {'name': 'Dim', 'age': 27},
    {'name': 'Dan', 'age': 25},
    {'name': 'Lisa', 'age': 28}
]

group_obj2 = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj2:
    print(key, list(value))

from itertools import count, cycle, repeat # runs until break

for i in count(10):
    print(i)
    if i == 15:
        break

ct = 0
for i in cycle(e):
    ct += 1
    print(i)
    if ct > 10:
        break

ct = 0
for i in repeat(1):
    ct += 1
    print(i)
    if ct > 10:
        break

for i in repeat(5, 3):
    print(i)
