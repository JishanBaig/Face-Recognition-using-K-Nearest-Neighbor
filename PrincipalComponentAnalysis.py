
import numpy as np
import sys

def pca(imageArray ,picIdArray ,numberOfComponents = None) :
    """

    :param imageArray: All the Training Example Images in Array Form
    :param imageIdArray: The Image IDs maintained as a list
    :param numberOfCompoenents:Select the numberOfComponents best Eigenvalues and the corresponding EigenVectors
    :return:EigenValues,Eigenvectors and a an array of means
    """


    [numberOfRows,numberOfColumns] = np.shape(a=imageArray)
    if (numberOfCompoenents <= 0) or (numberOfCompoenents > numberOfRows) :
        numberOfCompoenents = numberOfRows

    meanVector = np.mean(a=imageArray,axis=0) #axis = 0 implies :compute the mean on the flattened array

    imageArray -= meanVector

    try :

        if numberOfRows > numberOfColumns :

            #Reduce Dimension of The Covariance Matrix
            covarianceMatrix = np.dot(a=(imageArray.T,imageArray))
            [eigenValues , eigenVectors] = np.linalg.eigh(a=covarianceMatrix)

        else :
            covarianceMatrix = np.dot(a=(imageArray,imageArray.T))
            [eigenValues,eigenVectors] = np.linalg.eigh(a=covarianceMatrix)
            eigenVectors = np.dot(a=(imageArray.T,eigenVectors))

    except np.linalg.LinAlgError :
        print('Eigen Value Computation did not converge')

    except :
        print('Unexpected Error : Type of Error :'),
        print sys.exc_info()[0]
        raise

    for eachRow in range(0,numberOfRows) :
        eigenVectors[ : ,eachRow] = eigenVectors[ : ,eachRow] / np.linalg.norm(eigenVectors[ : ,eachRow])

    sortedIndices = np.argsort(-eigenValues) #Array of sorted indices(Indices from eigenValues)

    eigenValues = eigenValues[sortedIndices]
    eigenVectors = eigenVectors[ : ,sortedIndices]

    #Select only the number of components

    eigenValues = eigenValues[0 : numberOfCompoenents]
    eigenVectors = eigenVectors[ : ,0:numberOfCompoenents]

    return [eigenValues ,eigenVectors ,meanVector]

