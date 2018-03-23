#02.23.18
#CTI
# Write a loop program that asks the user to enter series of numbers
# The loop should continue until a negative number is entered

#Calculate the running total

total=0
num = int(input("Enter a number, enter negative number to exit: "))

while num >0:
    
    total+=num
    num = int(input("Enter a number"))

#Display the total

print("The total is: ", total)
