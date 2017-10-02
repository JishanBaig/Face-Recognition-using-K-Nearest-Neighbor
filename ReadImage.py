__author__ = 'satya'
from PIL import Image
import numpy as np
import os
import sys

def read_images ( myPath,size=None ) :
    c = 0
    imageArray , picIdArray = [] , []

    for directoryPath , directoryNames , fileNames in os.walk( myPath ) :
        for subDirectoryName in directoryNames :
            subject_path = os.path.join (directoryPath , subDirectoryName )
            for eachFilename in os.listdir( subject_path ) :
                try :
                    image = Image.open(os.path.join( subject_path ,eachFilename))
                    image = image.convert('L')
                    # resize to given size ( if given )
                    if ( size is not None ) :
                        image = image.resize( size , Image . ANTIALIAS )
                    imageArray.append( np.asarray ( image,dtype = np.uint8 ) )
                    picIdArray.append ( c )
                except IOError :
                    print ' I / O error ({0}) : {1} '.format(errno , strerror)
                except :
                    print 'Unexpected error : ' ,sys.exc_info()[0]
                    raise
            c = c +1
    return [imageArray , picIdArray ]



#Debugging Info
#pathToImages ='/home/satya/Documents/faces'
#[imageArray,picIdArray] = read_images(myPath=pathToImages)

#print imageArray
#print picIdArray