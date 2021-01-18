'''
use multithreading.Array to use array between processes
use multithreading.Value to use single value between processes (Value.value is the value)

each process (main and foo) has its own copy of array and value, located at different address
the content of array and value is stored in shared memory, hence contents are the same
'''

import multiprocessing

def foo(arr, val):
    arr[0] = 1
    arr[1] = 2
    arr[2] = 3
    arr[3] = 4
    val.value = sum(arr)
    print('process array: {}'.format(arr[:]))       # process array: [1, 2, 3, 4]
    print('process sum: {}'.format(val.value))      # process sum: 10

if __name__ == '__main__':
    # create an array of 4 integers
    mp_array = multiprocessing.Array('i', 4)
    # create an interger holding sum of the array
    mp_value = multiprocessing.Value('i')

    p = multiprocessing.Process(target=foo, args=(mp_array, mp_value))
    p.start()
    p.join()

    print('main process array: {}'.format(mp_array[:]))     # main process array: [1, 2, 3, 4]
    print('main process sum: {}'.format(mp_value.value))    # main process sum: 10
