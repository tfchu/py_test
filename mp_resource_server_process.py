'''
when python program starts, a server process starts, which can be used to hold objects. 
a server process is used to fork new process
(main) -> (server process) -> new process 1
                           -> new process 2

more flexible than shared memory (as it can hold more than array and value). but slower
use multiprocessing module Manager class to control server process
'''

import multiprocessing

def add_item(new_item, my_list):
    my_list.append(new_item)
    print('new process list: ' + '|'.join(map(str, my_list)))   # new process list: 1|2|3|4

if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        my_list = manager.list([1, 2, 3])   # create a list in server process
        new_item = 4
        
        # add the new item in new process
        p = multiprocessing.Process(target=add_item, args=(new_item, my_list))
        p.start()
        p.join()

        print('main process list: ' + '|'.join(map(str, my_list)))  # main process list: 1|2|3|4
