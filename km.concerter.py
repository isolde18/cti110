
#CTI
#4/19/2018
#Write a program that asks the user to enter a distance in km
#and then converts that distance to miles

CONVERSION_FACTOR=0.6214

def main():
    #get the distance in kilometers

    kilometers=float(input('Enter a distance in kilometers: '))
    #display the distance converted to miles

    show_miles(kilometers)

def show_miles(km):
    #calculate miles
    miles=km*CONVERSION_FACTOR
    #DISPLAY THE MILES
    print (km,'kilometer equals', miles, 'miles')

main()
    
