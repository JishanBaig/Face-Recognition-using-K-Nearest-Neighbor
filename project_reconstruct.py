
import numpy as np

def project(weightVector,imageArray,meanVector = None) :
    """
    PROJECTING THE TARINING EXAMPLES INTO THE PCA SUBSPACE
    :param weightVector:
    :param imageArray:
    :param meanVector:
    :return:
    """
    if meanVector is None :
        return np.dot(imageArray,weightVector)

    else:
        return np.dot(imageArray - meanVector,weightVector)


def reconstruct(weightVector,projectedMatrix,meanVector = None) :
    if meanVector is None :
        return (np.dot(a=projectedMatrix,b=weightVector.T))

    return np.dot(projectedMatrix,weightVector.T) + meanVector

def normalize(imageArray,low,high,dtype = None) :
    imageArray = np.asarray(imageArray)
    minOfImageArray , maxOfImageArray = np.min(imageArray),np.max(imageArray)

    imageArray = imageArray - float(minOfImageArray)
    imageArray = imageArray / (maxOfImageArray - minOfImageArray)
    imageArray = imageArray * (high - low)
    imageArray += low

    if dtype == None :
        return np.asarray(imageArray)

    return np.asarray(imageArray,dtype=dtype)
