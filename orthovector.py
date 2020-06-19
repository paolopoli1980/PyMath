##############################################################################
###########orthogonal vector calculation in a n dimensional space#############
##############################################################################

import numpy as np

def vector_generator(ndim):
    
    det=0
    mat=[]
    while det==0:
        mat=np.random.rand(ndim,ndim)
        
        det=np.linalg.det(mat)
    return (mat,det)
    
def find_orthogonal_vector(ndim):
   
    known_terms= np.zeros(ndim)
    known_terms[ndim-1]=1
    memmat=vector_generator(ndim)[0].transpose()
 
    orthovector=np.linalg.solve(memmat,known_terms)

    
    dotproduct=[]
    for i in range(ndim):
        vectot=0
        for j in range(ndim):
            vectot+=memmat[i][j]*orthovector[j]
        dotproduct.append(vectot)
    print (dotproduct)
    print (orthovector)
ndim=10

memmat = np.zeros((ndim,ndim))
find_orthogonal_vector(ndim)
