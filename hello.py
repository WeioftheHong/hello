# hello.py
# says 'Hello, git!'
# also does fizzBuzz
# hundred-fizz branch
# prints up to 100

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

n = 100

fizzBuzzIterative(1, n)
