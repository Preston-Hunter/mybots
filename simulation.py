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
            self.robot.Act(step)


            # print(frontLegSensorValues[_])
            time.sleep(1.0 / 60)
            #print(_)
