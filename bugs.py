

#Entomologist collects bugs for seven days
#Calculate the running total

bugs_total=0
#Get the bugs collected for each day.

for day in range (1,8):
    print("Enter the number of bugs collected on day: ", day)
    bugs=int(input ())
    bugs_total +=bugs


#Display the total bugs.

print ("You collected a total of", bugs_total,"bugs")
    

