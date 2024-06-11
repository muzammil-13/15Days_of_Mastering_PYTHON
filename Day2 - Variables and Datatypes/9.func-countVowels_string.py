"""
Create a function to count the number of vowels in a
given string)
"""


def count_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in str:
        if i in vowels:
            count += 1
    return count


string = input("Enter a string: ")
result = count_vowels(string)
print(f"Number of vowels in the string: ", result)
