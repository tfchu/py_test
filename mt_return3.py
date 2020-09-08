# multithreading with return values

'''
threading.Thread does not give return value
use multiprocessing.pool.ThreadPool instead
'''
import marktime # stopwatch
from multiprocessing.pool import ThreadPool

def foo(bar, baz):
    print('hello {0}'.format(bar))
    return 'foo' + baz

def foo2(bar, baz):
    print('hello2 ' + bar)
    return 'foo2 ' + baz

def main():
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(foo, ('world', 'foo')) # tuple of args for foo
    async_result2 = pool.apply_async(foo2, ('world', 'foo2'))

    # do some other stuff in the main process

    return_val = async_result.get()  # get the return value from your function.
    return_val2 = async_result2.get()

    print(return_val)
    print(return_val2)

if __name__ == "__main__":
    marktime.start('task')
    main()
    marktime.stop('task')
    print(marktime.duration('task').msecs)