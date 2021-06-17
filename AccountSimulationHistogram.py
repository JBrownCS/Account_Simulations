from matplotlib.pyplot import show, hist
import random


#Change in balance function in case the rate fluctuates; random.uniform makes all outcomes between 2 numbers likely
def changeInBalance(account_balance):
    return account_balance * random.uniform(0, 0.06)


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