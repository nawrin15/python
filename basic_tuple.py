my_tuple = ('pink', 'blue', 'green', 'pink')
my_tuple2 = 'yellow', 'white', 'black'
my_str = ('pink')
my_tuple3 = ('pink',)
my_tuple4 = 'pink',
my_tuple5 = tuple(['red', 'blue', 'red', 'green'])

print(my_tuple) #('pink', 'blue', 'green', 'pink')
print(my_tuple2) #('yellow', 'white', 'black')
print(type(my_str)) #<class 'str'>
print(type(my_tuple3)) #<class 'tuple'>
print(type(my_tuple4)) #<class 'tuple'>
print(type(my_tuple5)) #<class 'tuple'>
print(my_tuple5) #('red', 'blue', 'red', 'green')

print(my_tuple5[-1], my_tuple5[2]) #green red

for item in my_tuple5:
    print(item)


if 'green' in my_tuple5:
    print("yes")
else:
    print("no")

print(len(my_tuple5)) #4
print(my_tuple5.count('red'))  #2
print(my_tuple5.index('red'))  #0
try:
    print(my_tuple5.index('violet'))
except ValueError:
    print("value error happend")

print(list(my_tuple5)) #['red', 'blue', 'red', 'green']




a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
c = a[2:]
d = a[:5]
e = a[::2] # skip 1 element
f = a[::-1] # reversed tuple

print(b) #(3, 4, 5)
print(c) #(3, 4, 5, 6, 7, 8, 9, 10)
print(d) #(1, 2, 3, 4, 5)
print(e) #(1, 3, 5, 7, 9)
print(f) #(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

info = "foo", 45, 'rome'
name, age, city = info
print(info) #('foo', 45, 'rome')
print(name, age, city) #foo 45 rome

i1, *i2, i3, i4 = a
print(i1) #1
print(i2) #[2, 3, 4, 5, 6, 7, 8]
print(i3) #9
print(i4) #10
