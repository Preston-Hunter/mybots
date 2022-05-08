import numpy
import matplotlib.pyplot
import sys

if len(sys.argv) >= 2:
    id = sys.argv[1]
else:
    id = ""

backFootCPGSensorValues = numpy.load("data/BackLowerLeg_cpg" + id + ".npy")
frontFootCPGSensorValues = numpy.load("data/FrontLowerLeg_cpg" + id + ".npy")
rightFootCPGSensorValues = numpy.load("data/RightLowerLeg_cpg" + id + ".npy")
leftFootCPGSensorValues = numpy.load("data/LeftLowerLeg_cpg" + id + ".npy")

backFootCPGSensorValues += 1
frontFootCPGSensorValues += 1
rightFootCPGSensorValues += 1
leftFootCPGSensorValues += 1

backFootCPGSensorValues *= 1 / 2.0
frontFootCPGSensorValues *= 2.0 / 2
rightFootCPGSensorValues *= 3.0 / 2
leftFootCPGSensorValues *= 4.0 / 2

matplotlib.pyplot.scatter([i for i in range(len(backFootCPGSensorValues))], backFootCPGSensorValues,
                          label="backfootCPG", linewidth=.01, marker=",", s=1)
matplotlib.pyplot.scatter([i for i in range(len(frontFootCPGSensorValues))], frontFootCPGSensorValues,
                          label="frontfootCPG", linewidth=.01, marker=",", s=1)
matplotlib.pyplot.scatter([i for i in range(len(rightFootCPGSensorValues))], rightFootCPGSensorValues,
                          label="rightkfootCPG", linewidth=.01, marker=",", s=1)
matplotlib.pyplot.scatter([i for i in range(len(leftFootCPGSensorValues))], leftFootCPGSensorValues,
                          label="leftfootCPG", linewidth=.01, marker=",", s=1)

# ------------------------------------------------------------no cpg------------------------------------------
backFootNoCPGSensorValues = numpy.load("data/BackLowerLeg_no_cpg" + id + ".npy")
frontFootNoCPGSensorValues = numpy.load("data/FrontLowerLeg_no_cpg" + id + ".npy")
rightFootNoCPGSensorValues = numpy.load("data/RightLowerLeg_no_cpg" + id + ".npy")
leftFootNoCPGSensorValues = numpy.load("data/LeftLowerLeg_no_cpg" + id + ".npy")

backFootNoCPGSensorValues += 1
frontFootNoCPGSensorValues += 1
rightFootNoCPGSensorValues += 1
leftFootNoCPGSensorValues += 1

backFootNoCPGSensorValues *= -1 / 2.0
frontFootNoCPGSensorValues *= -2.0 / 2
rightFootNoCPGSensorValues *= -3.0 / 2
leftFootNoCPGSensorValues *= -4.0 / 2

matplotlib.pyplot.scatter([i for i in range(len(backFootNoCPGSensorValues))], backFootNoCPGSensorValues,
                          label="backfoot", linewidth=.01, marker=",", s=1)
matplotlib.pyplot.scatter([i for i in range(len(frontFootNoCPGSensorValues))], frontFootNoCPGSensorValues,
                          label="frontfoot", linewidth=.01, marker=",", s=1)
matplotlib.pyplot.scatter([i for i in range(len(rightFootNoCPGSensorValues))], rightFootNoCPGSensorValues,
                          label="rightkfoot", linewidth=.01, marker=",", s=1)
matplotlib.pyplot.scatter([i for i in range(len(leftFootNoCPGSensorValues))], leftFootNoCPGSensorValues,
                          label="leftfoot", linewidth=.01, marker=",", s=1)


matplotlib.pyplot.scatter([0], [6], linewidth=.01, marker=",", s=1)

# legend area
matplotlib.pyplot.legend(loc='upper center', ncol=4)

matplotlib.pyplot.savefig("generational_data/footprints/footprint"+id+".png")
matplotlib.pyplot.show()
