'''
Compare simple class and abstract base class
If a method is NOT implemented in derived class, then
    1. for simple class, the derived class can be instantiated and run methods
        -> error is raised only when calling the methods that is not implemented
    2. for abc, the derived class cannot be instantiated, following error occurs when instantiating
        -> TypeError: Can't instantiate abstract class Child with abstract methods method2
        note. keyword @abstractmethod must be included in abc
'''

from abc import ABCMeta, abstractmethod

class Base(object):
    def method1(self):
        raise NotImplementedError
    def method2(self):
        raise NotImplementedError

class ABCBase(metaclass=ABCMeta):
    @abstractmethod
    def method1(self):
        pass
    @abstractmethod
    def method2(self):
        pass

class Child(ABCBase):
    def method1(self):
        print('this is method1')

def main():
    child = Child()
    child.method1()
    child.method2()

if __name__ == '__main__':
    main()
