import os
from hillclimber import HILLCLIMBER

# for _ in range(5):
#     os.system("python generate.py")
#     os.system("python simulate.py")
hc = HILLCLIMBER()

hc.Evolve()