import pybullet as p
import pyrosim.pyrosim as pyrosim


class WORLD:

    def __init__(self):
        p.loadSDF("world.sdf")
        self.planeId = p.loadURDF("plane.urdf")

