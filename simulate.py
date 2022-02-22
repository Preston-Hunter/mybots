from simulation import SIMULATION
# import pyrosim.pyrosim as pyrosim
# import numpy as numpy
# import constants as c
#


#
#
# amplitudeFront = c.amplitudeFront
# frequencyFront = c.frequencyFront
# phaseOffsetFront = c.phaseOffsetFront
#
# amplitudeBack = c.amplitudeBack
# frequencyBack = c.frequencyBack
# phaseOffsetBack = c.phaseOffsetBack
#
#
# runtime = 1000
#
# frontLegSensorValues = numpy.zeros(runtime)
#
# # Sinusoidal vector
# target_angles = numpy.linspace(0, 2 * numpy.pi, runtime)
# target_angles_front = numpy.sin(frequencyFront * target_angles + phaseOffsetFront) * amplitudeFront
# target_angles_back = numpy.sin(frequencyBack * target_angles + phaseOffsetBack) * amplitudeBack
#
# numpy.save("data/sinusoidalValuesFront.npy", target_angles_front)
# numpy.save("data/sinusoidalValuesBack.npy", target_angles_back)
# # exit()

#
# numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
# numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
# numpy.save("data/sinusoidalValues.npy", target_angles)
simulation = SIMULATION()
simulation.Run()

