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

simulation = SIMULATION(directOrGUI, solutionID, save_sensors)
simulation.Run(cpg_tag)
# can be printed to print fitness
simulation.Get_Fitness()
