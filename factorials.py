#CTI
#Write a program that asks the user for a nonnegative integer
#and then uses a loop to calculate the factorial of that number
#Display the factorial


factorial =1
num=int(input("Enter a nonnegative integer: "))

while num < 0:
    print("Enter new number: ")
    num=int(input("Enter a nonnegative integer: "))
    

for n in range (1,num+1):
    factorial = factorial * n


print ("The factorial of ", num ,"is", factorial)
    


