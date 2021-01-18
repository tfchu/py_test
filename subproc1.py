'''
https://stefan.sofa-rockers.org/2013/08/15/handling-sub-process-hierarchies-python-linux-os-x/
process hierarchy: A --> B --> C
press ctrl-C kills all processes

Signals: IPC (inter-process communication) on POSIX OS (e.g. Linux, Mac OS)
- SIGINT: Ctrl-C sent from control terminal
- SIGTERM: sent to process to request termination, can be caught and interpreted/ignored by the process
    - receiving process can release resource and save state if needed
    - e.g. term() call in Python. Almost same as SIGINT
- SIGKILL: cause process to terminate immediately, cannot be caught or ignored, no cleanup can be done

Running the code: 
# python3 subproc1.py 
A started with pid=2098, ppid=2087
B started with pid=2099, ppid=2098
C started with pid=2100, ppid=2099
^CC got KeyboardInterrupt
A got KeyboardInterrupt
B got KeyboardInterrupt
B's child C terminated with code 0
A's child B terminated with code 0

'''

import subprocess
import sys
import time
import os

PYTHON = sys.executable
SCRIPT = __file__

def main(name):
    print('%s started with pid=%d, ppid=%d' % (name, os.getpid(), os.getppid()))

    # A and B spawn a subprocess
    if name == 'A':
        child = subproc('B')
    elif name == 'B':
        child = subproc('C')
    else:
        child = None

    # Sleep and wait for a Ctrl-C
    try:
        time.sleep(10)
        print('%s done' % name)
    except KeyboardInterrupt:
        print('%s got KeyboardInterrupt' % name)
    finally:
        if child:
            retcode = child.wait()
            print('%s\'s child %s terminated with code %d' % (name, child.args[2], retcode))

def subproc(name):
    """Create and return a new subprocess named *name*."""
    proc = subprocess.Popen([PYTHON, SCRIPT, name])
    return proc

if __name__ == '__main__':
    name = sys.argv[1] if len(sys.argv) > 1 else 'A'
    main(name)
