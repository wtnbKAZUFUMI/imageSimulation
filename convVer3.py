#sciCameraFOV: field of view of science camera
#sciCameraFOV, fits file of PSF and Original image file are needed to run this program
import pyfits
import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

SciCameraFOV = 2.0#parameter,0.03
#SciCameraFOV = 3.0#parameter, scao_canary
#SciCameraFOV = 3.2#parameter, scao_canary
PSFname = '../../sciPsfInst_00.fits'#parameter
OriginalImagename = '../originalImage/Oimage.png'#parameter

print("Initialising...")
sciPsfList = pyfits.open(PSFname)
sciPsfList[0].header["FOV"] = SciCameraFOV
#for i in sciPsfList[0].header:
# 	print (str(i) + "	" + str(sciPsfList[0].header[i]))
if "NAXIS3" in sciPsfList[0].header:
	psf = sciPsfList[0].data
else: 
	sciPsfList[0].header["NAXIS3"] = 1
	psf = []
	psf.append(sciPsfList[0].data)

OriginalImage = cv2.imread(OriginalImagename , cv2.IMREAD_GRAYSCALE)
print  OriginalImage.max()
OriginalImage = OriginalImage / float(OriginalImage.max()) * 255.0 
print  OriginalImage.max()
OriginalImageFOV = [0.5033754283, 0.3355836189]

#hightpixel = int(OriginalImageFOV[0]/(SciCameraFOV/sciPsfList[0].header["NAXIS1"]))
#widthpixel = int(OriginalImageFOV[1]/(SciCameraFOV/sciPsfList[0].header["NAXIS2"]))
#OriginalImageAdjusted = cv2.resize(OriginalImage , (widthpixel , hightpixel))

#newcode  
hightpixel = int(SciCameraFOV/(OriginalImageFOV[0]/OriginalImage.shape[0]))
widthpixel = int(SciCameraFOV/(OriginalImageFOV[1]/OriginalImage.shape[1]))
psfAdjusted = [cv2.resize(i , (widthpixel , hightpixel)) for i in psf]
#newcode

print("Convoluting " + PSFname + " and " + OriginalImagename + "...")
sciPsfList_c = np.zeros((sciPsfList[0].header["NAXIS3"] , sciPsfList[0].header["NAXIS1"] , sciPsfList[0].header["NAXIS2"]))
for n in range(sciPsfList[0].header["NAXIS3"]):
	for i in range(psfAdjusted[n].shape[0]):
		for j in range(psfAdjusted[n].shape[1]):
			sciPsfList_c[n , i , j] = psfAdjusted[n][psfAdjusted[0].shape[0] - 1 - i , psfAdjusted[0].shape[1] - 1 - j]
simulatedImage = []
for n in range(sciPsfList[0].header["NAXIS3"]):
	simulatedImage.append(cv2.filter2D(OriginalImage,32,sciPsfList_c[n]*1))

print("Writing into files...")
for n in range(sciPsfList[0].header["NAXIS3"]):
	filename = "../results/bmp/" + str(n) + ".bmp"
	cv2.imwrite(str(filename) , simulatedImage[n])

print("convolution succesfully finished")
plt.subplot(131)
plt.imshow(OriginalImage)
plt.subplot(132)
plt.imshow(psf[0])
plt.subplot(133)
plt.imshow(simulatedImage[0])
plt.colorbar()
plt.show()