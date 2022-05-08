import os
import master_constants as m
for i in range(m.numABTrials):
    data_tag = str(i)
    os.system("python search.py 0 " + data_tag)
