'''
open python, define a variable str = "test string", then print it and exit

Popen.communicate() is a helper method that does a 
one-time write of data to stdin and creates threads to pull data from stdout 
and stderr. It closes stdin when its done writing data and reads  stdout and 
stderr until those pipes close. You can't do a second communicate because the 
child has already exited by the time it returns.

Other subprocess tutorial: 
https://crashcourse.housegordon.org/python-subprocess.html#using-pipe-with-checkcallcheckoutputcall
'''
import sys
from subprocess import Popen, PIPE, STDOUT

PYTHON = sys.executable

def main():
    process = Popen([PYTHON], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

    # same as 'str = "test string"\nprint(str)\nexit()\n', more readable
    commands = ('str = "test string"\n'
                'print(str)\n'
                'exit()\n')

    # argument needs to be byte, can also use b'command string'
    out, err = process.communicate(input=commands.encode('utf-8'))
    print(out.decode('utf-8'))
    process.terminate()

if __name__ == '__main__':
    main()
