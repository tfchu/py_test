'''
https://www.geeksforgeeks.org/multithreading-python-set-1/
TCB (Thread Control Block)     Process Control Block
--------------------------     --------------------------
| parent process pointer | --> | process id (PID)       |
--------------------------     --------------------------
| thread ID (TID)        |     | process state          |
--------------------------     --------------------------
| thread state           |     | process counter        |
--------------------------     --------------------------
| program counter        |     | registers              |
--------------------------     --------------------------
| register set           |     | memory limits          |
--------------------------     --------------------------
| stack pointer          |     | list of open files     |
--------------------------     --------------------------

Highlights
- each thread contains its own register set and local variables (in stack)
- all threads of a process share global variables (in heap) and program code
- process id (os.getpid()) is the same

Sequence for this example
main ~~~~~~~~~~~~~~ idle ~~~~~~~~~~~~~~~~ done 
    print_square ~~ sleep 3sec ~~~~~~~ done
      print_cube ~~ sleep 1sec ~ done
'''
from time import sleep
import threading
 
# simple multithreading without return values

def print_cube(num):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))
    sleep(1)
    print('print_cube done')
 
def print_square(num):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))
    sleep(3)
    print('print_square done')
 
if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
 
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
 
    # both threads completely executed
    print("main process done")

