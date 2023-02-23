"""Ask for the total price of the bill, then ask how 
many diners there are. Divide the total bill by the 
number of diners and show how much each 
person must pay."""

bill = int(input("Total price of the bill: "))
diners = int(input("Total of diners: "))
pay_per_person = float(bill/diners)
print("Each person must pay "+str(pay_per_person)+".")
