''' https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/
example: 2 threads share the same resource 'x'
without locking the resoure, 'race condition' happens
x is supposed to be incremented by thread 1, then again by thread 2 (10 -> 12 at the end)
without locking 2nd thread reads the original x before increment as follows: 
--- time --->
x       10
thread  read(10)    10+1    11
thread    read (10)   10+1    11
 
threading.Lock()
- acquire([blocking]): thread is blocked until unlocked
- release(): reset to unlock
after thread 1 locks resources, thread 2 cannot lock it again (wait until release)
'''
import threading

# global variable x
x = 0
 
def increment():
    """
    function to increment global variable x
    """
    global x
    x += 1
 
def thread_task(lock):
    """
    task for thread
    calls increment function 100000 times.
    """
    for _ in range(100000):
        lock.acquire()
        increment()
        lock.release()
 
def main_task():
    global x
    # setting global variable x as 0
    x = 0
 
    # creating a lock
    lock = threading.Lock()
 
    # creating threads
    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))
 
    # start threads
    t1.start()
    t2.start()
 
    # wait until threads finish their job
    t1.join()
    t2.join()
 
if __name__ == "__main__":
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i,x))