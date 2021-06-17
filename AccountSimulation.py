from matplotlib.pyplot import show, plot, axis, legend
import random

#Initial Conditions
time = 0
balance = 1000
#Set list to store data
timeList = [time]
balanceList = [balance]

while time < 10:
    #increase balance and time
    balance += balance * 0.03
    time += 1
    timeList.append(time)
    balanceList.append(balance)

#output model results
for i in range(len(timeList)):
    print("Year: " + str(timeList[i]) + " Balance: " + str(balanceList[i]))

#plot the data
plot(timeList, balanceList, label="Balance Simulation", marker="x", markeredgecolor="green")
legend()
show()