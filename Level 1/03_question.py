'''Get a number from user and multiply 3 to that number and print the result.'''

def multiply():
    try:
        number = int(input())
        result = number * 3
        print(result)
    except ValueError:
        print("Error")
multiply()