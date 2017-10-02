__author__ = 'satya'

import matplotlib as  mt
from matplotlib import pyplot as plot
from matplotlib import text as t
import numpy as np
from PrincipalComponentAnalysis import pca
from project_reconstruct import project,reconstruct,normalize
import sys
from ReadImage import read_images as ri
from RowMatrix import toRowMatrix
from EigenFacesModel import EigenFacesModel as EFM

pathToImages ='/home/satya/Documents/faces'
[imageArray,picIdArray] = ri(myPath=pathToImages)

[eigenValueList,weightedVector,meanVector] = pca(imageArray,picIdArray)

def create_font ( fontname ='Tahoma',fontsize =10) :
    return { 'fontname':fontname,'fontsize':fontsize}


def subPlot(title ,images,numberOfRows,numberOfColumns,sptitle = 'subplot',sptitles=[],colormap = '0.75',ticks_visible = True,fileName = None) :

    figure = plot.figure() #Create an Empty Figure

    figure.text(x=0.5,y=0.95,s=title,horizontalalignment = 'center')

    for row in xrange(len(images)) :

        rowSubplot = figure.add_subplot(numberOfRows,numberOfColumns,(row + 1)) #For each Row construct a subplot

        plot.setp(rowSubplot.get_xticklabels(),visible = False) #For each Subplot make the X -axis Tick Labels invisible
        plot.setp(rowSubplot.get_yticklabels(),visible = False) #For each Subplot make the Y -axis Tick Labels invisible

        if(len(sptitles) == len(images)) :
            plot.title('%s #%s'%(sptitle,sptitles[row]),create_font())

        else :
            plot.title('%s #%d ' %(sptitle,( row+1 ) ),create_font())

        plot.imshow(np.asarray(images[row]),cmap=colormap)

    if fileName == None :
        plot.show()

    else:
        figure.savefig(fileName)

#TURN THE FIRST (AT MOST) 16 EIGEN VECTORS INTO GRAY SCALE

eigenVectorsToBePlotted = []
for iterator in xrange(min(len(imageArray),16)) :
    temporaryList = weightVector[ : , iterator].reshape(imageArray[0])
    eigenVectorsToBePlotted.append ( normalize (temporaryList ,0 ,255) )

subPlot(title='Eigenfaces AT & T Facedatabase',images=eigenVectorsToBePlotted,numberOfRows=4,numberOfColumns=4,sptitle='Eigenface',colormap=mt.jet,fileName=None)

#Reconstruction Steps

indexOfEigenFace = [index for index in xrange(10,min(len(imageArray),320),20)]

principalEigenFaces = []

for eachRow in xrange(min(len(indexOfEigenFace),16)) :
    numberOfEigenFaces = indexOfEigenFace[eachRow]

    P = project(weightVector=weightVector[ : ,0 : numberOfEigenFaces],imageArray=imageArray[0].reshape(1,-1),meanVector=meanVector)

    R = reconstruct(weightVector=weightVector[ : ,0 : numberOfEigenFaces],projectedMatrix=P,meanVector=meanVector)

    principalEigenFaces.append(normalize(R,0,255))


subPlot(title ='Eigenfaces AT & T Facedatabase',images = principalEigenFaces ,numberOfRows=4 ,numberOfColumns=4, sptitle = 'Eigenface' ,colormap = plot.jet , filename = None)

#Debuuging
print picIdArray



