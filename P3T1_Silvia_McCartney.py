
#03.02.2018
#CTI110
#create two rectangles and write a program that asks for 
#lenght and width of each and calculates the area1, and 2 
#tell which rectangle has a > area
#tel if the areas are the same


print ("This program will calculate the area of rectangle 1 and rectangle 2")
#Calculate the area of rectangle 1

length_rectangle_1= int (input ("length "))
width_rectangle_1= int (input ("width "))

area_1= length_rectangle_1 * width_rectangle_1

print ("area_1 = " , length_rectangle_1 * width_rectangle_1)


#Calculate the area of rectangle 2

length_rectangle_2= int (input ("length "))
width_rectangle_2= int (input ("width "))
area_2= length_rectangle_2 * width_rectangle_2

print ("area_2 = " , length_rectangle_2 * width_rectangle_2)



if area_1 > area_2:
    print ("rectangle 1 has the greater area ")
elif area_2 > area_1:
    print ("rectangle 2 has the greater area ")
if area_1 == area_2:
    print ("the areas are the same ")
    







