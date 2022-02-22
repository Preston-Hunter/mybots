import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:

    def __init__(self, linkName, runtime):
        self.linkName = linkName
        self.values = numpy.zeros(runtime)


    def Get_Value(self, step):
        self.values[step] = pyrosim.Get_Touch_Sensor_Value_For_Link('FrontLeg')

    def Save_Values(self):
        save_location = "data/" + self.linkName + ".npy"
        numpy.save(save_location, self.values)

