import numpy as np

class Calculations:

    @staticmethod
    def one_stage_height(mass_boost, mass_coast, t, T, g, k):
        # mass_boost = mass during boost
        # mass_coast = mass during coast
        # t = burn time
        # T = avg motor thrust in Newtons
        # g = gravitational acceleration

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
    def two_stage_height(mr_1, me_1, mp_1, mr_2, me_2, mp_2, t, T, g, k):
        # mr_1 = empty mass (no motor) of first stage
        # me_1 = loaded mass of engine in first stage
        # mp_1 = mass of propellant in first stage engine
        # mr_2 = empty mass (no motor) of just second stage
        # me_2 = loaded mass of engine in second stage
        # mp_2 = mass of propellant in second stage engine
        # t = array of burn times, first entry = first engine burn time etc
        # T = array of avg thrust, first entry = first engine thrust avg etc
        # g = gravitational acceleration
        # k = drag resistance factor

        mass_boost = mr_1 + mr_2 + me_1 + me_2 + mp_2 - mp_1 / 2

        # first stage
        q = np.sqrt((T[0] - mass_boost * g) / k)

        x = 2 * k * q / mass_boost

        v = q * (1 - np.exp(-x * t[0])) / (1 + np.exp(-x * t[0]))

        y_1 = -mass_boost / (2 * k) * np.log((T[0] - mass_boost * g - k * v ** 2) / (T[0] - mass_boost * g))

        # second stage
        v_0 = v  # set new velocity to old velocity
        m = mr_2 + me_2 - mp_2 / 2

        q_new = np.sqrt((T[1] - m * g) / k)

        x_new = 2 * k * q_new / m

        s = (q_new + v_0) / (q_new - v_0)

        v = q_new * ((s - np.exp(-x_new * t[1])) / (s + np.exp(-x_new * t[1])))

        y_2 = -m / (2 * k) * np.log((T[1] - m * g - k * v ** 2) / (T[1] - m * g - k * v_0 ** 2))

        # coasting phase
        m = me_2 + mr_2 - mp_2

        y_c = m / (2 * k) * np.log((m * g + k * v ** 2) / (m * g))

        q_a = np.sqrt(m * g / k)

        q_b = np.sqrt(g * k / m)

        t_a = np.arctan(v / q_a) / q_b  # coasting time (motor delay)


        return t_a, v, v_0, y_1 + y_2 + y_c

    @staticmethod
    def ODEints():
        pass