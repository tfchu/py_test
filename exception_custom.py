from exception_custom_import import ValueTooLargeError, ValueTooSmallError

# our main program
# user guesses a number until he/she gets it right

# you need to guess this number
number = 10

while True:
   try:
       i_num = int(input("Enter a number: "))
       if i_num < number:
           raise ValueTooSmallError(i_num)
       elif i_num > number:
           raise ValueTooLargeError(i_num)
       break
   except ValueTooSmallError as e:
       print(e)
   except ValueTooLargeError as e:
       print(e)
print("Congratulations! You guessed it correctly.")