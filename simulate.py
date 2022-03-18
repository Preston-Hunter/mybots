from simulation import SIMULATION
import sys
if len(sys.argv) >= 2:
    directOrGUI = sys.argv[1]
else:
    directOrGUI = "GUI"
simulation = SIMULATION(directOrGUI)
simulation.Run()
print(simulation.Get_Fitness())

