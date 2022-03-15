from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time

class SIMULATION:

    def __init__(self):
        self.runtime = 180

        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)

        self.world = WORLD()
        self.robot = ROBOT(self.runtime)



    def __del__(self):
        # todo call save values?
        p.disconnect()

    def Run(self):
        for step in range(self.runtime):
            p.stepSimulation()

            self.robot.Sense(step)
            self.robot.Think()
            self.robot.Act(step)

            print(step)
            time.sleep(1.0 / 60)
