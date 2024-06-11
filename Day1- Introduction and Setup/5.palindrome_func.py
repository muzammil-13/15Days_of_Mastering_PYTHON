"""
Create a Python function to check if a given string is a
palindrome
"""


def palindrome(str):
    return str == str[::-1]


string = input("Enter the string: ")
if palindrome(string):
    print(f"{string} is palindrome")
else:
    print(f"{string} is not a palindrome")
