#nimages: number of images that is going to be integlated
#only setting nimages is needed
import cv2
import numpy as np
from math import *
import sys

nimages = 46656#parameter

images = []

for n in range(nimages):
	f = open(("../results/txt/" + str(n) + "_ForGnuPlot.txt") , "w")
	images.append(cv2.imread(("../results/convolution/master/" + "{0:06d}".format(n) + ".png") , cv2.IMREAD_GRAYSCALE))
	for i in range(images[0].shape[0]):
		for j in range(images[0].shape[1]):
			f.write(str(i) + "	" + str(j) + "	" + str(images[n][i , j]))
			f.write("\n")
		f.write("\n")
	f.close()	
print "files for GUNPLOT succesfully generated"

#for n in range(nimages):
#	for i in range(images[0].shape[0]):
#		for j in range(images[0].shape[1]):
#			f[n].write(str(i) + "	" + str(j) + "	" + str(images[n][i , j]))
#			f[n].write("\n")
#		f[n].write("\n")

#for n in range(nimages):
#	f[n].close()