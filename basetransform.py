#################################################################
############### n transformed dimensional space##################
#################################################################

import numpy as np


def vector_generator(ndim):
    
    det=0
    mat=[]
    while det==0:
        mat=np.random.rand(ndim,ndim)
        
        det=np.linalg.det(mat)
    return (mat,det)
ndim=5
ortobasis=np.zeros((ndim,ndim))
memmat=vector_generator(ndim)[0].transpose()
vector=np.random.rand(ndim)
solution=np.linalg.solve(memmat,vector)
print (vector)
print (solution)

