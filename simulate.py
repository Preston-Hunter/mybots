import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import random
import matplotlib
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

runtime = 100

backLegSensorValues = numpy.zeros(runtime)
frontLegSensorValues = numpy.zeros(runtime)

# Sinusoidal vector
sinusoidal_values = numpy.linspace(0, 2*numpy.pi, runtime)
sinusoidal_values = numpy.sin(sinusoidal_values)
matplotlib.pyplot.plot(sinusoidal_values, label="sinusoidal_values", linewidth =4)

for _ in range(runtime):
    p.stepSimulation()
    backLegSensorValues[_] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[_] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_BackLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=(random.random() - 0.5) * numpy.pi,
        maxForce=40)
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Torso_FrontLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=(random.random() - 0.5) * numpy.pi,
        maxForce=40)
    print(frontLegSensorValues[_])
    time.sleep(1.0 / 60)
    # print(_)

numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)

p.disconnect()
