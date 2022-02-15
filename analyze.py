import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
sinusoidal_values = numpy.load("data/sinusoidalValues.npy")

# matplotlib.pyplot.plot(backLegSensorValues, label="backLeg", linewidth =4)
# matplotlib.pyplot.plot(frontLegSensorValues, label="frontLeg")
matplotlib.pyplot.plot(sinusoidal_values, label="sinusoidal_values", linewidth =4)

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
