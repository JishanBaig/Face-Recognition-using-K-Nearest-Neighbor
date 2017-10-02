__author__ = 'satya'

import numpy as np


class AbstractDistance(object) :

    def __init__(self,type):
        self.typeOfDistance = type

    def __implement__(self):
        raise NotImplementedError('Every AbsractDistance must invoke the __implement__ method')

    def __name__(self):
        return self.typeOfDistance


class EuclideanDistance(AbstractDistance) :

    def __init__(self):
        AbstractDistance.__init__(self,'EuclideanDistance') #Invoke The Base Class Constructor

    def __implement__(self,list1,list2):
        list1 = np.asarray( list1 ).flatten() #A copy of the input array, flattened to one dimension.
        list2 = np.asarray( list2 ).flatten()
        return np.sqrt(np.sum(np.power(( list1 - list2 ),2)))

#Debugging Info
