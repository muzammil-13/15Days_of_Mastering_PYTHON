"""
Write a Python program to check if a given string is a
pangram (contains all letters of the alphabet))
"""
input_str=input("Enter a string: ")

uniq_ltrs=set()

for i in input_str:
    if i.isalpha():
        uniq_ltrs.add(i)

if len(uniq_ltrs)==26:
    print("The string is a pangram")
else:
    print("The string is not pangram")