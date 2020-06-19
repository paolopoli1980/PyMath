###########################################################################
############### 2d rectangle bouncing #######################################
###########################################################################
import numpy as np
import matplotlib.pyplot as plt

lenght=5.0
height=5.0
angle=30.0
alfa=angle*np.pi/180
dt=0.1
dt2=0
endt=20
t=0
xpar=1
ypar=1
pointslistx=[]
pointslisty=[]
x=0
y=0
while t<endt:
    t+=dt
    x+=dt*xpar
    y+=(np.tan(alfa))*dt*ypar
    if y>height:
        ymem=y
        y-=(np.tan(alfa))*dt*ypar
        x-=dt*xpar
        
        dt2=(height-y)*dt/(ymem-y)
        y+=(np.tan(alfa))*dt2*ypar
        x+=dt2*xpar
        ypar*=-1
        
        
        
        
    if x>lenght:
        xmem=x

        x-=dt*xpar
        dt2=(lenght-x)*dt/(xmem-x)
        y-=(np.tan(alfa))*dt*ypar
 
        x+=dt2*xpar
        y+=(np.tan(alfa))*dt2*ypar
        xpar*=-1
        

    
        
        
    if x<0:
        xmem=x
        y-=(np.tan(alfa))*dt*ypar
        x-=dt*xpar
        dt2=(-x)*dt/(xmem-x)
        x+=dt2*xpar
        y+=(np.tan(alfa))*dt2*ypar
        xpar*=-1
         
        
        
    if y<0:
        ymem=y
        y-=(np.tan(alfa))*dt*ypar
        x-=dt*xpar
        dt2=(-y)*dt/(ymem-y)
        x+=dt2*xpar
        y+=(np.tan(alfa))*dt2*ypar       
        ypar*=-1
        
       
    
    
    pointslistx.append(x)
    pointslisty.append(y)
plt.title('Ray light in a rectangle geometry')
plt.plot(pointslistx,pointslisty)
plt.show()
