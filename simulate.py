import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

amplitude = numpy.pi / 4.0
frequency = 1
phaseOffset = 0

runtime = 1000

backLegSensorValues = numpy.zeros(runtime)
frontLegSensorValues = numpy.zeros(runtime)

# Sinusoidal vector
target_angles = numpy.linspace(0, 2 * numpy.pi, runtime)
target_angles = numpy.sin(frequency * target_angles + phaseOffset) * amplitude

for _ in range(runtime):
    p.stepSimulation()
    backLegSensorValues[_] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[_] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=target_angles[_],
        maxForce=40)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=target_angles[_],
        maxForce=40)
    print(frontLegSensorValues[_])
    time.sleep(1.0 / 60)
    # print(_)

numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
numpy.save("data/sinusoidalValues.npy", target_angles)

p.disconnect()
