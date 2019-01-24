import numpy as np
import scipy.integrate as spi
import scipy as sp

rho = 1.22  # kg/m^3
A = 0.005 # m^2 ------------must set this - unknown
Cd = 0.75
g = 9.8  # m/s^2

k = 0.5 * rho * Cd * A  # wind resistance factor

# mr = empty-no motor mass of rocket
# me = loaded mass of rocket
# mp = mass of propellant

# first stage

I_1 = 540  # Newton-seconds
T_max_1 = 555.2  # Newton - max thrust
t_1 = 1.1  # burn time
T_avg = t_1*I_1
M = 3  # kg - total initial mass
mr = 1  #empty mass (no motor)
me = 1.2472  #loaded mass
mp = 0.2472  #propellant mass - kg
mass_boost = mr + me - mp/2
mass_coast = mr + me - mp

# second stage

I_2 = 658  # Ns - impulse
T_max_2 = 512.3  # Newton - max thrust
t_2 = 1.9  # burn time
#M_2 = 2  # kg - wet mass of second stage
mr = 1.5 #empty mass (no motor)
me = 2 #loaded mass
mp = 0.337  #propellant mass - kg
M_2 = mr + me - mp/2

class Calculations:

    @staticmethod
    def height(mass_boost, mass_coast, t, T):
        # mass_boost = mass during boost
        # mass_coast = mass during coast
        # T - motor thrust in Newtons

        q = np.sqrt((T-mass_boost*g)/k)

        x = 2*k*q/mass_boost

        v = q * (1-np.exp(-x*t))/(1+np.exp(-x*t))

        y_1 = -mass_boost/(2*k)*np.log((T-mass_boost*g-k*v**2)/(T-mass_boost*g))

        y_c = mass_coast/(2*k)*np.log((mass_coast*g+k*v**2)/(mass_coast*g))

        q_a = np.sqrt(mass_coast*g/k)

        q_b = np.sqrt(g*k/mass_coast)

        t_a = np.arctan(v/q_a)/q_b  #coasting time (motor delay)

        return t_a, y_1+y_c


    @staticmethod
    def ODEint():
        pass


t_a, height = Calculations.height(mass_boost, mass_coast, t_1, T_avg)
print(t_a, height)