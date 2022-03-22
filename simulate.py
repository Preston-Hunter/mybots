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
simulation = SIMULATION(directOrGUI, solutionID)
simulation.Run()
print(simulation.Get_Fitness())

