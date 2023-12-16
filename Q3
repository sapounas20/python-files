import numpy as np
import matplotlib.pyplot as plt
c= 3e8
I2 = 1.4e38
a = 5* I2 * (10**(-9))**2 / (3*c**3) # Braking index
Q = 90
tau = 7*7*24*3600
tC= np.arange(0,0.5*365,1)

glitch_time = len(tC)//2
O = []

for k in tC:
    
    if k < glitch_time:
        omega = 33* 2* np.pi- (a * 24* 3600* k)/ I2
    
    elif k == glitch_time :
        D = 0.5* omega 
        omega_0 = 33* 2* np.pi- (a * 24* 3600* k)/ I2
        omega= omega_0 + D * (Q/100 *np.exp(-( 24* 3600* k)/(tau))+1- Q/100)
    else:    
        omega_0 = 33* 2* np.pi- (a * 24* 3600* k)/ I2
        omega= omega_0 + D * (Q/100 *np.exp(-( 24* 3600* k)/(tau))+1- Q/100)

    O.append(omega)

    
    
print(O)


plt.plot(tC, O)

plt.xlabel('Time')
plt.ylabel('Omega')
plt.title('Omega vs Time for Different Sets')
plt.yscale('log')
plt.legend()
plt.show()