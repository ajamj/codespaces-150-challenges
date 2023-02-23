"""Ask the user to enter three 
numbers. Add together the first 
two numbers and then multiply 
this total by the third. Display the 
answer as The answer is 
[answer]"""

first_num = int(input("Enter the first number: "))
sec_num = int(input("Enter the second number: "))
third_num = int(input("Enter the third number: "))
total = (first_num+sec_num)*third_num

print("The answer is "+str(total)+".")