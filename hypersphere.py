######################################################################################
# Hypersphere volume calculation with the Monte Carlo method
######################################################################################

import numpy as np
import matplotlib.pyplot as plt



def hypersphere(npoints,k,dmax,r):
    legend=''
    color=''
    for dim in range(2,dmax):
        ncountinto=0

        for j in range(npoints):
            distance=0
            s = np.random.uniform(-r,r,dim)
           # print (s)
            for i in s:
                distance+=i**2
            if distance<=r**2:
                ncountinto+=1
        v=(2*r)**dim*ncountinto/npoints

        volume[k][dim-2]=v
        dimension[k][dim-2]=dim

        if k==0:
            legend='n random points='+str(npoints)
            color='ro'
        if k==1:
            legend='n random points='+str(npoints)
            color='bo'

        if k==2:
            legend='n random points='+str(npoints)
            color='go'


    plt.plot(dimension[k],volume[k],str(color), label=str(legend))


nepochs=3
dmax=10
r=1

volume=[  [0 for j in range(2,dmax)]  for i in range(nepochs)]
dimension=[   [0 for j in range(2,dmax)] for i in range(nepochs)]
pi=np.pi
theoretical_solution=[pi,4.0*pi/3.0,0.5*pi**2,8.0*pi**2/15.0,pi**3/6.0,16*pi**3/105,pi**4/24,32*pi**4/945.0]
theoretical_dimension=[2,3,4,5,6,7,8,9]
print (volume)
for i in range(nepochs):
    npoints=(i+1)*10**5 # Number of points to measure the volume of sphere
    
    hypersphere(npoints,i,dmax,r)

plt.xlabel('Ndim')
plt.ylabel('Volume')
plt.plot(theoretical_dimension,theoretical_solution,'yo', label='Theoretical_values')
plt.legend(bbox_to_anchor=(0.25, 0.5,), loc='upper left', borderaxespad=0.)   
plt.show()
