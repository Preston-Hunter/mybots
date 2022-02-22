from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time


class SIMULATION:

    def __init__(self):
        self.runtime = 10000

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)

        self.world = WORLD()
        self.robot = ROBOT(self.runtime)

        pyrosim.Prepare_To_Simulate(0)


    def __del__(self):
        p.disconnect()

    def Run(self):
        for step in range(self.runtime):
            p.stepSimulation()
            self.robot.Sense(step)

            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex=robotId,
            #     jointName="Torso_BackLeg",
            #     controlMode=p.POSITION_CONTROL,
            #     targetPosition=target_angles_back[_],
            #     maxForce=40)
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex=robotId,
            #     jointName="Torso_FrontLeg",
            #     controlMode=p.POSITION_CONTROL,
            #     targetPosition=target_angles_front[_],
            #     maxForce=40)
            # print(frontLegSensorValues[_])
            time.sleep(1.0 / 60)
            #print(_)
