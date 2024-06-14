import numpy as np
import matplotlib.pyplot as plt
import os

# Collect all csv files in the foler:
data_path = "CurvedPipe\EX6"
txt_path = "CurvedPipe\EX6"

files = os.listdir(data_path)
files = [f for f in files if f.endswith('.csv')]
files = ["Velocity.csv", "Velocity_KOmega.csv", "Velocity_Spalart.csv"]

D = 0.104

for file in files:
    data = np.genfromtxt(data_path + '/' + file, delimiter=',')
    name = str(file.split(".")[0])
    r = data[1:, 0]
    u = data[1:, 1]

    # Remove duplicate values:
    r, indices = np.unique(r, return_index=True)
    u = u[indices]
    
    # Normalize the data by subtracting the median value:
    r -= r[0]+D/2
    r /= D/2 

    np.savetxt(os.path.join(txt_path, f'{name}_norm.txt'), np.array([r, u]).T, delimiter=' ')

    if True:
        plt.figure()
        plt.title(f'Method = {name}')
        plt.scatter(r, u, alpha=0.7, color = 'lightgrey', label='Data')
        plt.legend()
        plt.grid()
        plt.xlabel('y/D')
        plt.ylabel('u')

plt.show()
