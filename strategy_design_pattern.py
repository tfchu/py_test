'''
strategy (the algorithm) are encapsulated in classes
interchangable and independent from the client that uses it
'''
from abc import ABCMeta, abstractmethod
import time

class ABCSortStrategy(metaclass=ABCMeta):
    '''sort strategy abstract base class'''
    @abstractmethod
    def sort(self, array):
        pass
class BubbleSort(ABCSortStrategy):
    '''bubble sort'''
    def sort(self, array):
        print('bubble sort')
        for passnum in range(len(array)-1, 0, -1):
            for i in range(passnum):
                if array[i] > array[i+1]:
                    temp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = temp
        print(array)

class QuickSort(ABCSortStrategy):
    '''quick sort'''
    def sort(self, array):
        print('quick sort')
        self.quickSortHelper(array, 0, len(array) - 1)
        print(array)

    def quickSortHelper(self, array, first, last):
        '''helper'''
        if first < last:
            splitpoint = self.partition(array, first, last)
            self.quickSortHelper(array, first, splitpoint-1)
            self.quickSortHelper(array, splitpoint+1, last)

    def partition(self, array, first, last):
        '''partition'''
        pivotvalue = array[first]
        leftmark = first+1
        rightmark = last
        done = False
        while not done:
            while leftmark <= rightmark and array[leftmark] <= pivotvalue:
                leftmark = leftmark + 1
            while array[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark -1
            if rightmark < leftmark:
                done = True
            else:
                temp = array[leftmark]
                array[leftmark] = array[rightmark]
                array[rightmark] = temp
        temp = array[first]
        array[first] = array[rightmark]
        array[rightmark] = temp
        return rightmark

class SortArray(object):
    def __init__(self):
        self.sort_strategy = None
    def choose_strategy(self, sort_strategy):
        '''choose sorting strategy'''
        self.sort_strategy = sort_strategy
    def do_sort(self, array):
        '''do the sort'''
        self.sort_strategy.sort(array)

class StopWatch(object):
    def __init__(self):
        self.now = None
    def start(self):
        '''start stopwatch'''
        self.now = time.time()
    def stop(self):
        '''stop stopwatch'''
        print(time.time() - self.now)

def main():
    stop_watch = StopWatch()

    array = [5, 4, 6, 7, 2, 1, 9, 3, 8]
    #use bubble sort algo
    sort_array = SortArray()
    sort_array.choose_strategy(BubbleSort())
    stop_watch.start()
    sort_array.do_sort(array)
    stop_watch.stop()

    array = [5, 4, 6, 7, 2, 1, 9, 3, 8]
    #use quick sort algo
    sort_array.choose_strategy(QuickSort())
    stop_watch.start()
    sort_array.do_sort(array)
    stop_watch.stop()

if __name__ == '__main__':
    main()
