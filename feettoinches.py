

#CTI
#4/19/2018
#convert feet to inches

CONVERSION_FACTOR=12

#main function

def main():
    #get a number of feet from the user
    feet=int(input('enter a number of feet: '))

    #convert that to inches

    print(feet,'equals',feet_to_inches(feet),'inches.')

#the function feet_to_inches converts feet to inches

def feet_to_inches(feet):
    return feet * CONVERSION_FACTOR

#call the main function

main()
