from functions import *

#drag factor calculation
rho = 1.22  # kg/m^3
A = 0.01  # m^2 ----------UNKNOWN GUESS ATM
Cd = 0.75
g = 9.8  # m/s^2

k = 0.5 * rho * Cd * A  # wind resistance factor


# first stage data

I_1 = 540  # Newton-seconds
T_max_1 = 555.2  # Newton - max thrust
t_1 = 1.1  # burn time
T_avg_1 = t_1 * I_1
M = 3  # kg - total initial mass
mr_1 = 0.50  # empty mass (no motor) of just first stage -----UNKNOWN GUESS ATM
me_1 = 0.495  # mass of motor
mp_1 = 0.2472  # propellant mass - kg
mass_boost = mr_1 + me_1 - mp_1 / 2
mass_coast = mr_1 + me_1 - mp_1

# second stage data

I_2 = 658  # Ns - impulse
T_max_2 = 512.3  # Newton - max thrust
t_2 = 1.9  # burn time
T_avg_2 = t_2 * I_2
mr_2 = 0.75  # empty mass (no motor) ------UNKNOWN GUESS ATM
me_2 = 0.601  # loaded mass
mp_2 = 0.337  # propellant mass - kg


# just using bottom motor and no staging
t_a, v, height = Calculations.one_stage_height(mass_boost, mass_coast, t_1, T_avg_1, g, k)
print(t_a, v, height)


# two stage with no delay of staging between first and second
t = [t_1, t_2]
T = [T_avg_1, T_avg_2]

t_a, v, height = Calculations.two_stage_height(mr_1, me_1, mp_1, mr_2, me_2, mp_2, t, T, g, k)
print(t_a, v, height)
