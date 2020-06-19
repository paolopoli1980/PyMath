from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 1, 10)
x = 1 * np.outer(np.cos(u),1)
y = 1 * np.outer(np.sin(u),1)
z = 1 * np.outer(np.ones(np.size(u)), v)

# Plot the surface
ax.plot_surface(x, y, z, color='r')
px=[]
py=[]
pz=[]
t=0
dt=0.01
tetastar=10*np.pi/180
phistar=10*np.pi/180
tetaend=260*np.pi/180
phiend=65*np.pi/180
zstart=0.25
zend=0.8

n=int(1/dt)
k1=(tetaend-tetastar)
k3=(zend-zstart)

for i in range(n):
    t+=dt
    px.append(np.cos(k1*t+tetastar))
    py.append(np.sin(k1*t+tetastar))
    pz.append(k3*t+zstart)
print (t)    
plt.plot(px,py,pz)    
plt.show()



