'''Problem 4
Question: Write a loop program to print the sum of 6 to 1.
Testcase:
Output: 21'''

sum = 0
for i in range(6, 0, -1):   
    sum += i
    print(sum)