# https://medium.com/@happymishra66

# regular function
def add_func(x, y): 
    print('add_function: {}'.format(x+y))
add_func(2, 3)

# lambda anonymous function
# lambda arguments : expression
add_lambda = lambda x, y: x + y
print('add_lambda: {}'.format(add_lambda(2, 3)))

# map(function_object, iterable1, iterable2, ...)
#   executes the function_object for each element in the sequence
# map() returns another iterable which can be used in other loops directly
# list() is just to convert map() object to list so it can print
print(list(map(lambda x: x*2, [1, 2, 3, 4])))   # [2, 4, 6, 8]

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
print(list(map(lambda x: x['name'] == 'python', dict_a)))   # [True, False]

list_a = [1, 2, 3]
list_b = [10, 20, 30]
print(list(map(lambda x, y: x + y, list_a, list_b))) # Output: [11, 22, 33]

# filter(function_object, iterable)
#   function_object is called for each element of the iterable 
#   and filter returns only those element for which the function_object returns true
a = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x : x % 2 == 0, a)))   # [2, 4, 6]

'''
default value in lambda
case 1: lambda: i
    loop 0: lambda: 0 -> [(lambda: 0)]
    loop 1: lambda: 1 -> [(lambda: 1), (lambda: 1)]
    loop 2: lambda: 1 -> [(lambda: 2), (lambda: 2), (lambda: 2)]
    ... (i keeps being replaced with newer value)
    at the end all lambda functions return 9
case 2: lambda a=i: a
    loop 0: [(lambda a=0: a)]
    loop 1: [(lambda a=0: a), (lambda a=1: a)]
    loop 2: [(lambda a=0: a), (lambda a=1: a), (lambda a=2: a)]
    ... (original assigned value is preserved)
    at the end lambda function return its original assigned value
'''
print([c() for c in [(lambda: i) for i in range(10)]])          # case 1: [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
print([c() for c in [(lambda a=i: a) for i in range(10)]])      # case 2: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]