###############################################################################
############ n dimensional Random Walk ########################################
###############################################################################

import numpy as np
import matplotlib.pyplot as plt

ndim=[1,2,3,5]
nepochs=100
niterations=30000
matrixdistance=np.zeros((nepochs,niterations))
matrixpos1=np.zeros((nepochs,niterations))
matrixpos2=np.zeros((nepochs,niterations))
metricmatrix=np.zeros((nepochs,niterations))
averagelist=np.zeros(niterations)
averagepos1=np.zeros(niterations)
averagepos2=np.zeros(niterations)
zeropos1=np.zeros((len(ndim),nepochs))
averagontimeinzeropos1=np.zeros(niterations)
averagontimeinzeropos2=np.zeros(niterations)
slopelist=np.zeros(niterations-1)


plt.figure()


for t in range(len(ndim)):
    for i in range(nepochs):
        Agent1pos=np.zeros(ndim[t])
        Agent2pos=np.zeros(ndim[t])
        Agent1mov=np.random.randint(ndim[t]*2, size=niterations)
        Agent2mov=np.random.randint(ndim[t]*2, size=niterations)
        for j in range(niterations):
            if Agent1mov[j]<ndim[t]:
                Agent1pos[Agent1mov[j]]+=1

                
            else:
                Agent1pos[Agent1mov[j]-ndim[t]]-=1
                
                
            if Agent2mov[j]<ndim[t]:
                Agent2pos[Agent2mov[j]]+=1

                
            else:
                Agent2pos[Agent2mov[j]-ndim[t]]-=1
                
            
            
            metric=0
            dist1=0
            dist2=0
            contdist=0
            for k in range(ndim[t]):
                metric+=(Agent1pos[k]-Agent2pos[k])**2

            for k in range(ndim[t]):
                dist1+=(Agent1pos[k])**2
                dist2+=(Agent2pos[k])**2
                
            dist1=np.sqrt(dist1)
            dist2=np.sqrt(dist2)
            
            if dist1==0:
                zeropos1[t][i]+=1
                
            metricmatrix[i][j]=np.sqrt(metric)
            matrixpos1[i][j]=dist1
            matrixpos2[i][j]=dist2
            
        
    for i in range(niterations):
        averagelist[i]=np.mean(metricmatrix.transpose()[i])

    for i in range(niterations):
        averagepos1[i]=np.mean(matrixpos1.transpose()[i])    

    for i in range(niterations):
        averagepos2[i]=np.mean(matrixpos2.transpose()[i])
    for i in range(nepochs):
        zeropos1[t][i]/=niterations
        
    for i in range(niterations-1):
        slopelist[i]=averagelist[i+1]-averagelist[i]
    print (metricmatrix)    
    print (averagelist)

# cubevertex
    plt.subplot(221)
    plt.plot(averagepos1,averagepos2)
    plt.ylabel('Average positions agent 2')
    plt.xlabel('Average position agent 1')
    plt.title('Agent 1 Vs Agent 2 average positions')
    plt.grid(True)
    plt.gca().legend(('1d','2d','3d','5d'))

    # cubefaces
    plt.subplot(222)
    plt.plot(averagelist)
    plt.ylabel('Average distance')
    plt.xlabel('steps')
    plt.title('Agent 1 Agent 2 Average distances vs steps ')
    plt.grid(True)    
    plt.gca().legend(('1d','2d','3d','5d'))
  
    plt.subplot(223)
    plt.plot(zeropos1[t])
    plt.ylabel('Agent 1 in origin times fraction')
    plt.xlabel('epochs')
    plt.title('Number of times Agent 1 goes in origin')
    plt.grid(True)    
    plt.gca().legend(('1d','2d','3d','5d'))
    
    plt.subplot(224)
    plt.plot(slopelist)    
    plt.ylabel('Distance slope')
    plt.xlabel('steps')
    plt.title('Agents slope distance')
    plt.grid(True)
    plt.gca().legend(('1d','2d','3d','5d'))
    
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.5,
                    wspace=0.35)
    
plt.show()
