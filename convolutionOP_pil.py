import pyfits
import cv2
import matplotlib.pyplot as plt
import numpy
from conf import simConfiguration
from PIL import Image
from PIL import ImageOps


#parameters
psf_path = '../../sciPsfInst_00.fits'
oimage_path = '../originalImage/Oimage.png'
oimage_FOV = [0.5033754283, 0.3355836189]
oimage_resize = 0.1
#initialize
print("Initialising...")
sc_FOV = simConfiguration["Science"]["FOV"][0] * 0.4
psfs_fits = pyfits.open(psf_path)
if "NAXIS3" in psfs_fits[0].header:
	psfs = psfs_fits[0].data
else: 
	psfs_fits[0].header["NAXIS3"] = 1
	psfs = []
	psfs.append(psfs_fits[0].data)
oimage = ImageOps.grayscale(Image.open(oimage_path))
#oimage = oimage.resize((int(oimage.shape[0]*oimage_resize) , int(oimage.shape[1]*oimage_resize)))
oimage = oimage.resize((100 , 150))
oimage = oimage / float(oimage.max()) * 255.0
#psfs rotation

#psfs_mod_rotated = numpy.zeros((len(psfs_mod) , psfs[0].shape[0] , psfs[0].shape[1]))
#psfs_mod_rotated = []
#for psf_mod in psfs_mod:
#	for i in range(psf_mod.shape[0]):
#		for j in range(psf_mod.shape[1]):
#			psfs_mod_rotated.append(psf_mod[psf_mod.shape[0] - 1 - i , psf_mod[0].shape[1] - 1 - j])

#resize
hightpixel = int(sc_FOV/(oimage_FOV[0]/oimage.shape[0]))
widthpixel = int(sc_FOV/(oimage_FOV[1]/oimage.shape[1]))
psfs_mod = [cv2.resize(psf , (widthpixel , hightpixel)) for psf in psfs]
#convolution
print("Convoluting " + psf_path + " and " + oimage_path + "...")
simulatedImage = [cv2.filter2D(oimage , 32 , psf*1) for psf in psfs_mod]

plt.subplot(131)
plt.imshow(oimage)
plt.subplot(132)
plt.imshow(psfs_mod[0])
plt.subplot(133)
plt.imshow(simulatedImage[0])
plt.colorbar()
plt.show()