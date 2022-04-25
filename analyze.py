import numpy
import matplotlib.pyplot

# backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
# frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
# sinusoidalValuesFront = numpy.load("data/sinusoidalValuesFront.npy")
# sinusoidalValuesBack = numpy.load("data/sinusoidalValuesBack.npy")

noCPG = numpy.load("all_data_no_cpg.npy")
CPG = numpy.load("all_data_cpg.npy")

# matplotlib.pyplot.plot(backLegSensorValues, label="backLeg", linewidth =4)
# matplotlib.pyplot.plot(frontLegSensorValues, label="frontLeg")
# matplotlib.pyplot.plot(sinusoidalValuesFront, label="sinusoidal_values_front", linewidth =2)
# matplotlib.pyplot.plot(sinusoidalValuesBack, label="sinusoidal_values_back", linewidth =2)

matplotlib.pyplot.plot(noCPG, label="no cpg values", linewidth=2)
matplotlib.pyplot.plot(CPG, label="cpg values", linewidth=2)

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
