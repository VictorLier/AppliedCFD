import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import os

# Collect all csv files in the foler:
data_path = "LidDrivenVelocityprofile"
txt_path = "LidDrivenVelocityprofile\plot_files"

# Reference data:
y_exact = np.array([0.0000, 0.0625, 0.1016, 0.2813, 0.5000, 0.7344, 0.9531, 0.9688, 1.0000])
u_exact = np.array([0.0000, -0.20227, -0.30029, -0.28040, -0.06205, 0.18861, 0.47239, 0.58031, 1.000])

np.savetxt(os.path.join(txt_path, f'reference.txt'), np.array([u_exact, y_exact]).T, delimiter=' ')


files = os.listdir(data_path)
files = [f for f in files if f.endswith('.csv')]
# Sort the files based on the number of grid points. The files names are e.g. 400_1000 where 400 is the number of grid points and 1000 is the number of iterations. We sort based on the number of grid points:
files.sort(key=lambda x: int(x.split("_")[0]))

# Read the data from the csv files:
N = []
N_iter = []
RMSE = []
for file in files:
    data = np.genfromtxt(data_path + '/' + file, delimiter=',')
    n = int(file.split("_")[0])
    i = int(file.split("_")[1].split(".")[0])
    u = data[1:, 0]
    y = data[1:, 1]

    # Remove duplicate values:
    y, indices = np.unique(y, return_index=True)
    u = u[indices]

    interp = sp.interpolate.interp1d(y, u, kind='cubic', fill_value='extrapolate')

    # Compare the data with the reference data using Root Mean Square Error (RMSE):
    u_simulated = interp(y_exact)
    rmse = np.sqrt(np.mean((u_exact - u_simulated)**2))

    N.append(n)
    N_iter.append(i)
    RMSE.append(rmse)

    # Save data in txt file:
    np.savetxt(os.path.join(txt_path, f'{n}_{i}_simulation.txt'), np.array([u, y]).T, delimiter=' ')
    np.savetxt(os.path.join(txt_path, f'{n}_{i}_interp.txt'), np.array([u_simulated, y_exact]).T, delimiter=' ')

    if True:
        plt.figure()
        plt.title(f'N = {n}, iterations = {i}, RMSE = {rmse:.4f}')
        plt.scatter(u, y, alpha=0.7, color = 'lightgrey', label='Data')
        plt.plot(u_exact, y_exact, "o-", label='Reference')
        plt.plot(u_simulated, y_exact, "o-", label='Simulation', mfc='none')
        plt.legend()
        plt.grid()
        plt.xlabel('u')
        plt.ylabel('y')

if len(N) > 0:
    plt.figure()
    plt.loglog(N, RMSE, 'o')
    plt.grid()
    plt.xlabel('N')
    plt.ylabel('RMSE')

plt.show()