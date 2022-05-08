import numpy
import matplotlib.pyplot
import constants as c
import sys
if len(sys.argv) >= 2:
    id = sys.argv[1]
else:
    id = ""

noCPG = numpy.load("generational_data/all_data_no_cpg" + id + ".npy")
CPG = numpy.load("generational_data/all_data_cpg" + id + ".npy")

print(CPG)
print(noCPG)
CPGMean = []
noCPGMean = []
CPGMean = numpy.mean(CPG, axis=0)
noCPGMean = numpy.mean(noCPG, axis=0)

print(CPGMean)

# for p in range(len(noCPG)):
#     noCPGMean.append(numpy.mean(noCPG[p,:]))
#
# for p in range(len(CPG)):
#     CPGMean.append(numpy.mean(CPG[p,:]))
#

matplotlib.pyplot.plot(noCPGMean, label="no cpg values", linewidth=2)

matplotlib.pyplot.plot(CPGMean, label="has cpg values", linewidth=2)

matplotlib.pyplot.legend()
matplotlib.pyplot.savefig("generational_data/fitness_plots/fitnessPlot"+id+".png")
matplotlib.pyplot.show()
