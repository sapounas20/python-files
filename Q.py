import numpy as np
import matplotlib.pyplot as plt
import math

I1 = 1.4* 1.9885 * 10**30 * 10**8 * 0.4
I2 = 1.5 *10**45 / 1000 /10000
braking_index = 5  # Braking index


Q = np.array([0.9, 1.6, 1.5, 1.2, 1.2, 1.5, 1, 1.8, 1.2, 2.7, 0.5])
tau_c = np.array([4.93, 11.3, 43.6, 12.1, 20.6, 15.5, 58.4, 15.8, 21.5, 38.8, 10.5]) #kyr

t= np.arange(0, 70, 1)
glitch_time = len(t)//3

tau= []
for i in range(len(Q)):
    res= tau_c[i] * Q[i]/100
    tau.append(res)

tau= np.array(tau)
O = []
for j in range(len(tau)):
    values= []
    for k in range(len(t)):
        D= 0
        if k <= glitch_time:
            omega = 1000* 2* np.pi- braking_index * 24* 3600* t[k]/ 2000
        else:
            D += omega * 1.25 - omega
        
            omega_0 = 1000* 2* np.pi- braking_index * 24* 3600* t[k]/ 5000
            omega= omega_0 + D * (Q[j]/100 *math.exp(-( 24* 3600* t[k])/( 3*365 *24* 3600* tau[j]))+1- Q[j]/100)

        values.append(omega)
    
    O.append(values)



for j in range(len(O)):
    plt.plot(t, O[j], label=f'Set {j + 1}')

plt.xlabel('Time')
plt.ylabel('Omega')
plt.title('Omega vs Time for Different Sets')
plt.legend()
plt.show()