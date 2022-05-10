from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import pyrosim.pyrosim as pyrosim
import time

class SIMULATION:

    def __init__(self, directOrGUI, solutionID, save_sensors, printFitness):
        self.printFitness = printFitness
        self.save_sensors = save_sensors

        self.runtime = c.runtime
        #bool variable made by me, in order to have Drect run fast
        # and have GUI use time pause to have gui visible
        self.GUI = True

        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
            self.GUI = False
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)

        self.world = WORLD()
        self.robot = ROBOT(self.runtime, solutionID)

        if solutionID == "-1": # print neurons here. -1 will print nothing
            self.robot.nn.print_synapses(self.robot.nn.neurons)



    def __del__(self):
        # todo call save values?
        p.disconnect()

    def Run(self, cpg_tag):
        for step in range(self.runtime):
            p.stepSimulation()

            self.robot.Sense(step)
            self.robot.Think(step)
            self.robot.Act(step)

            # print(step)
            if self.GUI:
                time.sleep(1.0 / 60)
        if self.save_sensors:
            self.robot.Save_Foot_Sensors(cpg_tag)
        if self.printFitness:
            print(self.Get_Fitness())


    def Get_Fitness(self):
        return self.robot.Get_Fitness()
