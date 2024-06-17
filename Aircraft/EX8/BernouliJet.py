
D = 7.780472e+01 # N

U_engine = 2.194092e+02 # m/s

mass_flow = 1.113397e+00 # kg/s

A_engine = 2.742688e-03 # m^2

A_manifold = 5.824548e-03 # m^2

A_nozzle = 2.323672e-02 # m^2

p_inf = 101325 # Pa

R_gas = 287 # J/kgK

rho = 1.2 # kg/m^3

U_inf = 100 # m/s

p_engine = 1/2 * rho * U_inf**2 * (1 - (A_manifold/A_engine)**2)

U_nozzle = D / mass_flow + U_engine * (A_engine / A_manifold)

rho_nozzle = mass_flow / (A_nozzle * U_nozzle)

T_nozzle = p_inf / (rho_nozzle * R_gas)

print("The exit velocity is", U_nozzle, "m/s")
print("The exit density is", rho_nozzle, "kg/m^3")
print("The exit temperature is", T_nozzle, "K")