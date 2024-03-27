#Write a program that takes two integers as input, base and exponent, and calculates the power using loops.
print('====================================== part 1  "Base and exponent"')
base = 5 # int(input('Enter the base value: '))
exp = 3 # int(input('Enter the exponent value: '))
result = 1
for i in range(exp):
    result = result * base
print(result)


#Write a program that calculates the sum of all elements in a given tuple.
tup = (1,2,3,4,5,6)
result = 0
print('\n====================================== part 2  "Tuple sum"')
print(tup)
for item in tup:
    result = result + item
print(result)

#Write a program that creates a new tuple containing only the even numbers from a given tuple of integers.
print('\n====================================== part 3  "Even tuple"')
tup = (1,2,3,4,5,5,5,5,6,6,56,7,7,8,89,33,4,3,3)
lst = []
for item in tup:
    if item % 2 == 0:
        lst.append(item)
        print(item)
tup = tuple(lst)
print(tup)


#Write a program that merges two dictionaries into a single dictionary. If a key is common to both dictionaries, the value from the second dictionary should be used.

print('\n====================================== part 4  "Merge of two dictionaries"')
dic1 = {'a': 1, 'b': 2, 'c': 999}
dic2 = {'c': 4, 'd': 5, 'f': 6}
dic3 = dic1|dic2
print(dic3)

#Write a program that takes a list of integers as input and uses list comprehension to create a new list containing only the even numbers from the original list.
print('\n====================================== part 5  "List comprehension"')
lst = [1,2,3,4,5,5,5,5,6,6,56,7,7,8,89,33,4,3,3]
lst_res = [x for x in lst if x % 2 == 0]
print(lst_res)

#Write a program that takes a string as input and prints its reverse.
print('\n====================================== part 6 "String in reverse"')  
str = "abcdefg"
print(str[::-1])