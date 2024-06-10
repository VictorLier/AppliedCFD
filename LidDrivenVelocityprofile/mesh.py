import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import os

# Collect all csv files in the foler:
data_path = "LidDrivenVelocityprofile\Ex3"
txt_path = "LidDrivenVelocityprofile\plot_files_Ex3"

# Reference data:
# y_exact = np.array([0.0000, 0.0625, 0.1016, 0.2813, 0.5000, 0.7344, 0.9531, 0.9688, 1.0000])
# u_exact = np.array([0.0000, -0.20227, -0.30029, -0.28040, -0.06205, 0.18861, 0.47239, 0.58031, 1.000])
y_exact = np.array([0.0625, 0.1016, 0.2813, 0.5000, 0.7344, 0.9531, 0.9688])
u_exact = np.array([-0.20227, -0.30029, -0.28040, -0.06205, 0.18861, 0.47239, 0.58031])

np.savetxt(os.path.join(txt_path, f'reference.txt'), np.array([y_exact, u_exact]).T, delimiter=' ')


files = os.listdir(data_path)
files = [f for f in files if f.endswith('.csv')]
# files = ["51_3402.csv", "101_9427.csv", "201_27888.csv"]

# Read the data from the csv files:
names = []
N_iter = []
RMSE = []
for file in files:
    data = np.genfromtxt(data_path + '/' + file, delimiter=',')
    name = str(file.split("_")[0])
    i = int(file.split("_")[1].split(".")[0])
    u = data[1:, 0][1:-1]
    y = data[1:, 1][1:-1]

    # Remove duplicate values:
    u, indices = np.unique(u, return_index=True)
    y = y[indices]

    interp = sp.interpolate.interp1d(y, u, kind='cubic', fill_value='extrapolate')

    # Compare the data with the reference data using Root Mean Square Error (RMSE):
    u_simulated = interp(y_exact)
    rmse = np.mean(np.sqrt((u_exact - u_simulated)**2))

    names.append(name)
    N_iter.append(i)
    RMSE.append(rmse)

    # Save data in txt file:
    np.savetxt(os.path.join(txt_path, f'{name}_{i}_simulation.txt'), np.array([y, u]).T, delimiter=' ')
    np.savetxt(os.path.join(txt_path, f'{name}_{i}_interp.txt'), np.array([y_exact, u_simulated]).T, delimiter=' ')

    if True:
        plt.figure()
        plt.title(f'Method = {name}, iterations = {i}, RMSE = {rmse:.4f}')
        plt.scatter(y, u, alpha=0.7, color = 'lightgrey', label='Data')
        plt.plot(y_exact, u_exact, "o-", label='Reference')
        plt.plot(y_exact, u_simulated, "o-", label='Simulation', mfc='none')
        plt.legend()
        plt.grid()
        plt.xlabel('y')
        plt.ylabel('u')

plt.show()