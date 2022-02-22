from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim


class ROBOT:

    def __init__(self, runtime):
        self.runtime = runtime

        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)

        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            print(linkName)
            self.sensors[linkName] = SENSOR(linkName, self.runtime)

    def Sense(self, step):
        #self.sensors["FrontLeg"].Get_Value(step)
        print(step)
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(step)
            print(sensor)