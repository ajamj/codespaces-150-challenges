"""Write a program that will ask for a 
number of days and then will show how many hours, 
minutes and seconds are in that number of days."""

days = int(input("Input the number of the days: "))
hours = 24*days
minutes = 60*hours
seconds = 60*minutes
print("In " + str(days) + " days, there are " +str(hours) + " hours, " + str(minutes) + " minutes, " + " and "+str(seconds)+" seconds.")