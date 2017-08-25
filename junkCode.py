#JunkCode_generated_in_errorAnalrsis

'''
elite = []
for ind , val in enumerate(error_sad):
	if val < 10000:
		elite.append(ind)
'''
#print elite



#error_sad_elite = [error_sad[i] for i in elite]
#a = numpy.array([abs(error_sad_elite/10000.0 - 1) for error_sad_elite_e in error_sad_elite])

#b = numpy.array([error_zncc[i] for i in elite])
#print b
#c = numpy.array(elite)
#d = a*b
'''
plt.plot(c, d, "o")
plt.show()
'''
#error_ncc_elite = [error_ncc[i] for i in elite]

'''
error_zncc_elite = [error_zncc[i] for i in elite]
error_sad_elite = [abs(error_sad[i]/10000.0-1) for i in elite]
print error_sad_elite
plt.scatter(error_zncc_elite, error_sad_elite, marker = "o")
plt.show()
'''

#print error_zncc
#ax.scatter(error_zncc_elite , error_luminance_elite)




#plt.plot(error_sad_parsent , error_zncc , "o")
#plt.show()
'''
plt.subplot(121)
plt.plot(elite, [abs(error_sad_elite_e/10000.0 - 1) for error_sad_elite_e in error_sad_elite], "*", markersize=15)
plt.subplot(121)
plt.plot(elite, error_zncc_elite, "o", markersize=7)

#plt.plot(range(len(error_luminance_elite)), error_luminance_elite, "o", markersize=7)
plt.show()

plt.subplot(231)
plt.plot(member, sorted(error_sad), "o", markersize=2)

plt.subplot(232)
plt.plot(member, sorted(error_ssd), "o", markersize=2)

plt.subplot(233)
plt.plot(member, sorted(error_ncc), "o", markersize=2)

plt.subplot(234)
plt.plot(member, sorted(error_zncc), "o", markersize=2)

plt.subplot(235)
plt.plot(member, sorted(error_luminance), "o", markersize=2)

plt.show()

#plt.imshow(dataset[700])
#plt.show()
#sums = sumsFromDataSet(dataset)
#test = [cv2.calcHist([data] , [0], None, [256], [0, 256]) for data in dataset]
#plt.show()
#print test[0]
#results_1 = [cv2.compareHist(test[0], i, 0) for i in test]
#results_2 = [cv2.compareHist(test[0], i, 1) for i in test]
#results_3 = [cv2.compareHist(test[0], i, 2) for i in test]
#results_4 = [cv2.compareHist(test[0], i, 3) for i in test]

#x = range(0,1000)
#y = results_1
#plt.plot(x , y , "o")
#plt.show()

'''





