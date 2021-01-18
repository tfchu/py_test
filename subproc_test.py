from subprocess import Popen
from time import sleep

p = Popen(['python', 'test.py'])

for i in range(10):
    print('{}: {}'.format(i, p.poll()))
    sleep(1)