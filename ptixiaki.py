import numpy as np
import matplotlib.pyplot as plt

m = 1.674927471 * 10** -27 #neutron mass, kg
M = np.arange(0.7, 2.1, 0.1).tolist()#pulsar mass, solar masses
R =10000  #pulsar radius, m
c = 3*10**8 #speed of light, m/s
G = 6.6743 * 10** -11


MDI1 = np.array([(0.070, 0.232), (0.086, 0.425), (0.084, 0.488), (0.082, 0.365), (0.080, 0.339), (0.077, 0.322), (0.077, 0.309)])
MDI2 = np.array([(0.064, 0.212), (0.082, 0.483), (0.083, 0.458), (0.079, 0.413), (0.077, 0.380), (0.075, 0.354), (0.074, 0.334)])
MDI3 = np.array([(0.060, 0.181), (0.082, 0.529), (0.082, 0.492), (0.078, 0.441), (0.076, 0.396), (0.074, 0.363), (0.072, 0.337)])
MDI4 = np.array([(0.050, 0.075), (0.084, 0.615), (0.084, 0.602), (0.079, 0.479), (0.075, 0.400), (0.072, 0.347), (0.069, 0.309)])
MDI5 =  np.array([(0.055, 0.157), (0.082, 0.641), (0.083, 0.618), (0.078, 0.524), (0.075, 0.457), (0.072, 0.409), (0.070, 0.374)])
MDI6 =  np.array([(0.047, 0.039), (0.085, 0.656), (0.086, 0.670), (0.079, 0.508), (0.075, 0.408), (0.072, 0.343), (0.069, 0.298)])
MDI7 = np.array([(0.042, 0.016), (0.088, 0.804), (0.090, 0.919), (0.085, 0.699), (0.077, 0.488), (0.072, 0.392), (0.069, 0.325)])
HLPS1 = np.array([(0.079, 0.415), (0.087, 0.525), (0.087, 0.509), (0.085, 0.493), (0.084, 0.478), (0.083, 0.466), (0.082, 0.457)])
HLPS2 = np.array([(0.091, 0.339), (0.093, 0.366), (0.094, 0.403), (0.093, 0.376), (0.092, 0.376), (0.091, 0.371), (0.090, 0.399)])
SKI4 = np.array([(0.073, 0.248), (0.082, 0.356), (0.082, 0.343), (0.080, 0.327), (0.079, 0.314), (0.078, 0.304), (0.077, 0.296)])
SKa = np.array([(0.069, 0.377), (0.082, 0.622), (0.083, 0.580), (0.080, 0.553), (0.078, 0.520), (0.077, 0.494), (0.075, 0.474)])
Sly4 = np.array([(0.080, 0.365), (0.085, 0.427), (0.085, 0.411), (0.083, 0.405), (0.083, 0.398), (0.082, 0.392), (0.082, 0.387)])

models = np.array([MDI1, MDI2, MDI3, MDI4, MDI5, MDI6, MDI7, HLPS1, HLPS2, SKI4, SKa, Sly4])

Ic_I = []

for i in range(len(models)):
    model = []
    for j in range(len(models[i])):
        row = []
        for l in range(len(M)):
            beta = G * 1.9885 * 10**30 * M[l] / (R * c**2)

            res = (28 * np.pi * models[i][j][1] * 1.60218 * 10**32 * R**3 /
                    (3 * 1.9885 * 10**30 * M[l] * c**2) *
                    (1 - 1.67 * beta - 0.6 * beta**2) / beta *
                    (1 + (2 * models[i][j][1] * 1.60218 * 10**32) /
                    (models[i][j][0] * 10**45 * m * c**2) *
                    (1 + 5 * beta - 14 * beta**2) / beta**2))
            row.append(res)
        model.append(row)
    Ic_I.append(model)


print(Ic_I)
Ic_I= np.array(Ic_I)


for model_index, model_data in enumerate(Ic_I):
    fig, ax = plt.subplots()
    for j, M_data in enumerate(model_data):
        ax.plot(M, M_data, label=f'Data {j + 1}')
    ##################################################### 0.07 line 
    ax.axhline(y=0.07, color='r', linestyle='--')
    
    ax.annotate('0.07', xy=(M[0], 0.07), xytext=(M[0], 0.08),
                )
    
    ax.fill_between(M, 0.07, 1, color='green', alpha=0.1)
    ax.annotate('Allowed', xy=(2, 0.071), xytext=(1.9, 0.08),
                )
    
    ax.fill_between(M, 0, 0.07, color='red', alpha=0.1)
    ax.annotate('Forbidden', xy=(2, 0.065), xytext=(1.9, 0.05),
                )
    ###################################################### 0.016 line 
    ax.axhline(y=0.016, color='r', linestyle='--')
    ax.annotate('0.016', xy=(M[0], 0.016), xytext=(M[0], 0.02),
                )
    
    ax.fill_between(M, 0.016, 1, color='blue', alpha=0.1)
    ax.annotate('Allowed', xy=(2, 0.18), xytext=(1.9, 0.02),
                )
    
    ax.fill_between(M, 0, 0.016, color='yellow', alpha=0.1)
    ax.annotate('Forbidden', xy=(2, 0.01), xytext=(1.9, -0.02))

    ax.set_ylim(0, 0.5)
                

    ax.set_xlabel('Pulsar Mass (Solar Masses)')

    ax.set_ylabel('Ic/I')

    

    ax.legend()
    plt.show()

