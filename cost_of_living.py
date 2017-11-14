utilities = ""
internetCable = ""
rent = ""
totalRent = 0
groceries = 0
coupons = ""
carNumber = ""
carGas = ""
carPayments = ""
totalCar= 0
totalCOL= 0


import time
def carQuestions():
    print("How many vehicles do you own? (please type digits)")
    carNumber = input()
    print("How much do you pay per month for gas for your car(s)?")
    carGas = input()
    print("How much do you pay in loans, lease payments, or otherwise for your car(s) per month?")
    carPayments = input()
    global totalCar
    totalCar = int(carGas) + int(carPayments)
    print("Your total for cars each month is: " + str(totalCar))
    
def calcTotalCOL():
    global totalCOL
    totalCOL = int(totalRent) + int(groceries) + int(totalCar)

#Part 1: Rent
print("How much rent do you pay per month?")
rent = int(input())
print("How much do you pay for Internet + cable per month?")
internetCable = int(input())
print("How much do you pay for utilities per month?")
utilities = int(input())
totalRent = rent + utilities + internetCable
print("Your total for rent (including utilities and Internet/cable) is: " + str(totalRent))

#Part 2: Groceries
print("How much do you spend on groceries per month?")
groceries = int(input())
print("Do you use coupons? y/n")
coupons = input()
try:
    if coupons == "y":
        coupons = "y"
    elif coupons == "n":
        coupons = "n"
    else:
        print("That was not a valid answer")
except ValueError:
    print("Value Error")

#Part 3: Car
print("Do you own or lease a car? y/n")
carChoice = input()
if carChoice == "y":
    carQuestions()
elif carChoice == "n":
    print("Thank you.")
else:
    print("That was not a valid answer.")

#Test of Total Function
calcTotalCOL()
print("Your total cost of living (COL) is: " + str(totalCOL))
print("Rent is " + str(round((totalRent/totalCOL),2)*100) + "% of your costs.")
print("Groceries are " + str(round((groceries/totalCOL),2)*100) + "% of your costs.")
print("Cars are " + str(round((totalCar/totalCOL),2)*100) + "% of your costs.")

time.sleep(150)
