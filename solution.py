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
        preweights =[]
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
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[.5, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[-.5, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5], size=[length, width, height])
        pyrosim.End()

    def Create_Brain(self):
        brain_file_name = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(brain_file_name)
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        # for sensor in range(0, c.numSensorNeurons):
        #     pyrosim.Send_Sensor_Neuron(name=sensor, linkName=str(sensor))


        # for motor in range(c.numSensorNeurons, c.numSensorNeurons + c.numMotorNeurons):
        #     pyrosim.Send_Motor_Neuron(name=3, jointName=str(motor))

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

       # print("Synaptic Weights")
        for currentRow in range(c.numSensorNeurons):
            for currentColumnPlus3 in range(c.numSensorNeurons, c.numSensorNeurons + c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumnPlus3,
                                     weight=(self.weights[currentRow][currentColumnPlus3 - 3]))
               # print(self.weights[currentRow][currentColumnPlus3 - 3]) print synaptic weights

        pyrosim.End()

    def Set_ID(self, ID):
        self.myID = ID


