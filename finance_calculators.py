import math

from operator import index

# this prints title and user instructions for calulation of bond for house  
# or investment depending on user's choice using formulars.

print("Import Math \n".upper())

print("Investment - to calculate the amount of interest you'll earn on your investment")

print("Bond - to calculate the amount you'll have to pay on a home loan ")

print("Enter either 'investment' or 'bond' from the menu above to proceed:\n")

# the user input is requested in the variable "select_interest"

select_interest = input("Please enter bond or investment: ")

# if statment checks that user input stored in "select_interest"
# is equal to "investment" in lowercase using the lower method.
# all the user inputs and formalar are assigned with requisite variables

if select_interest.lower() == "investment":
   P = Amount_deposit = int(input("Enter Deposit Amount: "))
   The_interest_rate = float(input("Enter Interest Rate: \t"))
   r = The_interest_rate/100
   t = years_investing = int(input("Enter years: \t"))

   # if user selects investment user is requested to input "simple" or "compound"
   # and it is stored in variable "interest".

   interest = input("Please Enter Simple or Compound Interest: ")
   
   # checks that when user inputs "simple", simple interest of investment is 
   # calculated using simple interest formular.

   if interest.lower() =="simple" :
     simple_interest  = P*(1 + r*t)
     print("Simple interest: ")
     print(simple_interest)
   
    # calculates compound interest using formular when user input is "compound".

   elif interest.lower() == "compound":
    compound_interest  = P*math.pow((1 + r),t)
    print("Compound Interest: ")
    print(compound_interest)

   # if user input for selection of "simple" or "compound" 
   # is wrong it prints an error meassage.

   else : 
    print("error message: Please enter simple or compound")
   
# checks that user input is equal to "bond" in lower case, then using the repayment formular
# variables  with assigned inputs it calculates the Loan repayment.

elif select_interest.lower() == "bond":
     P = House_value = int(input("Enter Current house Value: \t"))
     monthly_interest_rate = int(input("Enter Monthly Interest Rate: \t"))
     i = monthly_interest_rate/100/12
     n = number_of_month_bond_repayemnt = int(input("Enter Number of Months for Bond Repayment: \t"))
     repayment = (i * P)/(1 - (1 + i)**(-n))
     print("Loan Repayment: ")
     print(repayment)

# if user input for selecting "investment" or "bond" is 
# incorrect it issues an error message.

else : 
     print("error message: Please enter investment or bond ")