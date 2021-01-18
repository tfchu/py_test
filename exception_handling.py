''' 
e.g. 
    function A calls B, B calls C (A -> B -> C)
Exception handling flow
    - if exeption is not handled in C, it is passed to B. if not handled in B, then to A (C -> B -> A)
    - if exception is handled in C or B, then process continues to run to the end
Using Ctrl-C to stop program
    - catch KeyboardInterrupt exception at top-most function (e.g. A)
    - catch other exeptions at any function below (e.g. B, C)
    - if at the same level (e.g. function A), then KeyboardInterrupt cannot be caught (why?)
Code: see main() and recip()
'''
# import module sys to get the type of exception
import sys
from time import sleep

randomList = ['a', 0, 2]

def recip(entry):
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        print("The reciprocal of",entry,"is",r)
    except ZeroDivisionError:
        print('Divide by zero!!')
        sleep(3)
    except ValueError:
        print('Invalid value is used!!')
        sleep(3)
    finally:
        print('entry "{}" is processed'.format(entry))

def main():
    for entry in randomList:
        try:
            recip(entry)
        except KeyboardInterrupt:
            print('Ctrl-C detected.')
            sys.exit()
        finally:
            print('do finally.')    # executed
    print('do something else.')     # not executed

def recip1(entry):
    print("The entry is", entry)
    r = 1/int(entry)
    print('entry "{}" is processed'.format(entry))
    print("The reciprocal of",entry,"is",r)

def main1():
    for entry in randomList:
        try:
            recip1(entry)
        except ZeroDivisionError:
            print('Divide by zero!!')
            sleep(3)
        except ValueError:
            print('Invalid value is used!!')
            sleep(3)
        except KeyboardInterrupt:   # cannot catch
            print('Ctrl-C detected.')
            sys.exit()
        # except: 
        #     print("Oops!", sys.exc_info()[0], "occured.")
        finally:
            print('entry "{}" is processed'.format(entry))
    print('do something else.')

if __name__ == '__main__':
    main()

