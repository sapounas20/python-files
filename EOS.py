import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant (m^3/kg/s^2)
c = 2.99792458e8  # Speed of light (m/s)

# Equation of state (EOS) functions
def eos_polytrope(rho, K, gamma):
    return K * rho ** gamma

def eos_cst(rho, K):
    return K

# Tolman-Oppenheimer-Volkoff (TOV) equations
def tov_equations(rho, m, r, eos_func, *eos_args):
    P = eos_func(rho, *eos_args)
    dp_dr = -(G * (rho + P / c ** 2) * (m + 4 * np.pi * r ** 3 * P / c ** 2)) / (r * (r - 2 * G * m / c ** 2))
    dm_dr = 4 * np.pi * r ** 2 * rho
    return dp_dr, dm_dr

# Integration using Runge-Kutta method
def integrate_tov(eos_func, *eos_args, dr=100, r_max=1e6):
    r = np.arange(dr, r_max + dr, dr)
    rho = np.zeros_like(r)
    m = np.zeros_like(r)
    P = np.zeros_like(r)

    rho[0] = 1e18  # Central density
    m[0] = 0  # Central mass

    for i in range(1, len(r)):
        dp_dr1, dm_dr1 = tov_equations(rho[i - 1], m[i - 1], r[i - 1], eos_func, *eos_args)
        dp_dr2, dm_dr2 = tov_equations(rho[i - 1] + 0.5 * dr * dp_dr1, m[i - 1] + 0.5 * dr * dm_dr1, r[i - 1] + 0.5 * dr,
                                       eos_func, *eos_args)
        dp_dr3, dm_dr3 = tov_equations(rho[i - 1] + 0.5 * dr * dp_dr2, m[i - 1] + 0.5 * dr * dm_dr2, r[i - 1] + 0.5 * dr,
                                       eos_func, *eos_args)
        dp_dr4, dm_dr4 = tov_equations(rho[i - 1] + dr * dp_dr3, m[i - 1] + dr * dm_dr3, r[i - 1] + dr, eos_func,
                                       *eos_args)

        rho[i] = rho[i - 1] + (dr / 6) * (dp_dr1 + 2 * dp_dr2 + 2 * dp_dr3 + dp_dr4)
        m[i] = m[i - 1] + (dr / 6) * (dm_dr1 + 2 * dm_dr2 + 2 * dm_dr3 + dm_dr4)
        P[i] = eos_func(rho[i], *eos_args)

        if rho[i] <= 0 or P[i] <= 0 or m[i] <= 0:
            break

    return r[:i+1], rho[:i+1], m[:i+1], P[:i+1]
