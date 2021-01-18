# multithreading with return values

import marktime # stopwatch
#import json
import queue
from threading import Thread
from time import sleep

def foo(bar, baz):
    print('hello {0}'.format(bar))
    return 'foo ' + baz

def foo2(bar, baz):
    print('hello2 ' + bar)
    return 'foo2 ' + baz

def main():
    que = queue.Queue()

    # lambda arg1, arg2, ...
    t = Thread(target=lambda q, arg1, arg2: q.put(foo(arg1, arg2)), args=(que, 'world!', 'foo'))
    t2 = Thread(target=lambda q, arg1, arg2: q.put(foo2(arg1, arg2)), args=(que, 'world!', 'foo2'))

    # t.start()
    # t.join()
    # result = que.get()
    # print(result)

    t.start()
    t2.start()

    t.join()
    t2.join()

    t_ret = que.get()
    t2_ret = que.get()

    print(t_ret)
    print(t2_ret)

    #while not que.empty():
    #    print(que.get())

if __name__ == "__main__":
    marktime.start('task')
    main()
    marktime.stop('task')
    print(marktime.duration('task').msecs)
    #print(json.dumps(marktime.labels))