#nimage depends on the exposure time
#only setting nimage is needed to run this program
import pyfits
import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

nimages = 40#parameter

images = []
for n in range(nimages):
	images.append(cv2.imread('../results/png/_' + str("{0:03d}".format(n+1)) + "_ForGnuPlot.png" , cv2.IMREAD_COLOR))

LE_image = np.zeros((images[0].shape[0] , images[0].shape[1] , 3))
for n in range(nimages):
	LE_image += images[n]
LE_image /= nimages
cv2.imwrite("../results/LE_image.png" , LE_image)
print "long exposure succesfully simulated"