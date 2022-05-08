import os
import master_constants as m

run_while = m.runWhile

#clear existing exceptions file
exception_triggered_file = open("exception.txt", "w")
exception_triggered_file.close()


if not run_while:
    # this for loop runs a set amount of times
    for i in range(m.numABTrials):
        data_tag = str(i)
        os.system("python search.py " + data_tag)
else:
    # this while loop runs until user deletes this file
    i = 0
    while os.path.exists("user_away.txt"):
        data_tag = str(i)
        os.system("python search.py " + data_tag)
        i += 1
    print("done, ran " + str(i) + " times")