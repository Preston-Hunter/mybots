import numpy
import matplotlib.pyplot

backFootCPGSensorValues = numpy.load("data/BackLowerLeg_cpg.npy")
frontFootCPGSensorValues = numpy.load("data/FrontLowerLeg_cpg.npy")
rightFootCPGSensorValues = numpy.load("data/RightLowerLeg_cpg.npy")
leftFootCPGSensorValues = numpy.load("data/LeftLowerLeg_cpg.npy")

backFootCPGSensorValues += 1
frontFootCPGSensorValues += 1
rightFootCPGSensorValues += 1
leftFootCPGSensorValues += 1

backFootCPGSensorValues *= 1/2.0
frontFootCPGSensorValues *= 2.0 / 2
rightFootCPGSensorValues *= 3.0 / 2
leftFootCPGSensorValues *= 4.0 / 2


backFootNoCPGSensorValues = numpy.load("data/BackLowerLeg_no_cpg.npy")
frontFootNoCPGSensorValues = numpy.load("data/FrontLowerLeg_no_cpg.npy")
rightFootNoCPGSensorValues = numpy.load("data/RightLowerLeg_no_cpg.npy")
leftFootNoCPGSensorValues = numpy.load("data/LeftLowerLeg_no_cpg.npy")

backFootNoCPGSensorValues += 1
frontFootNoCPGSensorValues += 1
rightFootNoCPGSensorValues += 1
leftFootNoCPGSensorValues += 1

backFootNoCPGSensorValues *= 1/2.0
frontFootNoCPGSensorValues *= 2.0 / 2
rightFootNoCPGSensorValues *= 3.0 / 2
leftFootNoCPGSensorValues *= 4.0 / 2

matplotlib.pyplot.plot(backFootCPGSensorValues, label="backfoot", linewidth =1)
matplotlib.pyplot.plot(frontFootCPGSensorValues, label="frontfoot", linewidth =1)
matplotlib.pyplot.plot(rightFootCPGSensorValues, label="rightkfoot", linewidth =1)
matplotlib.pyplot.plot(leftFootCPGSensorValues, label="leftfoot", linewidth =1)



# matplotlib.pyplot.plot(backFootNoCPGSensorValues, label="backfoot", linewidth =1)
# matplotlib.pyplot.plot(frontFootNoCPGSensorValues, label="frontfoot", linewidth =1)
# matplotlib.pyplot.plot(rightFootNoCPGSensorValues, label="rightkfoot", linewidth =1)
# matplotlib.pyplot.plot(leftFootNoCPGSensorValues, label="leftfoot", linewidth =1)


matplotlib.pyplot.legend()
matplotlib.pyplot.show()
