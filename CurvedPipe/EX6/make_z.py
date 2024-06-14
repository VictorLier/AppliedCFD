import numpy as np
import matplotlib.pyplot as plt
import os 

# Collect all csv files in the foler:
data_path = "CurvedPipe\EX6"
txt_path = "CurvedPipe\EX6"

files = os.listdir(data_path)
files = [f for f in files if f.endswith('.csv')]
files = ["Pressure.csv", "Pressure_KOmega.csv", "Pressure_Spalart.csv"]
# files = ["Pressure_Spalart.csv"]

D = 0.104

for file in files:
    data = np.genfromtxt(data_path + '/' + file, delimiter=',')
    name = str(file.split(".")[0])
    if name == "Pressure":
        p_ref = 2.152536e-1
    elif name == "Pressure_KOmega":
        p_ref = 1.898333e-1
    elif name == "Pressure_Spalart":
        p_ref = 2.114314e-1
    else:
        p_ref = 0
    data = data[1:]

    data = data[np.lexsort((data[:, 3], data[:, 1]))]

    p = data[:, 0]
    x = data[:, 1]
    y = data[:, 2]
    z = data[:, 3]

    x_max = np.max(x)

    x_arg_min = np.argsort(x)
    z_args = z[x_arg_min]
    z_arg_min = np.argmin(z_args)
    arg_min = x_arg_min[z_arg_min]

    outer_args = [arg_min]

    while True:
        # Find the closest point to the last point in the list:
        _l = np.sqrt((x - x[outer_args[-1]])**2 + (z - z[outer_args[-1]])**2)
        __arg = np.argsort(_l)
        _arg = [arg for arg in __arg if arg not in outer_args]
        arg = _arg[0]
        outer_args.append(arg)

        if x[arg] >= x_max-0.001:
            break

    x_outer = x[outer_args]
    z_outer = z[outer_args]
    p_outer = p[outer_args]


    z_arg_min = np.argsort(z)
    x_args = x[z_arg_min]
    x_arg_min = np.argmax(x_args[:15])
    arg_min = z_arg_min[x_arg_min]

    inner_args = [arg_min]

    while True:
        # Find the closest point to the last point in the list:
        _l = np.sqrt((x - x[inner_args[-1]])**2 + (z - z[inner_args[-1]])**2)
        __arg = np.argsort(_l)
        _arg = [arg for arg in __arg if arg not in inner_args]
        arg = _arg[0]
        inner_args.append(arg)

        if x[arg] >= x_max-0.001:
            break


    x_inner = x[inner_args]
    z_inner = z[inner_args]
    p_inner = p[inner_args]

    # x_inner = np.delete(x, outer_args)
    # z_inner = np.delete(z, outer_args)
    # p_inner = np.delete(p, outer_args)

    # # sort inner first by x, then by z:
    # args = np.lexsort((z_inner, x_inner))
    # x_inner = x_inner[args]
    # z_inner = z_inner[args]
    # p_inner = p_inner[args]

    plt.figure(figsize=(5, 5))
    plt.plot(x_outer, z_outer, color='black')
    plt.plot(x_inner, z_inner, color='red')
    # plt.show()

    l_outer = np.zeros_like(x_outer)
    l_inner = np.zeros_like(x_inner)
    
    for i in range(1, len(x_outer)):
        for j in range(2, i):
            l_outer[i] += np.sqrt((x_outer[j] - x_outer[j-1])**2 + (z_outer[j] - z_outer[j-1])**2)
            l_inner[i] += np.sqrt((x_inner[j] - x_inner[j-1])**2 + (z_inner[j] - z_inner[j-1])**2)

    # np.savetxt(os.path.join(txt_path, f'{name}_norm.txt'), np.array([r, u]).T, delimiter=' ')

    l_outer -= 1
    l_outer /= D
    l_inner -= 1
    l_inner /= D

    cp_outer = (p_outer-p_ref)/(1/2)
    cp_inner = (p_inner-p_ref)/(1/2)

    np.savetxt(os.path.join(txt_path, f'{name}_outer.txt'), np.array([l_outer, cp_outer]).T, delimiter=' ')
    np.savetxt(os.path.join(txt_path, f'{name}_inner.txt'), np.array([l_inner, cp_inner]).T, delimiter=' ')

    if True:
        plt.figure()
        plt.title(f'Method = {name}')
        plt.scatter(l_outer, cp_outer, alpha=0.7, color = 'lightgrey', label='Outer')
        plt.scatter(l_inner, cp_inner, alpha=0.7, color = 'red', label='Inner')
        plt.legend()
        plt.grid()
        plt.xlabel('y/D')
        plt.ylabel('u')

plt.show()