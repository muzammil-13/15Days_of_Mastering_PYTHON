"""
Create a function to reverse a given string)

"""


def rev_string(str):
    return str[::-1]


input_str = input("Enter the string: ")
print("Input string is ",input_str)

rev_output=rev_string(input_str)
print("Reversed string is ",rev_output)
