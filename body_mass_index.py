

#Program should define the BMI
#Use the following formula
#BMI=weight*(703/height**2)


weight= int (input("Enter the weight "))

height= float (input("Enter the height "))

#Calculate the BMI

BMI=weight*(703/(height**2))

print("Your BMI is", BMI )

if BMI >25:
    print("Your BMI is overweight ")
elif BMI >= 18.5 and BMI <25:
    print("Your BMI is optimal ")
else:
    print ("Your BMI is under weight ")






