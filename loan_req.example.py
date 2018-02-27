#CTI110
#Name
#Date
#Create a program for loan approval

#Define variables or/and get user input

salary = int (input (" Enter salary "))

yearOnJob = int (input ("Enter years on job "))

#Calculations or decision structure

if salary >= 30000:
    if yearOnJob >=2:
        print("You qualify for a loan")
    else:
        print("You must have worked for 2 years")
else:
    print ("You don't earn enough")

#Display results 
