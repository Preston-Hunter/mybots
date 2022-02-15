import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
sinusoidalValuesFront = numpy.load("data/sinusoidalValuesFront.npy")
sinusoidalValuesBack = numpy.load("data/sinusoidalValuesBack.npy")

# matplotlib.pyplot.plot(backLegSensorValues, label="backLeg", linewidth =4)
# matplotlib.pyplot.plot(frontLegSensorValues, label="frontLeg")
matplotlib.pyplot.plot(sinusoidalValuesFront, label="sinusoidal_values_front", linewidth =4)
matplotlib.pyplot.plot(sinusoidalValuesBack, label="sinusoidal_values_back", linewidth =4)

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
