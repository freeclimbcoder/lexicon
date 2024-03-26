print('#=======================  Part 1')
s = 'Python'

#'o'
print(s[-2:-1])

#'Pyth'
print(s[:-2])

#'yth'
print(s[1:-2])

#'nohtyP'
print(s[::-1])


print('#=======================  Part 2')
# Reassign "hello" to be "goodbye"
l = [3,7,[1,4,'hello']]
l[2][2] = 'goodbye'
print(l)

print('#=======================  Part 3')
# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])

print('#=======================  Part 4')
#  Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(mylist))

print('#=======================  Part 5')
# Use print formatting to print the following string:
age = 4
name = "Sammy"

print("Hello my dog's name is {} and he is {} years old".format(name, age))
print(f"Hello my dog's name is {name} and he is {age} years old")