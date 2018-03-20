#CTI
#03/20/18

# first create acum.variables

total_weight = 0
count = 0
weight =float (input ("Enter patient's weight: "))

while weight > 0:
    total_weight+=weight
    count=count+1
    weight = float (input ("Enter patient's weight: "))
print ("Average weight is:", total_weight/count)
 
