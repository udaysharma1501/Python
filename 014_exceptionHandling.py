# exception - event detected during execution that may interrupt the flow of a program
# any dangerous code comes under try block
try:
    num = int(input("enter numerator: "))
    den = int(input("enter denominator: "))

# good practice to catch specific exceptions as above as possible

# as e ---> works as typedef
except ZeroDivisionError as e:
    print(e)
    print("cannot divide by zero")
except ValueError as e:
    print(e)
    print("cannot divide by non number entity")
except Exception as e:
    print(e)
    print("something went wrong")
else:
    print(num/den)
finally: # has the functionalty of a destructor
    print("whatever may happen, 'finally' will always execute")