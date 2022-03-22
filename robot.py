from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:

    def __init__(self, runtime, solutionID):
        self.solutionID = solutionID
        self.sensors = {}
        self.runtime = runtime

        brain_file_name = "brain" + solutionID + ".nndf"
        self.nn = NEURAL_NETWORK(brain_file_name)

        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)

        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        command = "del " + brain_file_name
        os.system(command)

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName, self.runtime)

    def Sense(self, step):
        for sensor in self.sensors:
            self.sensors[sensor].Get_Value(step)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName, self.runtime, self.robotId)

    # todo what is num 72, seem to be doing t->desiredAngle for no reason
    def Act(self, desiredAngle):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(desiredAngle)
                # print(neuronName, "=", jointName, "storing ", desiredAngle)

    def Think(self):
        self.nn.Update()
        # self.nn.Print() print neural network

    # def Save_Motors(self): # removed method in motor.py
    #     for motor in self.motors:
    #         motor.Save_Values()

    def Save_Sensors(self):
        for sensor in self.sensors:
            sensor.Save_Values()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]

        tmpFileName = "tmp" + str(self.solutionID) + ".txt"
        f = open(tmpFileName, "w")
        f.write(str(xCoordinateOfLinkZero) + "\n")
        f.close()

        fitnessFileName = "fitness" + str(self.solutionID) + ".txt"
        os.system("rename " + tmpFileName + " " + fitnessFileName)
        return xCoordinateOfLinkZero