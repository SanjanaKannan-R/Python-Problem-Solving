'''Get a number from user and divide by the number by 8 and print the remainder.'''

def division():
    try:
        number=int(input())
        remainder=number%8
        print(remainder)
    except ValueError:
        print("Error")
division()