"""Ask the user for their name and their age. Add 1 to their age 
and display the output [Name] next birthday you will be [new age]."""

name = input("Your name: ")
age = int(input("Your age: "))

next_age = age+1
print(name+", next birthday you will be "+str(next_age)+".")