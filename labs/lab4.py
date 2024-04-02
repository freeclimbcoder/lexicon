# Write a lambda function to calculate the square of a number.
def square_func(x):
    s = lambda a : a*a
    return(s(x))
print([square_func(x) for x in range(16)])

# Write a function that takes a list of numbers and returns a list containing the squares of each number using lambda.

def square_lst(lst = [1,2,3]):
    squares = map(lambda x : x*x, lst)
    return(list(squares))
print(square_lst())
  
    


# Write a function that returns a list of prime numbers up to a given number using lambda.
def prime_num(n = 10):
    return(list(map(lambda a : a, range(n))))
print(prime_num())

# Write a program that modifies a global variable inside a function
global_variable = "global value"
def glob_modify():
    global global_variable
    print(global_variable)
    global_variable = "junk"
    print(global_variable)
glob_modify()
print(global_variable)

# Create a program that defines a function within another function and access variables from the outer function. 
# (Often called Enclosing Scope)

def outer_f():
    variable = "outer"
    def inner_f():
        print(variable)
    inner_f()
outer_f()



# Create a program that defines a variable with the same name as a global variable inside a function and observe its scope.
def scope_test():    
    global_variable = "inside function modify"
    print(global_variable)
scope_test()
print(global_variable)