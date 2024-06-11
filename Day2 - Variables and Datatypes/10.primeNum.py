"""
Write a program to check if a number is prime
"""


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True


num = int(input("Enter a number: "))
print("Number: ",num)
if prime(num):
    print("Prime")
else:
    print("Not prime")