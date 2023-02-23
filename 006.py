"""Ask how many slices 
of pizza the user 
started with and ask 
how many slices 
they have eaten. 
Work out how many 
slices they have left 
and display the 
answer in a user friendly format."""

pizza = int(input("How many slices of pizza did you have? "))
eaten_pizza = int(input("How many slices of pizza have you eaten? "))
while eaten_pizza>pizza:
    print("Impossible! The number of slices of pizza eaten must be less or equal to the number of slices of pizza at the beginning.")
    eaten_pizza = int(input("Please enter the correct number of eaten pizza: "))

remaining = pizza-eaten_pizza
if remaining>0:
    print("The pizza you have now is "+str(remaining)+".")
else:
    print("No pizza slices left.")