# hello.py
# says 'Hello, git!'
# also does fizzBuzz
# development branch
#

def fizzBuzzIterative(start, end):
    for i in range(start, end):
        fizzBuzzPrint(i)

def fizzBuzzPrint(n):
    mod3 = not n % 3
    mod5 = not n % 5
    if (not mod3 and not mod5):
        print(n)
    elif (mod3 and mod5):
        print("Fizz Buzz")
    elif (mod3):
        print("Fizz ")
    elif (mod5):
        print("Buzz ")

print("'Hello, git!'")

n = int(input("Fizz Buzz #? "))

fizzBuzzIterative(1, n)
