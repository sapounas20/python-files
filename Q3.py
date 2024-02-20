import numpy as np
import matplotlib.pyplot as plt
Q = 90 #healing parameter
tau_c = 7*7*24*3600 #relaxation time 7 weeks 
tau= (Q/100)*tau_c 
t= np.arange(47,247,1) #time range

glitch_time = t[len(t)//4]
O = []

for k in t:
    
    if k < glitch_time:
        omega = 1/np.sqrt(29*10**(-4)+19.152*10**(10)*k)
    
    elif k == glitch_time :
        D =2*np.pi*1.071*10**(-7)
        omega_0 =1/np.sqrt(29*10**(-4)+19.152*10**(10)*k)
        omega= omega_0 + D * (Q/100 *np.exp(-( 24* 3600* k)/(tau))+1- Q/100)
    else:    
        omega_0 = 1/np.sqrt(29*10**(-4)+19.152*10**(10)*k)
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