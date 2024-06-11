"""
Create a program that takes a sentence as input and
counts the number of words in it
"""

str=input("Enter the sentence: ")

count=0

words=str.split()

for i in words:
    count+=1

print("Number of words: ",count)