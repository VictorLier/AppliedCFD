import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import os

# Collect all csv files in the foler:
data_path = "LidDrivenVelocityprofile\Ex2"
txt_path = "LidDrivenVelocityprofile\plot_files"

# Reference data:
# y_exact = np.array([0.0000, 0.0625, 0.1016, 0.2813, 0.5000, 0.7344, 0.9531, 0.9688, 1.0000])
# u_exact = np.array([0.0000, -0.20227, -0.30029, -0.28040, -0.06205, 0.18861, 0.47239, 0.58031, 1.000])
y_exact = np.array([0.0625, 0.1016, 0.2813, 0.5000, 0.7344, 0.9531, 0.9688])
u_exact = np.array([-0.20227, -0.30029, -0.28040, -0.06205, 0.18861, 0.47239, 0.58031])

np.savetxt(os.path.join(txt_path, f'reference.txt'), np.array([y_exact, u_exact]).T, delimiter=' ')


files = os.listdir(data_path)
files = [f for f in files if f.endswith('.csv')]
# files = ["51_3402.csv", "101_9427.csv", "201_27888.csv"]

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
    u = data[1:, 0][1:-1]
    y = data[1:, 1][1:-1]

    # Remove duplicate values:
    u, indices = np.unique(u, return_index=True)
    y = y[indices]

    interp = sp.interpolate.interp1d(y, u, kind='cubic', fill_value='extrapolate')

    # Compare the data with the reference data using Root Mean Square Error (RMSE):
    u_simulated = interp(y_exact)
    rmse = np.mean(np.sqrt((u_exact - u_simulated)**2))

    N.append(n)
    N_iter.append(i)
    RMSE.append(rmse)

    # Save data in txt file:
    np.savetxt(os.path.join(txt_path, f'{n}_{i}_simulation.txt'), np.array([y, u]).T, delimiter=' ')
    np.savetxt(os.path.join(txt_path, f'{n}_{i}_interp.txt'), np.array([y_exact, u_simulated]).T, delimiter=' ')

    if True:
        plt.figure()
        plt.title(f'N = {n}, iterations = {i}, RMSE = {rmse:.4f}')
        plt.scatter(y, u, alpha=0.7, color = 'lightgrey', label='Data')
        plt.plot(y_exact, u_exact, "o-", label='Reference')
        plt.plot(y_exact, u_simulated, "o-", label='Simulation', mfc='none')
        plt.legend()
        plt.grid()
        plt.xlabel('y')
        plt.ylabel('u')


# Find the slope of the RMSE vs. N plot:
slope = np.polyfit(np.log(N), np.log(RMSE), 1)[0]

if len(N) > 0:
    np.savetxt(os.path.join(txt_path, f'convergence.txt'), np.array([N, RMSE]).T, delimiter=' ')
    plt.figure()
    scatter = plt.scatter(N, RMSE, c=N_iter, cmap='viridis', edgecolor='k', s=100)
    plt.colorbar(scatter, label='Number of Iterations')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which='both', ls='--')
    plt.xlabel('N')
    plt.ylabel('RMSE')
    plt.title('RMSE vs. Grid Points (N): Slope = {:.2f}'.format(slope))


plt.show()