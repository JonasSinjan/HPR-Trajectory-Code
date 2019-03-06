import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

rho = 1.22  # kg/m^3
A = 2.552 * 10 ** -3  # m^2 frontal area
Cd = 0.75  # air drag coefficient
g = 9.8  # m/s^2
k = 0.5 * rho * Cd * A  # drag resistance factor


def model(t, z):
    rho = 1.22
    A = 2.552 * 10 ** -3
    C_d = 0.75
    mdot = 0.1915  # kg/s - mass flow rate
    u_e = 1947.8  # m/s

    h = z[0] #initial values
    v = z[1]
    m = z[2]

    dhdt = v
    dvdt = - 9.81 - (0.5 * rho * v * np.abs(v) * C_d * A) / m + (v * mdot * u_e) / (np.abs(v) * m)
    dmdt = - mdot
    return [dhdt, dvdt, dmdt]


m_init = 4.6  # kg

# initial conditions
z0 = [0, 0, 4.6]

t = np.linspace(0, 1000, 1000)

sol = spi.solve_ivp(model, (0, 1), z0)

print(sol.z)