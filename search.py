import os
import rename_constants
from parallelHillclimber import  PARALLEL_HILL_CLIMBER

# for _ in range(5):
#     os.system("python generate.py")
#     os.system("python simulate.py")
phc = PARALLEL_HILL_CLIMBER(False)

phc.Evolve()
phc.Show_Best()
phc.print_fitness_of_each_generation()
phc.save_fitness_of_each_generation()

rename_constants.swap_names()

phc_cpg = PARALLEL_HILL_CLIMBER(True)

phc_cpg.Evolve()
phc_cpg.Show_Best()
phc_cpg.print_fitness_of_each_generation()
phc_cpg.save_fitness_of_each_generation()

rename_constants.swap_names()

