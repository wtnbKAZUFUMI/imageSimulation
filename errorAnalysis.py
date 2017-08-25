
import os
import pyfits
import cv2
import matplotlib.pyplot as plt
import numpy
import math
import random




def loadTarget(target):
	return numpy.array(cv2.imread(target , cv2.IMREAD_GRAYSCALE).tolist())
def loadDataSet(dataset_dir):
	dataset_files_list = os.listdir(dataset_dir)
	if ".DS_Store" in dataset_files_list:
			dataset_files_list.remove(".DS_Store")
	dataset = [numpy.array(cv2.imread(dataset_dir + file , cv2.IMREAD_GRAYSCALE).tolist()) for file in dataset_files_list]
	return dataset
def errorListFromSADMethod(dataset , data):
	error = [(data - dataset_element) for dataset_element in dataset]
	sumed_error = [i.sum() for i in error]
	return sumed_error
def MyerrorListFromSADMethod(dataset , data):
	#print data.tolist() 
	error = [dataset_element - data for dataset_element in dataset]
	sumed_error = [i.sum() for i in error]
	data_sum = data.sum()
	sumed_error_dived = [float(i)/data_sum for i in sumed_error]
	return sumed_error_dived
def errorListFromSSDMethod(dataset , data):
	error = [numpy.abs(data - dataset_element) for dataset_element in dataset]
	powed_error = [math.pow(i.sum(),2) for i in error]
	return powed_error
def errorListFromNCCMethod(dataset, data):
	error = [numpy.multiply(dataset_element,data).sum()/(math.sqrt(numpy.multiply(dataset_element,dataset_element).sum()) * math.sqrt(numpy.multiply(data,data).sum())) for dataset_element in dataset]
	error_alt = [i if not math.isnan(i) else 0.0 for i in error]
	return error_alt
def errorListFromZNCCMethod(dataset, data):
	m = data.shape[0]
	n = data.shape[1]
	error = [(m*n*numpy.multiply(dataset_element,data).sum() - dataset_element.sum()*data.sum())/math.sqrt((m*n*numpy.multiply(dataset_element,dataset_element).sum() - math.pow(dataset_element.sum(),2)) * (m*n*numpy.multiply(data,data).sum() - math.pow(data.sum(),2))) for dataset_element in dataset]
	for ind,val in enumerate(error):
		if val > 1.0:
			print str(ind) + " : " + str(val)
	error_alt = [i if not math.isnan(i) else 0.0 for i in error]
	return error_alt
def errorListFromSIFTMethod(dataset, data):
	sift = cv2.SIFT()
	kp_1, des_1 = sift.detectAndCompute(dataset[500], None)
	kp_2, des_2 = sift.detectAndCompute(data, None)
	matcher = cv2.DescriptorMatcher_create("FlannBased")
	matches = matcher.match(des_1,des_2)
def errorListFromLuminance(dataset, data):
	error = [abs(float(data.sum()) - float(dataset_element.sum())) for dataset_element in dataset]
	#print error
	return error
def makeRankList(error_list):
	error_sorted = sorted(error_list)
	error_li = list(set(error_sorted))
	ans = []
	for i in error_li:
		for ind, val in enumerate(error_list):
			if i == val:
				ans.append(ind)
	#print ans
	return ans
def eliteSelect(error_sad, tolerance_ratio):
	elite = []
	for ind , val in enumerate(error_sad):
		if abs(val) <= tolerance_ratio:
			elite.append(ind)
	return elite
def chrVector(error_mysad_elite , error_zncc_elite):
	return [numpy.array([error_mysad_elite[i] , error_zncc_elite[i]]) for i in range(len(error_mysad_elite))]
def proto_chrVector(error_mysad_elite , error_zncc_elite , elite , target_number):
	target = numpy.array([error_mysad_elite[elite.index(target_number)] , error_zncc_elite[elite.index(target_number)]])
	print target
	return [numpy.array([error_mysad_elite[i] , error_zncc_elite[i]]) - target for i in range(len(error_mysad_elite))]
def ranking(mag, elite):
	mag_sorted_set = sorted(set(mag))
	#print mag_sorted_set
	ind_mag = []
	for i in mag_sorted_set:
		for ind,val in enumerate(mag):
			if i == val:
				ind_mag.append(ind)
	ans = []
	for i in ind_mag:
		for ind,val in enumerate(elite):
			if i == ind:
				ans.append(val)
	return ans
def rankToDeg(rank):
	delta_deg = 36
	ans = []
	for i in rank:
		a = (i/100) * delta_deg
		b = (i%100)/10 * delta_deg
		c = ((i%100)%10) * delta_deg
		numpy.array([a, b, c])
		ans.append(numpy.array([a, b, c]))
	return ans
def degs3DPlot(degs):
	degs = degs[0:100:1]
	x = [deg[0] for deg in degs]
	y = [deg[1] for deg in degs]
	z = [deg[2] for deg in degs]
	plt.subplot(121)
	plt.scatter(x, y)
	plt.subplot(122)
	plt.scatter(x, z)
	plt.show()
def outputResults(sad, ncc, output_file, dataset_dir):
	dataset_files_list = os.listdir(dataset_dir)
	if ".DS_Store" in dataset_files_list:
			dataset_files_list.remove(".DS_Store")
	f = open(output_file, "w")
	#f.write("file_name\tSAD\tNCC\n")
	for i in range(len(sad)):
		f.write(str(dataset_files_list[i].split(".")[0]) + "\t" + str(sad[i]) + "\t" +str(ncc[i]) + "\n")

def main(dataset_dir, target):
	number = dataset_dir.split("/")[3]
	target = loadTarget(target)
	dataset = loadDataSet(dataset_dir)
	error_mysad = MyerrorListFromSADMethod(dataset , target)
	error_ncc = errorListFromNCCMethod(dataset , target)
	#plt.scatter(error_mysad, error_ncc)
	outputResults(error_mysad, error_ncc, "../results/errorAnalysis/" + str(number) + "/longExposure.txt", dataset_dir)
	

	#a = error_mysad
	#b = numpy.array(error_ncc)
	#elite = eliteSelect(error_mysad, tolerance_ratio = 1.0)
	#a = [a[i] for i in elite]
	#b = [b[i] for i in elite]
	
	
#main(dataset_dir = "../results/convolution/000/longExposure/" , target = "../results/convolution/000/longExposure/000970.png")
#main(dataset_dir = "../results/convolution/001/longExposure/" , target = "../results/convolution/000/longExposure/000970.png")
#main(dataset_dir = "../results/convolution/002/longExposure/" , target = "../results/convolution/000/longExposure/000970.png")
#main(dataset_dir = "../results/convolution/003/longExposure/" , target = "../results/convolution/000/longExposure/000970.png")
#main(dataset_dir = "../results/convolution/004/longExposure/" , target = "../results/convolution/000/longExposure/000970.png")
#main(dataset_dir = "../results/convolution/005/longExposure/" , target = "../results/convolution/000/longExposure/000970.png")
#main(dataset_dir = "../results/convolution/006/longExposure/" , target = "../results/convolution/000/longExposure/000970.png")
main(dataset_dir = "../results/convolution/007/longExposure/" , target = "../results/convolution/000/longExposure/000970.png")
#main(dataset_dir = "../results/convolution/008/longExposure/" , target = "../results/convolution/000/longExposure/000970.png")
#main(dataset_dir = "../results/convolution/009/longExposure/" , target = "../results/convolution/000/longExposure/000970.png")
#plt.show()
'''
dataset_dir = "../results/convolution/000/longExposure/"
target_number = 971
target = "../results/convolution/000/longExposure/000970.png"

target = loadTarget(target)
dataset = loadDataSet(dataset_dir)
error_mysad = MyerrorListFromSADMethod(dataset , target)
#error_sad = errorListFromSADMethod(dataset , dataset[target_number])
#error_ssd = errorListFromSSDMethod(dataset , dataset[target_number])
error_ncc = errorListFromNCCMethod(dataset , target)
#error_zncc = errorListFromZNCCMethod(dataset , dataset[target_number])
#error_sift = errorListFromSIFTMethod(dataset , dataset[target_number])
#error_luminance = errorListFromLuminance(dataset, dataset[target_number])
#big_ch_vector = chrVector(error_mysad , error_zncc)
#print big_ch_vector[284]
#print big_ch_vector[329]

a = error_mysad
b = numpy.array(error_ncc)
elite = eliteSelect(error_mysad, tolerance_ratio = 1.0)
a = [a[i] for i in elite]
b = [b[i] for i in elite]
plt.scatter(a, b)
plt.show()
ch_vector = proto_chrVector(a , b , elite , target_number)
#for i in ch_vector:
#	print i

mag = [abs(i[1]) for i in ch_vector]
#print mag
plt.plot(range(len(a)) , sorted(mag) , "o" , markersize=5)
plt.show()
rank = ranking(mag,elite)
#for i in rank:
#	print (i)
#	print error_zncc[i]

#degs = rankToDeg(rank)
#for i in degs:
#	print i

#degs3DPlot(degs)
'''


