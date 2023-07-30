import math as m
def M(delta_c, a_c,delta_0, a_0 ):
 
    return(m.sqrt((delta_0 - delta_c)**2 +(a_0*m.cos(delta_0)-a_c*m.cos(delta_c))**2))

m= M()

print(m)
