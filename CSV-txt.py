import numpy as np

dataLocation = 'LidDrivenEX4/2order-residuals'
dataName = '2order-residuals.csv'

# Load the data
collumnNames = np.loadtxt(dataLocation + '/' + dataName, delimiter=',', max_rows=1, dtype=str)
collumnNames = np.char.strip(collumnNames, '"')
collumnNames = [col.split(':')[0] for col in collumnNames]
print(collumnNames)
data = np.loadtxt(dataLocation + '/' + dataName, delimiter=',', skiprows=1)

for i, name in enumerate(collumnNames):
    printData = data[:, [0, i]]
    np.savetxt(dataLocation + '/' + name + '.txt', printData)