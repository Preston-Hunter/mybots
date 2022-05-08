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

    def __init__(self, ID, useCPG):
        self.useCPG = useCPG
        self.generation = -1
        self.myID = ID
        pre_sensor_weights = []
        rowInSensorWeights = []

        self.sensor_self_weights = []
        self.motor_self_weights = []
        self.hidden_self_weights = []

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

        # ---------------------Make recurrent connections-----------------

        # connect motors to each other and to hidden and to sensors
        rowInRecMotorWeights = []
        pre_rec_motor_weights = []
        for motor in range(0, c.numMotorNeurons):
            for hid_sen_mot in range(0, c.numHiddenNeurons + c.numSensorNeurons + c.numMotorNeurons - 1):
                rowInRecMotorWeights.append(numpy.random.rand())
            pre_rec_motor_weights.append(rowInRecMotorWeights)
            rowInRecMotorWeights = []
        self.rec_motor_weights = numpy.array(pre_rec_motor_weights)

        # connect hidden to each other and to sensors
        rowInRecHiddenWeights = []
        pre_rec_hidden_weights = []
        for hidden in range(0, c.numHiddenNeurons):
            for hid_sen in range(0, c.numHiddenNeurons + c.numSensorNeurons - 1):
                rowInRecHiddenWeights.append(numpy.random.rand())
            pre_rec_hidden_weights.append(rowInRecHiddenWeights)
            rowInRecHiddenWeights = []
        self.rec_hidden_weights = numpy.array(pre_rec_hidden_weights)
        # print("hidden")
        # print(self.rec_hidden_weights)
        # print("motor")
        # print(self.rec_motor_weights)
        # connect hidden to each other and to sensors

        # connect sensors to each other
        rowInRecSensorWeights = []
        pre_rec_sensor_weights = []
        for sensor in range(0, c.numSensorNeurons):
            for sen in range(0, c.numSensorNeurons - 1):
                rowInRecSensorWeights.append(numpy.random.rand())
            pre_rec_sensor_weights.append(rowInRecSensorWeights)
            rowInRecSensorWeights = []
        self.rec_sensor_weights = numpy.array(pre_rec_sensor_weights)

        # ----------Make self connecting weights----------------
        for sensor in range(0, c.numSensorNeurons):
            self.sensor_self_weights.append(numpy.random.rand())
        self.sensor_self_weights = numpy.array(self.sensor_self_weights)

        for hidden in range(0, c.numHiddenNeurons):
            self.hidden_self_weights.append(numpy.random.rand())
        self.hidden_self_weights = numpy.array(self.hidden_self_weights)

        for motor in range(0, c.numMotorNeurons):
            self.motor_self_weights.append(numpy.random.rand())
        self.motor_self_weights = numpy.array(self.motor_self_weights)

        # self.weights = numpy.array([[numpy.random.rand(), numpy.random.rand()], [numpy.random.rand(), numpy.random.rand()],
        #                 [numpy.random.rand(), numpy.random.rand()]])

        self.sensor_weights *= 2
        self.sensor_weights -= 1

        self.motor_weights *= 2
        self.motor_weights -= 1

        self.sensor_self_weights *= 2
        self.sensor_self_weights -= 1

        self.hidden_self_weights *= 2
        self.hidden_self_weights -= 1

        self.motor_self_weights *= 2
        self.motor_self_weights -= 1

        self.rec_hidden_weights *= 2
        self.rec_hidden_weights -= 1
        self.rec_hidden_weights *= c.scale

        self.rec_motor_weights *= 2
        self.rec_motor_weights -= 1
        self.rec_motor_weights *= c.scale

        self.rec_sensor_weights *= 2
        self.rec_sensor_weights -= 1
        self.rec_sensor_weights *= c.scale

    def Evaluate(self, directOrGUI):

        self.Start_Simulation(directOrGUI)
        self.Wait_For_Simulation_To_End()

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID) + " " + "False")

    def Start_Simulation_Save_Sensors(self, directOrGUI, cpg_tag, abID):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        cpg_tag = cpg_tag + abID
        os.system("python simulate.py " + directOrGUI + " " + str(self.myID) + " " + "True" + " " + cpg_tag)

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        # permission denied can happen here
        try:
            fitnessFile = open(fitnessFileName, "r")
            self.fitness = float(fitnessFile.read())
            fitnessFile.close()
            os.system("del " + fitnessFileName)
        except:
            exception_triggered_file = open("exception.txt", "w")
            try:
                fitnessFile = open(fitnessFileName, "r")
                self.fitness = float(fitnessFile.read())
                fitnessFile.close()
                os.system("del " + fitnessFileName)
            except:
                self.fitness = 0
                exception_triggered_file.write("0")

            exception_triggered_file.close()
            print("---------------------------------------------------------------------")

    def Mutate(self):
        which_matrix = random.randint(0, 3)
        if which_matrix % 4 == 0:
            row = random.randint(0, c.numSensorNeurons - 1)
            col = random.randint(0, c.numHiddenNeurons - 1)
            self.sensor_weights[row, col] = random.random() * 2 - 1
        elif which_matrix % 4 == 1:
            row = random.randint(0, c.numHiddenNeurons - 1)
            col = random.randint(0, c.numMotorNeurons - 1)
            self.motor_weights[row, col] = random.random() * 2 - 1
        elif which_matrix % 4 == 2:  # mutate self connections
            which_neuron_set = random.randint(0, 2)
            if which_neuron_set % 3 == 0:
                if len(self.sensor_self_weights) != 0:
                    index = random.randint(0, len(self.sensor_self_weights) - 1)
                    self.sensor_self_weights[index] = random.random() * 2 - 1
                else:
                    which_neuron_set += 1
            if which_neuron_set % 3 == 1:
                if len(self.hidden_self_weights) != 0:
                    index = random.randint(0, len(self.hidden_self_weights) - 1)
                    self.hidden_self_weights[index] = random.random() * 2 - 1
                else:
                    which_neuron_set += 1
            if which_neuron_set % 3 == 2:
                if len(self.motor_self_weights) != 0:
                    index = random.randint(0, len(self.motor_self_weights) - 1)
                    self.motor_self_weights[index] = random.random() * 2 - 1
        else:
            which_rec_set = random.randint(0, 2)
            # modify rec_motor_weights
            if which_rec_set % 3 == 0:
                row = random.randint(0, c.numMotorNeurons - 1)
                col = random.randint(0, c.numMotorNeurons + c.numSensorNeurons + c.numHiddenNeurons - 2)
                self.rec_motor_weights[row, col] = random.random() * 2 - 1
            elif which_rec_set % 3 == 1:
                row = random.randint(0, c.numMotorNeurons - 1)
                col = random.randint(0, c.numSensorNeurons + c.numHiddenNeurons - 2)
                self.rec_hidden_weights[row, col] = random.random() * 2 - 1
            else:
                row = random.randint(0, c.numSensorNeurons - 1)
                col = random.randint(0, c.numSensorNeurons - 2)
                self.rec_sensor_weights[row, col] = random.random() * 2 - 1

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
        # Sensor Neurons
        i = 0
        pyrosim.Send_Sensor_Neuron(name=i, linkName="Torso")
        i += 1
        pyrosim.Send_Sensor_Neuron(name=i, linkName="BackLeg")
        i += 1
        pyrosim.Send_Sensor_Neuron(name=i, linkName="FrontLeg")
        i += 1
        pyrosim.Send_Sensor_Neuron(name=i, linkName="LeftLeg")
        i += 1
        pyrosim.Send_Sensor_Neuron(name=i, linkName="RightLeg")
        i += 1
        pyrosim.Send_Sensor_Neuron(name=i, linkName="BackLowerLeg")
        i += 1
        pyrosim.Send_Sensor_Neuron(name=i, linkName="FrontLowerLeg")
        i += 1
        pyrosim.Send_Sensor_Neuron(name=i, linkName="LeftLowerLeg")
        i += 1
        pyrosim.Send_Sensor_Neuron(name=i, linkName="RightLowerLeg")
        i += 1

        # -----------------CPG Sensor neuron---------------
        if self.useCPG:
            pyrosim.Send_Sensor_Neuron(name=i, linkName="CPG")
            i += 1
        # for sensor in range(0, c.numSensorNeurons):
        #     pyrosim.Send_Sensor_Neuron(name=sensor, linkName=str(sensor))

        # for motor in range(c.numSensorNeurons, c.numSensorNeurons + c.numMotorNeurons):
        #     pyrosim.Send_Motor_Neuron(name=3, jointName=str(motor))

        # Hidden neurons
        for j in range(c.numHiddenNeurons):
            pyrosim.Send_Hidden_Neuron(name=i)
            i += 1
        # Motor Neurons
        pyrosim.Send_Motor_Neuron(name=i, jointName="Torso_BackLeg")
        i += 1
        pyrosim.Send_Motor_Neuron(name=i, jointName="Torso_FrontLeg")
        i += 1
        pyrosim.Send_Motor_Neuron(name=i, jointName="Torso_LeftLeg")
        i += 1
        pyrosim.Send_Motor_Neuron(name=i, jointName="Torso_RightLeg")
        i += 1

        pyrosim.Send_Motor_Neuron(name=i, jointName="BackLeg_BackLowerLeg")
        i += 1
        pyrosim.Send_Motor_Neuron(name=i, jointName="FrontLeg_FrontLowerLeg")
        i += 1
        pyrosim.Send_Motor_Neuron(name=i, jointName="LeftLeg_LeftLowerLeg")
        i += 1
        pyrosim.Send_Motor_Neuron(name=i, jointName="RightLeg_RightLowerLeg")
        i += 1

        # print("Synaptic Weights")
        # Sensor neuron weights
        for sensor in range(0, c.numSensorNeurons):
            for hidden in range(0, c.numHiddenNeurons):
                hidden_name = hidden + c.numSensorNeurons
                pyrosim.Send_Synapse(sourceNeuronName=sensor, targetNeuronName=hidden_name,
                                     weight=(self.sensor_weights[sensor][hidden]))
            # print(self.weights[currentRow][currentColumnPlus3 - 3]) print synaptic weights
        # Hidden neuron weights
        for hidden in range(0, c.numHiddenNeurons):
            for motor in range(0, c.numMotorNeurons):
                hidden_name = hidden + c.numSensorNeurons
                motor_name = motor + c.numSensorNeurons + c.numHiddenNeurons
                if c.numHiddenNeurons != 1:
                    pyrosim.Send_Synapse(sourceNeuronName=hidden_name, targetNeuronName=motor_name,
                                         weight=(self.motor_weights[hidden][motor]))
                else:
                    pyrosim.Send_Synapse(sourceNeuronName=hidden_name, targetNeuronName=motor_name,
                                         weight=(self.motor_weights[0][motor]))

        # self connections
        for sensor in range(0, c.numSensorNeurons):
            pyrosim.Send_Synapse(sourceNeuronName=sensor, targetNeuronName=sensor,
                                 weight=(self.sensor_self_weights[sensor]))

        for hidden in range(0, c.numHiddenNeurons):
            hidden_name = hidden + c.numSensorNeurons
            pyrosim.Send_Synapse(sourceNeuronName=hidden_name, targetNeuronName=hidden_name,
                                 weight=(self.hidden_self_weights[hidden]))

        for motor in range(0, c.numMotorNeurons):
            motor_name = motor + c.numSensorNeurons + c.numHiddenNeurons
            pyrosim.Send_Synapse(sourceNeuronName=motor_name, targetNeuronName=motor_name,
                                 weight=(self.motor_self_weights[motor]))

        # Recurrent connections

        for motor in range(0, c.numMotorNeurons):
            for hid_sen_mot in range(0, c.numHiddenNeurons + c.numSensorNeurons + c.numMotorNeurons - 1):
                motor_name = motor + c.numSensorNeurons + c.numHiddenNeurons
                if hid_sen_mot < motor_name:
                    target = hid_sen_mot
                else:
                    target = hid_sen_mot + 1
                pyrosim.Send_Synapse(sourceNeuronName=motor_name, targetNeuronName=target,
                                     weight=(self.rec_motor_weights[motor][hid_sen_mot]))

        for hidden in range(0, c.numHiddenNeurons):
            for hid_sen in range(0, c.numHiddenNeurons + c.numSensorNeurons - 1):
                hidden_name = hidden + c.numSensorNeurons
                if hid_sen < hidden_name:
                    target = hid_sen
                else:
                    target = hid_sen + 1
                pyrosim.Send_Synapse(sourceNeuronName=hidden_name, targetNeuronName=target,
                                     weight=(self.rec_hidden_weights[hidden][hid_sen]))

        for sensor in range(0, c.numSensorNeurons):
            for sen in range(0, c.numSensorNeurons - 1):
                if sen < sensor:
                    target = sen
                else:
                    target = sen + 1
                pyrosim.Send_Synapse(sourceNeuronName=sensor, targetNeuronName=target,
                                     weight=(self.rec_sensor_weights[sensor][sen]))

        pyrosim.End()

    def Set_ID(self, ID):
        self.myID = ID
