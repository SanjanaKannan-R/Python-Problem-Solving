'''Problem 4
Question: Get a number from user and check whether it is prime or not, then print the
result.
Testcase:
Input: 61 → Output: Number is Prime
Input: 1200 → Output: Number is not Prime'''


def check_prime():
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("Number is not Prime")
                break
        else:
            print("Number is Prime")
    else:
        print("Number is not Prime")
check_prime()
