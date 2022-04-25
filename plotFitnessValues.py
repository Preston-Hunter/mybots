import numpy
import matplotlib.pyplot

noCPG = numpy.load("all_data_no_cpg.npy")
CPG = numpy.load("all_data_cpg.npy")

matplotlib.pyplot.plot(noCPG, label="no cpg values", linewidth=2)
matplotlib.pyplot.plot(CPG, label="cpg values", linewidth=2)

matplotlib.pyplot.legend()
matplotlib.pyplot.show()