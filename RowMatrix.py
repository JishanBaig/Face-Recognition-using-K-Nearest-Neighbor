__author__ = 'satya'

import numpy as np

def toRowMatrix(imageArray) :

    if(len(imageArray) == 0) :
        return np.array([])

    completeMatrix = np.empty(shape=(0,imageArray[0].size),dtype=imageArray[0].dtype)

    for row in imageArray :
        completeMatrix = np.vstack(tup=(completeMatrix,np.asarray(row).reshape(1,-1)))

    return completeMatrix
