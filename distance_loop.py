#Distance traveled program
#The program should ask 2 questions
#What is the speed
#What are the numbers of hours the vehicle has traveled
#Then, it should displays the distance that the
#vehicle has traveled for each hour of that time period

speed=int (input("Enter the speed of the vehicle in mph: "))
hours =int(input ("Enter the hours it has traveled: "))



for time in range(1,hours+1):
    print ("distance" , '=', speed * time) 
