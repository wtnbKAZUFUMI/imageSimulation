import pyfits
import cv2
import matplotlib.pyplot as plt
import numpy
from conf import simConfiguration
from PIL import Image

a = numpy.zeros((10,10))
a = [[i + j*10 for i in range(10)] for j in range(10)]

b = [i[::-1] for i in a[::-1]]
print b
c = numpy.array(b)
print c