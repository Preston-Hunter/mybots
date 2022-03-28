import numpy
from pyrosim import pyrosim
import os
import random
import time
import constants as c

length = 1
width = 1
height = 1


class SOLUTION:

    def __init__(self, ID):
        self.myID = ID
        preweights = []
        rowInWeights = []
        for sensor in range(0, c.numSensorNeurons):
            for motor in range(0, c.numMotorNeurons):
                rowInWeights.append(numpy.random.rand())
            preweights.append(rowInWeights)
            rowInWeights = []

        self.weights = numpy.array(preweights)

        # self.weights = numpy.array([[numpy.random.rand(), numpy.random.rand()], [numpy.random.rand(), numpy.random.rand()],
        #                 [numpy.random.rand(), numpy.random.rand()]])

        self.weights *= 2
        self.weights -= 1

    def Evaluate(self, directOrGUI):

        self.Start_Simulation(directOrGUI)
        self.Wait_For_Simulation_To_End()

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        fitnessFile = open(fitnessFileName, "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()
        os.system("del " + fitnessFileName)

    def Mutate(self):
        row = random.randint(0, c.numSensorNeurons - 1)
        col = random.randint(0, c.numMotorNeurons - 1)
        self.weights[row, col] = random.random() * 2 - 1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[0, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position=[-.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-.5, 0, 0], size=[1, .2, 0.2])
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position=[.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[.5, 0, 0], size=[1, .2, 0.2])

        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute",
                           position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[.2, .2, 1])

        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute",
                           position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[.2, .2, 1])

        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute",
                           position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[.2, .2, 1])
        #
        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute",
                           position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[.2, .2, 1])

        pyrosim.End()

    def Create_Brain(self):
        brain_file_name = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(brain_file_name)
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="RightLowerLeg")
        # for sensor in range(0, c.numSensorNeurons):
        #     pyrosim.Send_Sensor_Neuron(name=sensor, linkName=str(sensor))

        # for motor in range(c.numSensorNeurons, c.numSensorNeurons + c.numMotorNeurons):
        #     pyrosim.Send_Motor_Neuron(name=3, jointName=str(motor))

        pyrosim.Send_Motor_Neuron(name=5, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=8, jointName="Torso_RightLeg")

        pyrosim.Send_Motor_Neuron(name=9, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="RightLeg_RightLowerLeg")

        # print("Synaptic Weights")
        for currentRow in range(c.numSensorNeurons):
            for currentColumnPlus3 in range(c.numSensorNeurons, c.numSensorNeurons + c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumnPlus3,
                                     weight=(self.weights[currentRow][currentColumnPlus3 - c.numSensorNeurons]))
            # print(self.weights[currentRow][currentColumnPlus3 - 3]) print synaptic weights

        pyrosim.End()

    def Set_ID(self, ID):
        self.myID = ID
