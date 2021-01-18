'''
https://pymotw.com/3/signal/
Ubuntu manpages
$ kill -l                   // 2 user-defined signal exists in Ubuntu, NOT Windows
    2) SIGINT ... 10) SIGUSR1 ...	12) SIGUSR2
$ kill -l SIGINT            // check number of SIGINT
$ kill -<signal> <pid>      // kill a process
    e.g. $ kill -USR1 9988  // remove 'SIG' in 'SIGxxx'

Python doc
signal.signal(signalnum, handler)
- signalnum is the number above, e.g. 2 for SIGINT
- handler takes 2 argements: signal number and current stack frame

Usage: 
- run the code in one terminal, this shows pid (e.g. 9988)
- in another terminal
    $ kill -USR1 9988       // send SIGUSR1
    $ kill -USR2 9988       // send SIGUSR2
    $ kill -INT 9988        // send keyboard interrupt (Ctrl-C), process stops here

Output: 
    Waiting...
    Received: 10
    Waiting...
    Received: 12
    Waiting... ()
    Traceback (most recent call last):
    File "py_test.py", line 20, in <module>
        time.sleep(3)
    KeyboardInterrupt

'''
import signal
import os
import time

def receive_signal(signum, stack):
    print('Received:', signum)

# Register signal handlers
signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

# Print the process ID so it can be used with 'kill'
# to send this program signals.
print('My PID is:', os.getpid())

while True:
    print('Waiting...')
    time.sleep(3)