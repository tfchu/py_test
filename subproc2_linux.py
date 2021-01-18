'''
https://stefan.sofa-rockers.org/2013/08/15/handling-sub-process-hierarchies-python-linux-os-x/
> python subproc2_linux.py      // result is same as subproc1.py in Linux (use Ctrl-C to terminate)
> python subproc2_linux.py term // parent process (A) waits for 1 sec then terminate child (B)
                                // child (B) gets SIGTERM and run cleanup(), which terminates its child (C) if applicable

Sequnce for using 'term'
- terminate = True and name = 'A', call main('A', True)
    - print 'A started'
    - child = subprocess('B'), call main('B', False)
        - print 'B started'
        - child = subprocess('C'), call main('C' False)
            - print 'C started'
            - child = None
- process A: terminate = True, so wait 1 sec, then terminate process B
    - process B gets SIGTERM, call cleanup('B', <process C>, <signum of SIGTERM>, <stack>)
    - print 'B got a SIGTERM'
    - terminate process C
        - process C gets SGTERM, call cleanup('C', None, <signum of SIGTERM>, <stack>)
        - print 'C got a SIGTERM'
    - print 'A ended'

Output: 
    $ python3 py_test2.py term
    A started
    B started
    C started
    B got a SIGTERM
    C got a SIGTERM
    A ended
'''

import functools
import signal
import subprocess
import sys
import time
import traceback

PYTHON = sys.executable
SCRIPT = __file__
SIGNALS = {
    signal.SIGINT: 'SIGINT',
    signal.SIGTERM: 'SIGTERM',
}

def main(name, terminate):
    """If *terminate* is ``True`` (should only be the case if *name* is ``A``),
    A will try to terminate B.

    B and C will always just sleep and wait for things to happen ...

    """
    print('%s started' % name)

    # A and B spawn a subprocess
    if name == 'A':
        child = subproc('B')
    elif name == 'B':
        child = subproc('C')
    else:
        child = None

    # Curry our cleanup func and register it as handler for SIGINT and SIGTERM
    # signal(signum, handler): handler takes 2 arguments by default, signum and stack frame
    # Using partial() adds 'name' and 'child' before default arguments
    handler = functools.partial(cleanup, name, child)
    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGTERM, handler)

    if terminate:
        # A tries to terminate B
        time.sleep(1)
        term(child)
        print('%s ended' % name)
    else:
        time.sleep(10)
        print('%s done' % name)
        if child:
            child.wait()

def subproc(name):
    """Create and return a new subprocess named *name*."""
    proc = subprocess.Popen([PYTHON, SCRIPT, name])
    return proc

def term(proc):
    """Send a SIGTERM to *proc* and wait for it to terminate."""
    proc.terminate()  # Sends SIGTERM
    proc.wait()

def cleanup(name, child, signum, frame):
    """Stop the sub-process *child* if *signum* is SIGTERM. Then terminate."""
    try:
        print('%s got a %s' % (name, SIGNALS[signum]))
        if child and signum != signal.SIGINT:
            term(child)
    except:
        traceback.print_exc()
    finally:
        sys.exit()

if __name__ == '__main__':
    terminate = False
    if len(sys.argv) == 1:
        name = 'A'
    elif sys.argv[1] == 'term':
        terminate = True
        name = 'A'
    else:
        name = sys.argv[1]  # B or C

    main(name, terminate)