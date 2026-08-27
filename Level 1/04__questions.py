'''Get a number from user and divide by the number by 6 and print the quotient.'''

def divide_number():
    try:
        number = int(input())
        quotient = number/6
        print(quotient)
    except ValueError:
        print("Error")
divide_number()