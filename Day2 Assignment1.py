# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 22:46:02 2020

@author: hp 3006tx
"""
#list
lst=[1,2,3,4,5,6,7,8,9]
print(lst)

print(len(lst))
print(max(lst))
print(min(lst))

s='Aditya'
lst1 = list(s)
print(lst1)

#dictionary
dic={'name':'aditya','age':18,'job':'student'}

print(dic['name'])
print(dic.copy())
print(dic.keys())
print(dic.items())
dic.pop('job')
print(dic)
dic['age'] = 27
print(dic)
print(sorted(dic))
print(len(dic))
print(any(dic))
dic.clear()
print(dic)

# tuple
tuple = ()
print(tuple)


tuple = (1, 2, 3)
print(tuple)


tuple = (1, "Hello", 3.4)
print(tuple)

tuple = ("mouse", [8, 4, 6], (1, 2, 3),'p','l','a','y')
print(tuple)


print(tuple[0])
print(tuple[1][2])
print(tuple[-1])
print(tuple[1:2])
print(tuple.count('p'))
print(tuple.index('l'))



#sets
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

my_set = {1, 3, 4, 5, 6}
print(my_set)

my_set.discard(4)
print(my_set)
my_set.remove(6)
print(my_set)

my_set.discard(2)
print(my_set)


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)
print(A & B)
print(A - B)
print(A ^ B)



#strings

my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

str1 = 'Hello'
str2 ='World!'

print(str1 + str2)

print( str1 * 3)

print('n' in 'aditya')
print(len(my_string))