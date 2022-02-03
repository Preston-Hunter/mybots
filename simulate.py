import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)

for _ in range(100):
    p.stepSimulation()
    backLegSensorValues[_] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[_] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    print(frontLegSensorValues[_])
    time.sleep(1.0/60)
    #print(_)
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)

p.disconnect()