import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p


class MOTOR:

    def __init__(self, jointName, runtime, robotId):
        self.jointName = jointName
        #self.Prepare_to_Act(runtime)
        self.robotId = robotId

    def Set_Value(self, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=self.robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=40)

    # def Save_Values(self):
    #     save_location = "data/" + self.jointName + "MotorValues.npy"
    #     numpy.save(save_location, self.motorValues)
