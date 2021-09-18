# Strings: ordered, immutable, text representation
my_string1 = 'Hello \'world'
my_string2 = "Hello 'world"
my_string3 = """Hello
world"""
my_string4 = """Hello \
world"""
print(my_string1)
print(my_string2)
print(my_string3)
print(my_string4)
print(my_string4[2]) #l
print(my_string4[-3]) #r

substring1 = my_string4[1:5]
substring2 = my_string4[1:]
substring3 = my_string4[:5]
substring4 = my_string4[::2] #every second char
substring5 = my_string4[:] #every char
substring6 = my_string4[::-1] #reverse string


print(substring1) #ello
print(substring2) #ello world
print(substring3) #Hello
print(substring4) #Hlowrd
print(substring5) #Hello world
print(substring6) #dlrow olleH

greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence) #Hello Tom

for i in greeting:
    print(i)

if "el" in greeting:
    print("yes") # yes

my_string5 = "    Geeet   "
print(my_string5.strip()) #Geeet

my_string6="sadia"
print(my_string6.upper())#SADIA

my_string7="SADIA"
print(my_string7.lower())#sadia

print(my_string7.startswith('a')) #False
print(my_string7.startswith('SA')) #True

print(my_string7.endswith('A')) #True

print(my_string7.find('A')) #1 (first index that match)
print(my_string7.find('IA')) #3

print(my_string7.count('A')) #2
print(my_string7.count('AD')) #1

print(my_string7.replace('AD', "BA")) #SBAIA
print(my_string7.replace('ADD', "BA")) #SADIA

my_string8 = "how are you doing?"

my_list = my_string8.split() # by default arg takes space
print(my_list) #['how', 'are', 'you', 'doing?']

my_string9 = "how,are,you,doing?"

my_list2 = my_string9.split(',')
print(my_list2) #['how', 'are', 'you', 'doing?']

print(''.join(my_list2)) #howareyoudoing?
print(', '.join(my_list2)) #how, are, you, doing?
print(' '.join(my_list2)) #how are you doing?


from timeit import default_timer as timer

my_list3 = ['a'] * 10000

#bad
start = timer()
my_string10=''
for i in my_list3:
    my_string10 += i
stop = timer()
print(stop-start) #0.002468341000167129


#good
start = timer()
my_string10 = ''.join(my_list3)
stop = timer()
print(stop-start)#0.00021985499961374444

#formatting string - %, format(), f-Strings
##way-%
name = "Tom"
count = 3
decimal_num = 3.141618

print("this is %s" % name)
print("this is %d" % count)
print("this is %d" % decimal_num)
print("this is %f" % decimal_num)
print("this is %.2f" % decimal_num)


# this is Tom
# this is 3
# this is 3
# this is 3.140000
# this is 3.14


##way-format()
print("this is {}".format(decimal_num))
print("this is {:.2f} and {}".format(decimal_num, count))

# this is 3.141618
# this is 3.14 and 3

##way-f-Strings
print(f"this is {decimal_num} and {count * 2}") # <python-3.6

#this is 3.141618 and 6
