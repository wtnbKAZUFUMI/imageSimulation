import os
import pyfits
import cv2
import matplotlib.pyplot as plt
import numpy

images_dir = "../results/convolution/midterm/longExposure/"
output_dir = "../results/convolution/midterm_lighted/"

image_files_list = os.listdir(images_dir)
if ".DS_Store" in image_files_list:
	image_files_list.remove(".DS_Store")

for file_name in image_files_list:
	image = cv2.imread(images_dir + file_name , cv2.IMREAD_GRAYSCALE)
	image = image + image
	cv2.imwrite(output_dir + file_name , image)

