import commands
try:
	from conf import simConfiguration
except:
	commands.getstatusoutput("cp ../../conf.py .")
	from conf import simConfiguration
from parameters import parameter_0, parameter_1, parameter_2, parameter_3, parameter_4, parameter_5, parameter_6, parameter_7, parameter_8, parameter_9, parameter_midterm
from classes import ImageSim
from multiprocessing import Process


def main_inst(parameter, simConfiguration):
	imageSim = ImageSim(parameter , simConfiguration)
	imageSim.loadOimages()
	imageSim.loadInstPsfs()
	imageSim.runInstExposure()
	imageSim.writeInstFiles()
def main_long(parameter, simConfiguration = simConfiguration):
	imageSim = ImageSim(parameter , simConfiguration)
	imageSim.loadOimages()
	imageSim.loadLongPsf()
	imageSim.runLongExposure()
	imageSim.writeLongFile()

#main_long(parameter = parameter_0)
#main_long(parameter = parameter_1)
#main_long(parameter = parameter_2)
#main_long(parameter = parameter_3)
#main_long(parameter = parameter_4)
#main_long(parameter = parameter_5)
#main_long(parameter = parameter_6)
main_long(parameter = parameter_midterm)
#main_long(parameter = parameter_8)
#main_long(parameter = parameter_9)
'''
jobs = [
    Process(target=main_long, args=(parameter_6,simConfiguration)),
    Process(target=main_long, args=(parameter_7,simConfiguration)),
]

for j in jobs:
    j.start()
for j in jobs:
    j.join()

jobs = [
    Process(target=main_long, args=(parameter_8,simConfiguration)),
    Process(target=main_long, args=(parameter_9,simConfiguration))
]

for j in jobs:
    j.start()
for j in jobs:
    j.join()

'''
