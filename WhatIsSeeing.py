import pyfits
import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

SciCameraFOV = 3.0#parameter
PSFname = '../../sciPsf_00.fits'#parameter

sciPsf = pyfits.open(PSFname)
sciPsf[0].header["FOV"] = SciCameraFOV

xaxis = sciPsf[0].header["NAXIS1"]
yaxis = sciPsf[0].header["NAXIS2"]
peak = sciPsf[0].data[int(xaxis/2) , int(yaxis/2)]
print sciPsf[0].data[64]
print int(xaxis/2)
print int(yaxis/2)
print peak

for n in range(int(xaxis*0.5)):
	if sciPsf[0].data[int(yaxis*0.5) , n] - peak*0.5 > 0:
		seeing = (int(xaxis/2) - n)*(SciCameraFOV/xaxis)
		print seeing

plt.imshow(sciPsf[0].data)
plt.show()