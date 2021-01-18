# multithreading with return values

import marktime # stopwatch
from threading import Thread

def foo(bar, baz):
    print('hello {0}'.format(bar))
    return 'foo ' + baz

def foo2(bar, baz):
    print('hello2 ' + bar)
    return 'foo2 ' + baz

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)

        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        Thread.join(self)
        return self._return

def main():
    twrv = ThreadWithReturnValue(target=foo, args=('world!', 'foo'))
    twrv2 = ThreadWithReturnValue(target=foo2, args=('world!', 'foo2'))

    twrv.start()
    twrv2.start()

    print(twrv.join())
    print(twrv2.join())

if __name__ == "__main__":
    marktime.start('task')
    main()
    marktime.stop('task')
    print(marktime.duration('task').msecs)
    #print(json.dumps(marktime.labels))