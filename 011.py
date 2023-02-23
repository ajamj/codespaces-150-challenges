"""Task the user to enter a number over 100 and then enter a number under 
10 and tell them how many times the smaller number goes into the larger 
number in a user-friendly format."""

num_over_100 = int(input("Input number over 100: "))
while num_over_100<100:
    print("The number must over 100!")
    num_over_100 = int(input("Input the number over 100: "))

num_under_10 = int(input("Input number under 10: "))
while num_under_10>10:
    print("The number must onder 10!")
    num_under_10 = int(input("Input number under 10: "))

divide = num_over_100/num_under_10
print("It will take ",divide,"times from",num_under_10,"to",num_over_100)