import numpy as np
import scipy.integrate as spi
import scipy as sp

rho = 1.22  # kg/m^3
A = 0.01  # m^2 ------------must set this - unknown
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
T_avg_1 = t_1 * I_1
M = 3  # kg - total initial mass
mr_1 = 0.50  # empty mass (no motor) of just first stage
me_1 = 0.495  # mass of motor
mp_1 = 0.2472  # propellant mass - kg
mass_boost = mr_1 + me_1 - mp_1 / 2
mass_coast = mr_1 + me_1 - mp_1

# second stage

I_2 = 658  # Ns - impulse
T_max_2 = 512.3  # Newton - max thrust
t_2 = 1.9  # burn time
T_avg_2 = t_2 * I_2
mr_2 = 0.75  # empty mass (no motor)
me_2 = 0.601  # loaded mass
mp_2 = 0.337  # propellant mass - kg


class Calculations:

    @staticmethod
    def one_stage_height(mass_boost, mass_coast, t, T):
        # mass_boost = mass during boost
        # mass_coast = mass during coast
        # t = burn time
        # T = avg motor thrust in Newtons

        q = np.sqrt((T - mass_boost * g) / k)

        x = 2 * k * q / mass_boost

        v = q * (1 - np.exp(-x * t)) / (1 + np.exp(-x * t))

        y_1 = -mass_boost / (2 * k) * np.log((T - mass_boost * g - k * v ** 2) / (T - mass_boost * g))

        y_c = mass_coast / (2 * k) * np.log((mass_coast * g + k * v ** 2) / (mass_coast * g))

        q_a = np.sqrt(mass_coast * g / k)

        q_b = np.sqrt(g * k / mass_coast)

        t_a = np.arctan(v / q_a) / q_b  # coasting time (motor delay)

        return t_a, v, y_1 + y_c

    @staticmethod
    def two_stage_height(mr_1, me_1, mp_1, mr_2, me_2, mp_2, t, T):
        mass_boost = mr_1 + mr_2 + me_1 + me_2 + mp_2 - mp_1 / 2
        # mass_first_stage = me_1
        # t = array of burn times
        # T = array of avg motor thrust in Newtons

        # first stage
        q = np.sqrt((T[0] - mass_boost * g) / k)

        x = 2 * k * q / mass_boost

        v = q * (1 - np.exp(-x * t[0])) / (1 + np.exp(-x * t[0]))

        y_1 = -mass_boost / (2 * k) * np.log((T[0] - mass_boost * g - k * v ** 2) / (T[0] - mass_boost * g))

        # second stage
        v_0 = v  # set new velocity to old velocity
        m = mass_boost - mr_1 - me_2 - mp_1 - mp_2 / 2

        q = np.sqrt((T[1] - m * g) / k)

        x = 2 * k * q / m

        s = (q + v_0) / (q - v_0)

        v = q * (s - np.exp(-x * t[1])) / (s + np.exp(-x * t[1]))

        y_2 = -m / (2 * k) * np.log((T[1] - m * g - k * v ** 2) / (T[1] - m * g - k * v_0 ** 2))

        # coasting phase
        m = me_2 + mr_2 - mp_2

        y_c = m / (2 * k) * np.log((m * g + k * v ** 2) / (m * g))

        q_a = np.sqrt(m * g / k)

        q_b = np.sqrt(g * k / m)

        t_a = np.arctan(v / q_a) / q_b  # coasting time (motor delay)

        return t_a, v, y_1 + y_2 + y_c


t_a, v, height = Calculations.one_stage_height(mass_boost, mass_coast, t_1, T_avg_1)
print(t_a, v, height)

t = [t_1, t_2]
T = [T_avg_1, T_avg_2]

t_a, v, height = Calculations.two_stage_height(mr_1, me_1, mp_1, mr_2, me_2, mp_2, t, T)
print(t_a, v, height)
