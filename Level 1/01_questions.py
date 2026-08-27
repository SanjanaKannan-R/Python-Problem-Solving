'''Get a number from user and add 2 to that number and print the result.'''

def add_numbers():
    try:
        number=int(input())
        result = number+2
        print(result)
    except ValueError:
        print("Error")
add_numbers()

