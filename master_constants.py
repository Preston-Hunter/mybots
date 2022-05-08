import numpy


numABTrials = 30
runWhile = False

# ---------------------------------Below are also in child constants files-------------------------

numSensorNeuronsWithCPG = 10

runtime = 1000

amplitude = numpy.pi / 4.0
frequency = 8
phaseOffset = 0

amplitudeBack = numpy.pi / 4.0
frequencyBack = 10
phaseOffsetBack = -numpy.pi / 4.0

numberOfGenerations = 20
populationSize = 20

numSensorNeurons = numSensorNeuronsWithCPG - 1
numMotorNeurons = 8
numHiddenNeurons = 9

motorJointRange = 0.2

x = .8

scale = 1
