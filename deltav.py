import numpy as np
import scipy as sp

rho = 1.2  # kg/m^3
A = 1  # m^2
Cd = 0.75
g = 9.8  # m/s^2

k = 0.5 * rho * Cd * A  # wind resistance factor


q_1 = np.sqrt(T_max_1 * 2 / 3 - M_1 * g) / k
x = 2 * k * q_1 / M_1

dv_1 = q_1 * (1 - np.exp(-x * t_1)) / (1 + np.exp(-x * t_1))
print(dv_1)  # m/s
print(dv_1 * 3.6)  # kmh
var = (T_max_1 * 2 / 3 - M_1 * g - k *dv_1 ** 2) / (T_max_1 * 2 / 3 - M_1 * g)
print(var)
yb = (-M_1 / (2 * k)) * np.log((T_max_1 * 2 / 3 - M_1 * g - k * dv_1 ** 2) / (T_max_1 * 2 / 3 - M_1 * g))
yc = (+M_1 / (2 * k)) * np.log((M_1 * g + k * dv_1 ** 2) / (M_1 * g))

alt = yb + yc
print(alt)
