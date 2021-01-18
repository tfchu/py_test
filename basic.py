import time

'''
compare tuple and list
in general
tuple: heterogeneous (like c struct), e.g. (year, month, day) or (quotient, remainder)
list: homogeneous (like c array), e.g. [0, 1, 2, 3, 4, 5]
access an item in either tuple or list: xx[0], xx[1], .. 
'''
def tuple_list_compare():
    # get tuple
    print(divmod(11, 3))    # (3, 2). note: 11/3 = 3 ... 2
    # get list
    print(dir(time))        # a list of attributes in 'time' module. [..., 'localtime', 'sleep', ...]

if __name__ == "__main__":
    tuple_list_compare()