from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim


class ROBOT:

    def __init__(self, runtime):
        self.sensors = {}
        self.runtime = runtime

        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName, self.runtime)

    def Sense(self, step):
        print(step)
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(step)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            print(jointName)
            self.motors[jointName] = MOTOR(jointName, self.runtime, self.robotId)

    def Act(self, step):
        for motor in self.motors:
            self.motors[motor].Set_Value(step)

    def Save_Motors(self):
        for motor in self.motors:
            motor.Save_Values()

    def Save_Sensors(self):
        for sensor in self.sensors:
            sensor.Save_Values()

