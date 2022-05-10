from simulation import SIMULATION
import sys
if len(sys.argv) >= 2:
    directOrGUI = sys.argv[1]
else:
    directOrGUI = "GUI"
if len(sys.argv) >= 3:
    solutionID = str(sys.argv[2])
else:
    solutionID = "0"
if len(sys.argv) >= 4:

    if str(sys.argv[3]) == "True":
        save_sensors = True
    else:
        save_sensors = False
else:
    save_sensors = False

if len(sys.argv) >= 5:
    cpg_tag = sys.argv[4]
else:
    cpg_tag = ""

if len(sys.argv) >= 6:
    printFitness = sys.argv[5]
    if printFitness == "1":
        printFitness = True
    else:
        printFitness = False
else:
    printFitness = False

simulation = SIMULATION(directOrGUI, solutionID, save_sensors, printFitness)
simulation.Run(cpg_tag)
# can be printed to print fitness
simulation.Get_Fitness()
