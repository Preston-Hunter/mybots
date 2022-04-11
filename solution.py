import numpy
from pyrosim import pyrosim
import os
import random
import time
import constants as c

length = 1
width = 1
height = 1

numHiddenNeurons = 1
class SOLUTION:

    def __init__(self, ID):
        self.myID = ID
        pre_sensor_weights = []
        rowInSensorWeights = []
        for sensor in range(0, c.numSensorNeurons):
            for hidden in range(0, c.numHiddenNeurons):
                rowInSensorWeights.append(numpy.random.rand())
            pre_sensor_weights.append(rowInSensorWeights)
            rowInSensorWeights = []

        self.sensor_weights = numpy.array(pre_sensor_weights)

        pre_motor_weights = []
        rowInMotorWeights = []
        for hidden in range(0, c.numHiddenNeurons):
            for motor in range(0, c.numMotorNeurons):
                rowInMotorWeights.append(numpy.random.rand())
            pre_motor_weights.append(rowInMotorWeights)
            rowInMotorWeights = []

        self.motor_weights = numpy.array(pre_motor_weights)

        # self.weights = numpy.array([[numpy.random.rand(), numpy.random.rand()], [numpy.random.rand(), numpy.random.rand()],
        #                 [numpy.random.rand(), numpy.random.rand()]])

        self.sensor_weights *= 2
        self.sensor_weights -= 1

        self.motor_weights *= 2
        self.motor_weights -= 1

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
        which_matrix = random.randint(0, 1)
        if which_matrix % 2 == 0:
            row = random.randint(0, c.numSensorNeurons - 1)
            col = random.randint(0, c.numHiddenNeurons - 1)
            self.sensor_weights[row, col] = random.random() * 2 - 1
        else:
            row = random.randint(0, c.numHiddenNeurons - 1)
            col = random.randint(0, c.numMotorNeurons - 1)
            self.motor_weights[row, col] = random.random() * 2 - 1

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

        sensor_neuron_names = ["Torso", "Backleg", "FrontLeg", "LeftLeg", "RightLeg", "BackLowerLeg", "FrontLowerLeg",
                        "LeftLowerLeg", "RightLowerLeg"]
        #Sensor Neurons
        i = 0
        pyrosim.Send_Sensor_Neuron(name=i, linkName="Torso")
        i+=1
        pyrosim.Send_Sensor_Neuron(name=i, linkName="BackLeg")
        i+=1
        pyrosim.Send_Sensor_Neuron(name=i, linkName="FrontLeg")
        i+=1
        pyrosim.Send_Sensor_Neuron(name=i, linkName="LeftLeg")
        i+=1
        pyrosim.Send_Sensor_Neuron(name=i, linkName="RightLeg")
        i+=1
        pyrosim.Send_Sensor_Neuron(name=i, linkName="BackLowerLeg")
        i+=1
        pyrosim.Send_Sensor_Neuron(name=i, linkName="FrontLowerLeg")
        i+=1
        pyrosim.Send_Sensor_Neuron(name=i, linkName="LeftLowerLeg")
        i+=1
        pyrosim.Send_Sensor_Neuron(name=i, linkName="RightLowerLeg")
        i+=1
        # for sensor in range(0, c.numSensorNeurons):
        #     pyrosim.Send_Sensor_Neuron(name=sensor, linkName=str(sensor))

        # for motor in range(c.numSensorNeurons, c.numSensorNeurons + c.numMotorNeurons):
        #     pyrosim.Send_Motor_Neuron(name=3, jointName=str(motor))


        # Hidden neurons
        for j in range(c.numHiddenNeurons):
            pyrosim.Send_Hidden_Neuron(name=i)
            i+=1
        # Motor Neurons
        pyrosim.Send_Motor_Neuron(name=i, jointName="Torso_BackLeg")
        i+=1
        pyrosim.Send_Motor_Neuron(name=i, jointName="Torso_FrontLeg")
        i+=1
        pyrosim.Send_Motor_Neuron(name=i, jointName="Torso_LeftLeg")
        i+=1
        pyrosim.Send_Motor_Neuron(name=i, jointName="Torso_RightLeg")
        i+=1

        pyrosim.Send_Motor_Neuron(name=i, jointName="BackLeg_BackLowerLeg")
        i+=1
        pyrosim.Send_Motor_Neuron(name=i, jointName="FrontLeg_FrontLowerLeg")
        i+=1
        pyrosim.Send_Motor_Neuron(name=i, jointName="LeftLeg_LeftLowerLeg")
        i+=1
        pyrosim.Send_Motor_Neuron(name=i, jointName="RightLeg_RightLowerLeg")
        i+=1

        # print("Synaptic Weights")
        #Sensor neuron weights
        for sensor in range(0, c.numSensorNeurons):
            for hidden in range(0, c.numHiddenNeurons):
                hidden_name = hidden + c.numSensorNeurons
                pyrosim.Send_Synapse(sourceNeuronName=sensor, targetNeuronName=hidden_name,
                                     weight=(self.sensor_weights[sensor][hidden]))
            # print(self.weights[currentRow][currentColumnPlus3 - 3]) print synaptic weights
        #Hidden neuron weights
        for hidden in range(0, c.numHiddenNeurons):
            for motor in range(0, c.numMotorNeurons):
                hidden_name = hidden + c.numSensorNeurons
                motor_name = motor + c.numSensorNeurons + c.numHiddenNeurons
                if(c.numHiddenNeurons != 1):
                    pyrosim.Send_Synapse(sourceNeuronName=hidden_name, targetNeuronName=motor_name,
                                     weight=(self.motor_weights[hidden][motor]))
                else:
                    pyrosim.Send_Synapse(sourceNeuronName=hidden_name, targetNeuronName=motor_name,
                                         weight=(self.motor_weights[0][motor]))
        pyrosim.End()

    def Set_ID(self, ID):
        self.myID = ID
