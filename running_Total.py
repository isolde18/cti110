


total_sales = 0 

end =int(input("How many days your business operates: ")) 
for days in range(end):

    sales = float(input("Enter generated sales: "))

    total_sales = total_sales + sales

print ("Total amount of sales is", total_sales)
