import numpy as np
import matplotlib.pyplot as plt

k=100
maxdim=1000
points=[]
numbgraphs=4
for j in range(numbgraphs):
    
    for i in range(2,maxdim):
        prob=((k**i)-(k-2)**i)/k**i
        points.append(prob)
    plt.plot(points)
    points=[]
    k*=2 
plt.title('The probability to stay on a border in function of the dimensions number')   
plt.xlabel('Ndim')
plt.ylabel('P')
plt.grid(True)
plt.gca().legend(('100','200','400','800'))
plt.show()

    
    
