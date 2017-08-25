import os
import pyfits
import cv2
import matplotlib.pyplot as plt
import numpy

class ImageSim():
	def __init__(self, parameters , conf):
		self.psf_dir = parameters["psf_dir"]
		self.oimage_dir = parameters["oimage_dir"]
		self.output_dir = parameters["output_dir"]
		self.oimage_FOV = parameters["oimage_FOV"]
		self.oimage_resize = parameters["oimage_resize"]
		self.oimage_max_luminance = parameters["oimage_max_luminance"]
		self.sc_FOV_ratio = parameters["sc_FOV_ratio"]
		self.conf = conf
	def loadOimages(self):
		print("loading original images...")
		self.oimage_files_list = os.listdir(self.oimage_dir)
		if ".DS_Store" in self.oimage_files_list:
			self.oimage_files_list.remove(".DS_Store")
		#print self.oimage_files_list 
		#print self.oimage_files_list
		#print len(self.oimage_files_list)
		self.oimages = [cv2.imread(self.oimage_dir + file , cv2.IMREAD_GRAYSCALE) for file in self.oimage_files_list]
		self.oimages = [cv2.resize(oimage , (int(oimage.shape[1]*self.oimage_resize) , int(oimage.shape[0]*self.oimage_resize))) for oimage in self.oimages]
		oimage_max_list = [float(oimage.max()) for oimage in self.oimages]
		print oimage_max_list
		oimage_max = max(oimage_max_list)		
		self.oimages = [oimage / oimage_max * self.oimage_max_luminance for oimage in self.oimages]

	def	loadInstPsfs(self):
		print("loading sciPsfInst_00.fits...")
		psfs_fits = pyfits.open(self.psf_dir + "sciPsfInst_00.fits")
		self.sc_FOV = self.conf["Science"]["FOV"][0] * self.sc_FOV_ratio
		self.inst_psfs = psfs_fits[0].data
		psfs_list = self.inst_psfs.tolist()
		psfs_len = range(len(self.inst_psfs))
		psfs_rot = [numpy.array([i[::-1] for i in psfs_list[n][::-1]]) for n in psfs_len]
		hightpixel = int(self.sc_FOV/(self.oimage_FOV[0]/self.oimages[0].shape[0]))
		widthpixel = int(self.sc_FOV/(self.oimage_FOV[1]/self.oimages[0].shape[1]))
		psfs_rot_mod = [cv2.resize(psf , (widthpixel , hightpixel)) for psf in psfs_rot]
		self.inst_psfs = psfs_rot_mod
	def	loadLongPsf(self):
		print("loading sciPsf_00.fits...")
		psfs_fits = pyfits.open(self.psf_dir + "sciPsf_00.fits")
		self.sc_FOV = self.conf["Science"]["FOV"][0] * self.sc_FOV_ratio
		long_psf_tmp = []
		long_psf_tmp.append(psfs_fits[0].data.tolist())
		self.long_psf = numpy.array(long_psf_tmp) / float(self.conf["Sim"]["nIters"])
		psfs_list = self.long_psf.tolist()
		psfs_len = range(len(self.long_psf))
		psfs_rot = [numpy.array([i[::-1] for i in psfs_list[n][::-1]]) for n in psfs_len]
		hightpixel = int(self.sc_FOV/(self.oimage_FOV[0]/self.oimages[0].shape[0]))
		widthpixel = int(self.sc_FOV/(self.oimage_FOV[1]/self.oimages[0].shape[1]))
		psfs_rot_mod = [cv2.resize(psf , (widthpixel , hightpixel)) for psf in psfs_rot]
		self.long_psf = psfs_rot_mod
	def runInstExposure(self):
		print("convoluting(inst)...")
		self.inst_simulatedImage = [[cv2.filter2D(oimage , 32 , psf*1) for psf in self.inst_psfs] for oimage in self.oimages]
		plt.imshow(self.inst_simulatedImage[0][35])
		plt.colorbar()
		plt.show()
	def runLongExposure(self):
		print("convoluting(long)...")
		self.long_simulatedImage = [cv2.filter2D(oimage , -1 , psf) for psf in self.long_psf for oimage in self.oimages]
		plt.imshow(self.long_simulatedImage[0]*1)
		#plt.colorbar()
		#plt.show()
	def writeInstFiles(self):
		print("writing inst files...")
		oimages_len = range(len(self.oimages))
		psfs_len = range(len(self.inst_psfs))
		[cv2.imwrite(self.output_dir + str("instExposure/") + str(j) + "_" + str(i) + ".bmp" , self.inst_simulatedImage[j][i]) for i in psfs_len for j in oimages_len]
		plt.imshow(self.inst_simulatedImage[0])
		plt.colorbar()
		plt.show()
	def writeLongFile(self):
		print("writing long files...")
		oimages_len = range(len(self.oimages))
		#[cv2.imwrite(self.output_dir + str("longExposure/") + "{0:06d}".format(j) + ".bmp" , self.long_simulatedImage[j]) for j in oimages_len]
		print self.output_dir + str("longExposure/") + self.oimage_files_list[0]
		[cv2.imwrite(self.output_dir + str("longExposure/") + self.oimage_files_list[j] , self.long_simulatedImage[j]) for j in oimages_len]
	def writePlotLongFile(self):
		print("plotting...")
		oimages_len = range(len(self.oimages))
		for n in oimages_len:
			plt.imshow(self.long_simulatedImage[n])
			plt.savefig("./plot/" + "{0:06d}".format(n) + ".png")

