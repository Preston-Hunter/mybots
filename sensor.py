import numpy
import pyrosim.pyrosim as pyrosim

class SENSOR:

    def __init__(self, linkName, runtime):
        self.linkName = linkName
        self.values = numpy.zeros(runtime)


    def Get_Value(self, step):
        print(self.linkName)
        self.values[step] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
        # frontLegSensorValues[_] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

        print(self.values)
