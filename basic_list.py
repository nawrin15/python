
# List : ordered, mutable, allow duplicate elements
num_arr = [9, 8, 6, -5, 4, 3]
str_arr = ["apple, banana", "pine-apple", "lechy", "orange"]








k = [0] * 5 # [0, 0, 0, 0, 0]
print(k)


a = [0] * 5
b = [5, 6, 2, 7, 6]

print(a+b) #[0, 0, 0, 0, 0, 5, 6, 2, 7, 6]

print(b[1:4]) #[6, 2, 7]

print(b[::2]) #[5, 2, 6]

print(b[::-1]) #[6, 7, 2, 6, 5]


str_list = ["apple, banana", "pine-apple", "lechy", "orange"]


str2_list = str_list

str3_list = str_list.copy() # way-1
str4_list = list(str_list) # way-2
str5_list = str_list[:] # way-3

str_list.append("mongo")

print(str2_list) #['apple, banana', 'pine-apple', 'lechy', 'orange', 'mongo']
print(str3_list) #['apple, banana', 'pine-apple', 'lechy', 'orange']
print(str4_list) #['apple, banana', 'pine-apple', 'lechy', 'orange']
print(str5_list) #['apple, banana', 'pine-apple', 'lechy', 'orange']


c = [i*i for i in b]
print(c) #[25, 36, 4, 49, 36]
