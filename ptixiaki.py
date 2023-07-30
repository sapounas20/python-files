import numpy as np
import matplotlib.pyplot as plt

G= G = 6.67430e-11  # Gravitational constant in m^3 kg^(-1) s^(-2)

def I_crust(R_t,P_t,R,):
    #Schwarzschild radius
    ##mass of star
    M= float(input("Enter star's mass in kg: "))
    Rs= 2*G*M

    I= ((16*np.pi())/3 )*(R_t**6 *(P_t/Rs))* (1-(0.21/((R/Rs)-1)))
    return I 

