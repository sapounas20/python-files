import numpy as np
import matplotlib.pyplot as plt
c= 3e8
I2 = 1.4e38
Q = 90 #healing parameter
tau_c = 7*7*24*3600 #relaxation time 7 weeks 
tau= (Q/100)*tau_c 
t= np.arange(0,0.2*365,1) #time range

glitch_time = len(t)//5
O = []

for k in t:
    
    if k < glitch_time:
        omega = 33* 2* np.pi* np.exp(-8*10**(-2)*k)
    
    elif k == glitch_time :
        D = 2* omega 
        omega_0 =33* 2* np.pi* np.exp(-8*10**(-2)*k)
        omega= omega_0 + D * (Q/100 *np.exp(-( 24* 3600* k)/(tau))+1- Q/100)
    else:    
        omega_0 = 33* 2* np.pi* np.exp(-8*10**(-2)*k)
        omega= omega_0 + D * (Q/100 *np.exp(-( 24* 3600* k)/(tau))+1- Q/100)

    O.append(omega)

    
    
print(O)


plt.plot(t, O)

plt.xlabel('Time (days)')
plt.ylabel('Angular velocity (r/s)')
plt.title('Crab Pulsar glitch model')
plt.yscale('log')
plt.legend()
plt.show()