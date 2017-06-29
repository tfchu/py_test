from abc import ABCMeta, abstractmethod

class ABCSortStrategy(metaclass=ABCMeta):
    @abstractmethod
    def sort(self, array):
        pass

class BubbleSort(ABCSortStrategy):
    def sort(self, array):
        print('bubble sort')

class QuickSort(ABCSortStrategy):
    def sort(self, array):
        print('quick sort')

class SortArray(object):
    def __init__(self, sort_strategy):
        self.sort_strategy = sort_strategy
    def do_sort(self, array):
        self.sort_strategy.sort(array)

def main():
    array = [5, 4, 6, 7, 2, 1, 9, 3, 8]
    sort_array = SortArray(BubbleSort())
    sort_array.do_sort(array)

if __name__ == '__main__':
    main()
