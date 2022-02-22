import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p


class MOTOR:

    def __init__(self, jointName, runtime, robotId):
        self.jointName = jointName
        self.Prepare_to_Act(runtime)
        self.robotId = robotId

    def Prepare_to_Act(self, runtime):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset

        self.motorValues = numpy.linspace(0, 2 * numpy.pi, runtime)
        self.motorValues = numpy.sin(self.frequency * self.motorValues + self.offset) * self.amplitude

    def Set_Value(self, step):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=self.robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[step],
            maxForce=40)

    def Save_Values(self):
        save_location = "data/" + self.jointName + "MotorValues.npy"
        numpy.save(save_location, self.motorValues)
