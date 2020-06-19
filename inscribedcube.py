import numpy as np
import matplotlib.pyplot as plt

pi=np.pi
r=1
theoretical_solution=[pi*r**2,4.0*pi*r**3/3.0,0.5*r**4*pi**2,8.0*pi**2*r**5/15.0,pi**3*r**6/6.0,16*r**7*pi**3/105,pi**4*r**8/24,32*pi**4*r**9/945.0]
limit=len(theoretical_solution)
inscribedcubevolume=[((2*r)/np.sqrt(n+2))**(n+2) for n in range(limit)]
ratiovector=np.zeros(limit)
for i in range(limit):
    ratiovector[i]=inscribedcubevolume[i]/theoretical_solution[i]

print (ratiovector)

plt.plot(ratiovector)
plt.title('Volume cube/sphere ratio')   
plt.xlabel('Ndim')
plt.ylabel('Volume cube/sphere ratio')
plt.grid(True)
plt.show()

