from matplotlib.pyplot import show, hist
import random


#Change in balance function in case the rate fluctuates
def changeInBalance(account_balance):
    #random.gauss creates a gaussean bell curve distribution with average=3% and standard deviation=2%
    return account_balance * random.gauss(0.03, 0.02)


#Initial Conditions
num_of_years = 10
simulationCount = 1000
#Set list to store data of final balances after the time period
finalBalances = []

for i in range(simulationCount):
    #set initial conditions for time and balance
    time = 0
    balance = 10000

    while time < num_of_years:
        # increase balance and time
        balance += changeInBalance(balance)
        time += 1

    finalBalances.append(balance)


#plot the data
hist(finalBalances, bins=20)
show()