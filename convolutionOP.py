#imports
import os
import pyfits
import cv2
import matplotlib.pyplot as plt
import numpy
import commands
try:
	from conf import simConfiguration
except:
	commands.getstatusoutput("cp ../../conf.py .")
	from conf import simConfiguration

#parameters
psf_path = "../../sciPsf_00.fits"
oimagename = "Oimage.png"
oimage_dir = "../originalImage/"
output_dir = "../results/convolution_" + oimagename.split(".")[0] + "/"
oimage_FOV = [0.5033754283, 0.3355836189]
oimage_resize = 0.1
oimage_max_luminance = 255 
sc_FOV_ratio = 0.2 #default: 1.0
#initialize
print("Initializing...")
sc_FOV = simConfiguration["Science"]["FOV"][0] * sc_FOV_ratio
psfs_fits = pyfits.open(psf_path)
if "NAXIS3" in psfs_fits[0].header:
	psfs = psfs_fits[0].data
	isFullExposure = False
else: 
	psfs_tmp = []
	psfs_tmp.append(psfs_fits[0].data.tolist())
	psfs = numpy.array(psfs_tmp) / float(simConfiguration["Sim"]["nIters"])
	isFullExposure = True
oimage = cv2.imread(oimage_dir + oimagename , cv2.IMREAD_GRAYSCALE)
oimage = cv2.resize(oimage , (int(oimage.shape[1]*oimage_resize) , int(oimage.shape[0]*oimage_resize)))
oimage = oimage / float(oimage.max()) * oimage_max_luminance
#psfs rotation
print("rotating psfs...")
psfs_list = psfs.tolist()
psfs_len = range(len(psfs))
psfs_rot = [numpy.array([i[::-1] for i in psfs_list[n][::-1]]) for n in psfs_len]
#resize
print("resizing...")
hightpixel = int(sc_FOV/(oimage_FOV[0]/oimage.shape[0]))
widthpixel = int(sc_FOV/(oimage_FOV[1]/oimage.shape[1]))
psfs_rot_mod = [cv2.resize(psf , (widthpixel , hightpixel)) for psf in psfs_rot]
#convolution
print("Convoluting " + psf_path + " and " + oimage_dir + oimagename + "...")
simulatedImage = [cv2.filter2D(oimage , 32 , psf*1) for psf in psfs_rot_mod]
#write files
print("writing files...")
if isFullExposure:
	[cv2.imwrite(output_dir + str("FullExposure/") + str(n) + ".bmp" , simulatedImage[n]) for n in psfs_len]
else :
	[cv2.imwrite(output_dir + str("InstExposure/") + str(n) + ".bmp" , simulatedImage[n]) for n in psfs_len]
#plt.subplot(131)
#plt.imshow(oimage)
#plt.subplot(132)
#plt.imshow(psfs[0])
#plt.subplot(133)
plt.imshow(simulatedImage[0])
plt.colorbar()
plt.show()

