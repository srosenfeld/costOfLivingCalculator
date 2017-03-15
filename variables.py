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

def carQuestions():
    print("How many vehicles do you own? (please type digits)")
    carNumber = input()
    print("How much do you pay per month for gas for your car(s)?")
    carGas = input()
    print("How much do you pay in loans, lease payments, or otherwise for your car(s) per month?")
    carPayments = input()
    totalCar = int(carGas) + int(carPayments)
    print("Your total for cars each month is: " + str(carTotal))
    
def calcTotalCOL():
    global totalCOL
    totalCOL = int(totalRent) + int(groceries) + int(totalCar)
    
#calcTotalCOL()
#print("Your total cost of living (COL) is: " + str(totalCOL))
