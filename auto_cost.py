


loan_pay = int(input("Enter monthly loan payment: "))
insurance = int(input("Enter monthly insurance bill: "))

gas = int(input("Enter the gas amount: "))
oil = int(input("Enter the oil amount: "))

tires = int(input("Enter the amount for tires: "))
maintenance = int(input("Enter the bill for maintenance: "))



def expenses (loan_payment, insurance_pay,g,o,t,m):

    monthly_expenses = loan_payment+insurance_pay+g+o+t+m

    yealy_exp = 12 *monthly_expenses
    print (" Monthly Expenses", monthly_expenses)
    print (" Yearly Expenses", yealy_exp)


expenses(loan_pay,insurance,gas,oil,tires,maintenance)
    
