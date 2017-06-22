'''
Design a tool to monitor how a product is produced in a company (e.g. Company -> Worker -> Machine)
Traditional approach: Company class is associated with Worker class
class Company():
    def __init__(self):
        self.worker = Worker()
    def produce(self):
        self.worker.work()
If a new type of worker is added (e.g. SpecializedWorker class), then Company needs to be changed
Following code demonstrate dependency inversion
    - Worker and SpecializedWorker classes implements an interface
    - or inherit abstract class
'''
from abc import ABCMeta, abstractmethod

class Company(object):
    '''High level logics of Company,
    this will never change after applying dependency inversion'''
    def __init__(self):
        self.worker = None
    def set_worker(self, worker):
        '''set different type of worker'''
        self.worker = worker
    def produce(self):
        '''in order for company to produce, workers work'''
        self.worker.work()
#workers
class ABCWorker(metaclass=ABCMeta):
    '''abc for all types of worker to inherit from'''
    def __init__(self):
        self.machine = None
    def set_machine(self, machine):
        '''concrete method used to set specific machine'''
        self.machine = machine
    @abstractmethod
    def work(self):
        '''abstract method'''
        pass
class Worker(ABCWorker):
    '''regular work'''
    def work(self):
        '''low level logics'''
        print('Regular worker is working. ')
        self.machine.make()
#add a new type of worker
class SpecializedWorker(ABCWorker):
    '''specialized worker'''
    def work(self):
        '''low level logics'''
        print('Specialized worker is working. ')
        self.machine.make()
#machines
class ABCMachine(metaclass=ABCMeta):
    '''abc for all types of machines to inherit from'''
    @abstractmethod
    def make(self):
        '''abstract method'''
        pass
class Machine(ABCMachine):
    '''regular machine'''
    def make(self):
        '''how regular machine works'''
        print('Regular machine is making.')
class SpecializedMachine(ABCMachine):
    '''specialized machine'''
    def make(self):
        '''how specialized machine works'''
        print('Specialized machine is making.')
def main():
    '''test the code'''
    company = Company()
    worker = Worker()
    worker.set_machine(Machine())
    company.set_worker(worker)
    company.produce()
    #add new type of worker
    worker = SpecializedWorker()
    worker.set_machine(SpecializedMachine())
    company.set_worker(worker)
    company.produce()

if __name__ == '__main__':
    main()
