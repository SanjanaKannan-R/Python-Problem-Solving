''' Get a number from user and subtract 5 to that number and print the result.'''


def subtract_number():
    try:
        number = int(input())
        difference = number - 5
        print(difference)
    except ValueError:
        print("Error")
subtract_number()