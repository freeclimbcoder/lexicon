import random
#Write a program that takes two integers as input, base and exponent, and calculates the power using loops.
def part1(base = 5, exp = 3, custom = False):
    print('====================================== part 1  "Base and exponent"')

    if custom:
        base = int(input('Enter the base value: '))
        exp = int(input('Enter the exponent value: '))
    result = 1
    for i in range(exp):
        result = result * base
    print(f'{base}^{exp} = {result}')


#Write a program that calculates the sum of all elements in a given tuple.
def part2(tup = (1,2,3,4,5,6)):
    result = 0
    print('\n====================================== part 2  "Tuple sum"')

    for item in tup:
      result = result + item
    print(f'Sum of tuple elements {tup} = {result}')

#Write a program that creates a new tuple containing only the even numbers from a given tuple of integers.
def part3(tup = (1,2,3,4,5,5,5,5,6,6,56,7,7,8,89,33,4,3,3)):
    print('\n====================================== part 3  "Even tuple"')

    lst = []
    for item in tup:
        if item % 2 == 0:
            lst.append(item)
    tup_result = tuple(lst)
    print(f'Even values from input tuple {tup} are: {tup_result}')


#Write a program that merges two dictionaries into a single dictionary. If a key is common to both dictionaries, the value from the second dictionary should be used.
def part4(dic1 = {'a': 1, 'b': 2, 'c': 999}, dic2 = {'c': 4, 'd': 5, 'f': 6}):
    print('\n====================================== part 4  "Merge of two dictionaries"')
    
    print(f'Merge of:\nFirst dictionaty {dic1}\nand second {dic2}\n= {dic1|dic2}')

#Write a program that takes a list of integers as input and uses list comprehension to create a new list containing only the even numbers from the original list.
def part5(lst = [1,2,3,4,5,5,5,5,6,6,56,7,7,8,89,33,4,3,3]):
    print('\n====================================== part 5  "List comprehension"')

    print(f'List {lst} with only even values = {[x for x in lst if x % 2 == 0]}')


#Write a program that takes a string as input and prints its reverse.
def part6(str = "abcdefg"):
    print('\n====================================== part 6 "String in reverse"') 

    print(f'Input string "{str}" in reverse = "{str[::-1]}"')

###############################################################################################################
###############################################################################################################
###############################################################################################################
    
# Given a list of integers, return True if the sequence of numbers 1, 2, 3 appears in the list somewhere
def arrayCheck(array = [1, 1, 2, 3, 1]):
    for i in range(len(array)-2):
        if array[i]==1 and array[i+1]==2 and array[i+2]==3:
            print(f'The sequence of numbers 1, 2, 3 appears in the list {array}')
            return True
    print(f'The sequence of numbers 1, 2, 3 does not appear in the list {array}')
    return False

# Given a string, return a new string made of every other character starting with the first, so "Hello" yields "Hlo".

def stringBits(str = 'Hello'):
    print(str[::2])
    return(str[::2])

# Given a string, return a string where for every char in the original, there are two chars.

def doubleChar(str = 'The'):
    str_res = ''
    for ch in str:
        str_res = str_res + 2*ch
    print(str_res)
    return(str_res)

# Return the number of even integers in the given array/list

def count_evens(lst = [1,2,3,4,5,6]):
    count = 0
    for item in lst:
        if item % 2 == 0:
            count = count + 1
    print(f'There are {count} even integers in {lst}')



  



def call_all():
    part1()
    part2()
    part3()
    part4()
    part5()
    part6()
    arrayCheck()
    arrayCheck([1, 1, 2, 4, 1])
    stringBits()
    stringBits('Heeololeo')
    doubleChar()
    count_evens()
    count_evens([2, 2, 0])




call_all()