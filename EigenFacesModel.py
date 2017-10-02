import numpy as np
from distanceClass import EuclideanDistance
from PrincipalComponentAnalysis import pca
from ReadImage import read_images as  ri
from RowMatrix import toRowMatrix as trm
from project_reconstruct import project

class EigenFacesModel(object) :

    def __init__(self,imageArray=None,picIdArray=None,distanceMetric = EuclideanDistance(),numberOfComp= None):
        self._distanceMetric = distanceMetric
        self._numberOfComp = 0
        self.projections = []
        self.meanVector =[]
        self.weightVector = []

        if(imageArray is not None) and (picIdArray is not None) :
            self.compute(imageArray,picIdArray)

    def compute(self):
        pathToImages = 'C:\Users\jishan baig\Desktop\ML\faces'
        [imageArray,picIdArray] = ri(myPath=pathToImages)

      #model = EigenFacesModel(imageArray,picIdArray)
print picIdArray


