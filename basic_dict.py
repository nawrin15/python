#Dictionary: key-value pairs, unordered, mutable

myDict = {"name": "Max", "age": 42, "city": "New York"}
myDict2 = dict(name="Mary", age="41", city="Boston")

print(myDict) #{'name': 'Max', 'city': 'New York', 'age': 42}
print(myDict2) #{'city': 'Boston', 'name': 'Mary', 'age': '41'}

print(myDict["name"]) #Max


myDict["email"] = "cool@xyz,com"
print(myDict) #{'age': 42, 'name': 'Max', 'email': 'cool@xyz,com', 'city': 'New York'}


##delete item

#way-1

del myDict["email"]
print(myDict) #{'age': 42, 'name': 'Max', 'city': 'New York'}


#way-2

myDict.pop("name")
print(myDict) #{'age': 42, 'city': 'New York'}


#way-3(pop last item)
myDict.popitem()
print(myDict) #{'city': 'New York'}



##check elemnt

if "city" in myDict:
    print(myDict) #{'city': 'New York'}


for key in myDict2:
    print(key)


for key in myDict2.keys():
    print(key)

for value in myDict2.values():
    print(value)

for key, value in myDict2.items():
    print(key, value)


myDict2_cpy = myDict2

print(myDict2_cpy) #{'age': '41', 'city': 'Boston', 'name': 'Mary'}

myDict2_cpy['email'] = "cool@www.com"

print(myDict2_cpy) #{'age': '41', 'email': 'cool@www.com', 'city': 'Boston', 'name': 'Mary'}
print(myDict2) #{'age': '41', 'email': 'cool@www.com', 'city': 'Boston', 'name': 'Mary'}

##copy dict

#way-1

myDict2_cpy1 = myDict2.copy()
myDict2_cpy1['fav_color'] = "blue"

print(myDict2_cpy1) #{'age': '41', 'fav_color': 'blue', 'email': 'cool@www.com', 'city': 'Boston', 'name': 'Mary'}
print(myDict2) #{'age': '41', 'email': 'cool@www.com', 'city': 'Boston', 'name': 'Mary'}


#way-2

myDict2_cpy2 = dict(myDict2)
myDict2_cpy2['fav_color'] = "green"

print(myDict2_cpy2) #{'age': '41', 'fav_color': 'green', 'email': 'cool@www.com', 'city': 'Boston', 'name': 'Mary'}
print(myDict2) #{'age': '41', 'email': 'cool@www.com', 'city': 'Boston', 'name': 'Mary'}


myDict2.update(myDict2_cpy2)
print(myDict2) #{'age': '41', 'email': 'cool@www.com', 'fav_color': 'green', 'city': 'Boston', 'name': 'Mary'}

mytuple = (8, 9)
myDict3 = {mytuple: "tuple"}
print(myDict3)
    
