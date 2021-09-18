#Sets: unordered, mutable, no duplicates

my_dict = {} #type dict
my_set = set() # type setA

my_set = {1, 3, 3}
print(my_set) # {1,3}

list_to_set = set([1, 2, 6, 6])
print(list_to_set) # {1, 2, 6}

str_to_set = set('Hello')
print(str_to_set) # {'e', 'l', 'o', 'H'}


my_set1 = set()

my_set1.add(1)
my_set1.add(8)
my_set1.add(4)
my_set1.add(7)
my_set1.add(45)
my_set1.add(65)


my_set1.remove(4)
# my_set1.remove(5) will have error keyerror if element is not found in set
print(my_set1) #{1, 65, 7, 8, 45}

my_set1.discard(7)
my_set1.discard(9) #will not have any error if element is not found
print(my_set1) #{1, 65, 8, 45}

print(my_set1.pop()) #1
print(my_set1) #{65, 8, 45}


for i in my_set1:
    print(i)

if 8 in my_set1:
    print('present')

my_set1.clear() #clear the set
print(my_set1) #set()


odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}


u = odds.union(evens)

print(u) #{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

i = evens.intersection(primes)
print(i) # {2}

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff) #{4, 5, 6, 7, 8, 9}

diff = setA.symmetric_difference(setB)
print(diff) #{4, 5, 6, 7, 8, 9, 10, 11, 12}


setA.update(setB)
print(setA) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}


setA1= {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB1 = {1, 2, 3, 10, 11, 12}

setA1.intersection_update(setB1)
print(setA1) #{1, 2, 3}

setA2= {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB2 = {1, 2, 3, 10, 11, 12}

setA2.difference_update(setB2)
print(setA2) #{4, 5, 6, 7, 8, 9}

setA3= {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB3 = {1, 2, 3, 10, 11, 12}

setA3.symmetric_difference_update(setB3)
print(setA3) #{4, 5, 6, 7, 8, 9, 10, 11, 12}

setA4= {1, 2, 3, 4, 5, 6}
setB4 = {1, 2, 3}
setC4 = {7, 8}

print(setB4.issubset(setA4)) #True
print(setA4.issubset(setB4)) #False


print(setB4.issuperset(setA4)) #False
print(setA4.issuperset(setB4)) #True


print(setA4.isdisjoint(setB4)) #False
print(setA4.isdisjoint(setC4)) #True

setA5 = {1, 2, 3, 4, 5, 6}

setB5 = setA5
setC5 = setA5.copy()
setD5 = set(setA5)

setB5.add(7)
setC5.add(9)
setD5.add(45)

print(setA5) #{1, 2, 3, 4, 5, 6, 7}

setE = frozenset([1,2, 3, 4]) #can't change elementafter init. add, remove, update not work. intersection, union, difference will work

print(setE)
