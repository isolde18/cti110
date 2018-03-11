

keep_going='y' #set value of keep_going to y so loop iterates at least once
while keep_going=='y':
    sales=float(input("Enter sales amount: "))
    comm_rate=float(input("Enter commison rate: "))            
    commission= sales * comm_rate
    print ("Your commission is ", commission )#display commision calculated
    print () #to skip a line
    #below statement provides means to terminate loop or continue
    keep_going= input("Do you want to calculate another commission? Enter y if yes ")
    print()
