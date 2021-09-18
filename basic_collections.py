#collections - special datatypes
#collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter

a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter)#Counter({'a': 5, 'b': 4, 'c': 3})
print(my_counter.items())#dict_items([('c', 3), ('b', 4), ('a', 5)])
print(my_counter.keys())#dict_keys(['c', 'b', 'a'])
print(my_counter.values())#dict_values([3, 4, 5])
print(my_counter.most_common(1)) #[('a', 5)]
print(my_counter.most_common(2)) #[('a', 5), ('b', 4)]
print(my_counter.most_common(1)[0]) #('a', 5)
print(my_counter.most_common(1)[0][0]) #a
print(my_counter.elements()) #<itertools.chain object at 0x7fb18c5c7c50>
print(list(my_counter.elements())) #['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c']


from collections import namedtuple

Point = namedtuple('Point', 'x,y')

pt = Point(1, -4)

print(pt) #Point(x=1, y=-4)
print(pt.x, pt.y) #1 -4


from collections import OrderedDict

##python-3.7 dict is already ordered, so this no longer needed

ordered_dict = OrderedDict()
ordered_dict['b'] = 1
ordered_dict['c'] = 2
ordered_dict['d'] = 3
ordered_dict['a'] = 4

print(ordered_dict) #OrderedDict([('b', 1), ('c', 1), ('d', 1), ('a', 1)])

unordered_dict = {}
unordered_dict['b'] = 1
unordered_dict['c'] = 2
unordered_dict['d'] = 3
unordered_dict['a'] = 4
print(unordered_dict)

from collections import defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['b']) #2
print(d['c']) #0 retrun zero, not having any key error

e = defaultdict(float)

print(e['a']) #0.0

f = defaultdict(list)

print(f['a']) #[]


from collections import deque # double enned queue


g = deque()

g.append(2)
g.append(5)

g.appendleft(3)
print(g) #deque([3, 2, 5])
g.pop()
print(g) #deque([3, 2])

g.extend([8, 9, 10])
print(g) #deque([3, 2, 8, 9, 10])

g.popleft()
print(g) #deque([2, 8, 9, 10])

g.extendleft([11, 19])
print(g) #deque([19, 11, 2, 8, 9, 10])

g.rotate(1)
print(g) #deque([10, 19, 11, 2, 8, 9])
g.rotate(2)
print(g) #deque([8, 9, 10, 19, 11, 2])
g.rotate(-1)
print(g) #deque([9, 10, 19, 11, 2, 8])

g.clear()
print(g) #deque([])
