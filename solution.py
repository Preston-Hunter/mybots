import numpy
from pyrosim import pyrosim
import os
import random

length = 1
width = 1
height = 1

class SOLUTION:

    def __init__(self, ID):
        self.myID = ID
        self.weights = numpy.array([[numpy.random.rand(), numpy.random.rand()], [numpy.random.rand(), numpy.random.rand()],
                        [numpy.random.rand(), numpy.random.rand()]])

        self.weights *= 2
        self.weights -= 1



    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID))
        fitnessFile = open("fitness.txt", "r")
        self.fitness = float(fitnessFile.read())
        fitnessFile.close()

    def Mutate(self):
        row = random.randint(0,2)
        col = random.randint(0,1)
        self.weights[row, col] = random.random() * 2 - 1


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()
        print("ss")

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

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

       # print("Synaptic Weights")
        for currentRow in range(0, 3):
            for currentColumnPlus3 in range(3, 5):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumnPlus3,
                                     weight=(self.weights[currentRow][currentColumnPlus3 - 3]))
               # print(self.weights[currentRow][currentColumnPlus3 - 3]) print synaptic weights

        pyrosim.End()

    def Set_ID(self, ID):
        self.myID = ID


