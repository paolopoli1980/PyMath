import numpy as np

def vector_generator(ndim):
    
    det=0
    mat=[]
    while det==0:
        mat=np.random.rand(ndim,ndim)
        
        det=np.linalg.det(mat)
    return mat,det  
    
ndim=10

print(vector_generator(ndim)[0],vector_generator(ndim)[1])
