import commands
import os
import pyfits
import cv2
import matplotlib.pyplot as plt
import numpy
import shutil

proc = 10
dataset_dir = "../dataset_0813_master/"

def loadDataSet(proc):
	dataset_files_list_master = os.listdir(dataset_dir)
	if ".DS_Store" in dataset_files_list_master:
			dataset_files_list_master.remove(".DS_Store")
	boundary = [(len(dataset_files_list_master)/float(10)) * i for i in range(proc+1)]
	boundary = [int(i) for i in boundary]
	dataset_files_list_sub = [dataset_files_list_master[boundary[i]:boundary[i+1]] for i in range(proc)]
	for i, n in enumerate(dataset_files_list_sub):
		print i
		dataset = [cv2.imread(dataset_dir + file , cv2.IMREAD_GRAYSCALE) for file in i]
	print "test"
	return dataset

#dataset = loadDataSet(10)


dataset_files_list_master = os.listdir(dataset_dir)
boundary = [(len(dataset_files_list_master)/float(10)) * i for i in range(proc+1)]
boundary = [int(i) for i in boundary]
dataset_files_list_sub = [dataset_files_list_master[boundary[i]:boundary[i+1]] for i in range(proc)]

#dataset_sub_dir = dataset_dir + "{0:03d}".format(0) + "/"
#shutil.copyfile(dataset_dir + "000000.png" , dataset_sub_dir + "000000.png")

for i in range(proc):
	if not "{0:03d}".format(i) in os.listdir(dataset_dir):
		os.mkdir(dataset_dir + "{0:03d}".format(i))
	dataset_sub_dir = dataset_dir + "{0:03d}".format(i) + "/"
	for file in dataset_files_list_sub[i]:
		print file
		shutil.copyfile(dataset_dir + file , dataset_sub_dir + file)




