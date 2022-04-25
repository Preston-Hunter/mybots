import os
import rename_constants
from parallelHillclimber import  PARALLEL_HILL_CLIMBER

# for _ in range(5):
#     os.system("python generate.py")
#     os.system("python simulate.py")
# be sure to start program with constants_cpg.py existing
all_simulations_data_filename_cpg = "all_data_cpg.npy"
all_simulations_data_filename_no_cpg = "all_data_no_cpg.npy"
rename_constants.rename_constants_to_constants_with_cpg()



phc = PARALLEL_HILL_CLIMBER(False)

phc.Evolve()
#phc.Show_Best()
print("No cpg results")
phc.write_simulation_data_to_file(all_simulations_data_filename_no_cpg)
phc.print_best_fitness_of_each_generation()
print(phc.generation_fitness)


rename_constants.swap_names()

phc_cpg = PARALLEL_HILL_CLIMBER(True)

phc_cpg.Evolve()
#phc_cpg.Show_Best()
print("Has cpg results")
phc_cpg.write_simulation_data_to_file(all_simulations_data_filename_cpg)
print(phc_cpg.generation_fitness)
phc_cpg.print_best_fitness_of_each_generation()

rename_constants.swap_names()

