from functions import *

#drag factor calculation
rho = 1.22  # kg/m^3
A = 2.552*10**-3 # m^2 ---------- UNKNOWN GUESS ATM
Cd = 0.75  # air drag coefficient
g = 9.8  # m/s^2

k = 0.5 * rho * Cd * A  # drag resistance factor


# first stage data

I_1 = 540  # Impulse (Newton-seconds)
T_max_1 = 555.2  # max thrust (Newton)
t_1 = 1.1  # burn time (seconds)
T_avg_1 = t_1 * I_1 * 0.8  # avg thrust (Newtons)
mr_1 = 1.5  # empty mass (no motor) of just first stage (kg) ----- UNKNOWN GUESS ATM
me_1 = 0.495  # loaded mass of motor (kg)
mp_1 = 0.2472  # propellant mass (kg)
mass_boost = mr_1 + me_1 - mp_1 / 2
mass_coast = mr_1 + me_1 - mp_1

# second stage data

I_2 = 658  # Impulse (Newton-seconds)
T_max_2 = 512.3  # max thrust (Newton)
t_2 = 1.9  # burn time (seconds)
T_avg_2 = t_2 * I_2 * 0.8  # avg thrust (Newtons)
mr_2 = 2  # empty mass (no motor) (kg) ------ UNKNOWN GUESS ATM
me_2 = 0.601  # loaded mass  (kg)
mp_2 = 0.337  # propellant mass (kg)


# # just using bottom motor and no staging
# t_a, v, height = Calculations.one_stage_height(mass_boost, mass_coast, t_1, T_avg_1, g, k)
# print("Just One stage motor firing - no separation")
# print(f"The calculated coast time is {t_a} s")
# print(f"The max velocity is {v} m/s")
# print(f"The peak altitude is {height} m")
# print("-")

# two stage with no delay of staging between first and second
t = [t_1, t_2]
T = [T_avg_1, T_avg_2]

t_a, v, v_0, height = Calculations.two_stage_height(mr_1, me_1, mp_1, mr_2, me_2, mp_2, t, T, g, k)
print("Two stage rocket")
print(f"The calculated coast time is {t_a} s")
print(f"The max velocity is {v} m/s")
print(f"The dv after the first stage is {v_0} m/s")
print(f"The peak altitude is {height} m")

