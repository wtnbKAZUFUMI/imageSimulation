#library
import commands
#dictionary
try:
	from conf import simConfiguration
except:
	commands.getstatusoutput("cp ../../conf.py .")
	from conf import simConfiguration
from parameters import parameter_1
#class
from classes import ImageSim


imageSim = ImageSim(parameter_1 , simConfiguration)
imageSim.loadOimages()
#imageSim.loadInstPsfs()
imageSim.loadLongPsf()
#imageSim.runInstExposure()
imageSim.runLongExposure()
#imageSim.writeFiles()





