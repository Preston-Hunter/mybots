from simulation import SIMULATION



#
#
# frontLegSensorValues = numpy.zeros(runtime)
#
# # Sinusoidal vector
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

