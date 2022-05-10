import solution
import numpy

best_solutions = []

bestCPG = "22"
bestNoCPG = "28"
evolved = "1"
# ------------------------- cpg solution -----------------------------

bestCPGID = "_cpg_" + bestCPG
cpg_sol = solution.SOLUTION(0, True)
cpg_sol.sensor_weights = numpy.load("best_robots/sensor_weights" + bestCPGID + ".npy")
cpg_sol.motor_weights = numpy.load("best_robots/motor_weights" + bestCPGID + ".npy")

cpg_sol.sensor_self_weights = numpy.load("best_robots/sensor_self_weights" + bestCPGID + ".npy")
cpg_sol.motor_self_weights = numpy.load("best_robots/motor_self_weights" + bestCPGID + ".npy")
cpg_sol.hidden_self_weights = numpy.load("best_robots/hidden_self_weights" + bestCPGID + ".npy")

cpg_sol.rec_sensor_weights = numpy.load("best_robots/rec_sensor_weights" + bestCPGID + ".npy")
cpg_sol.rec_hidden_weights = numpy.load("best_robots/rec_hidden_weights" + bestCPGID + ".npy")
cpg_sol.rec_motor_weights = numpy.load("best_robots/rec_motor_weights" + bestCPGID + ".npy")

best_solutions.append(cpg_sol)

# ------------------------- no cpg solution -----------------------------
bestNoCPGID = "_no_cpg_" + bestNoCPG
no_cpg_sol = solution.SOLUTION(1, False)
no_cpg_sol.sensor_weights = numpy.load("best_robots/sensor_weights" + bestNoCPGID + ".npy")
no_cpg_sol.motor_weights = numpy.load("best_robots/motor_weights" + bestNoCPGID + ".npy")

no_cpg_sol.sensor_self_weights = numpy.load("best_robots/sensor_self_weights" + bestNoCPGID + ".npy")
no_cpg_sol.motor_self_weights = numpy.load("best_robots/motor_self_weights" + bestNoCPGID + ".npy")
no_cpg_sol.hidden_self_weights = numpy.load("best_robots/hidden_self_weights" + bestNoCPGID + ".npy")

no_cpg_sol.rec_sensor_weights = numpy.load("best_robots/rec_sensor_weights" + bestNoCPGID + ".npy")
no_cpg_sol.rec_hidden_weights = numpy.load("best_robots/rec_hidden_weights" + bestNoCPGID + ".npy")
no_cpg_sol.rec_motor_weights = numpy.load("best_robots/rec_motor_weights" + bestNoCPGID + ".npy")

best_solutions.append(no_cpg_sol)
# ------------------------- evolved -----------------------------
evolvedID = "_no_cpg_" + evolved
evolved_sol = solution.SOLUTION(1, False)
evolved_sol.sensor_weights = numpy.load("best_robots/sensor_weights" + evolvedID + ".npy")
evolved_sol.motor_weights = numpy.load("best_robots/motor_weights" + evolvedID + ".npy")

evolved_sol.sensor_self_weights = numpy.load("best_robots/sensor_self_weights" + evolvedID + ".npy")
evolved_sol.motor_self_weights = numpy.load("best_robots/motor_self_weights" + evolvedID + ".npy")
evolved_sol.hidden_self_weights = numpy.load("best_robots/hidden_self_weights" + evolvedID + ".npy")

evolved_sol.rec_sensor_weights = numpy.load("best_robots/rec_sensor_weights" + evolvedID + ".npy")
evolved_sol.rec_hidden_weights = numpy.load("best_robots/rec_hidden_weights" + evolvedID + ".npy")
evolved_sol.rec_motor_weights = numpy.load("best_robots/rec_motor_weights" + evolvedID + ".npy")

#best_solutions.append(evolved_sol)

rand_sol = solution.SOLUTION(2, False)
#rand_sol.Start_Simulation_Linear("GUI")

for solution in best_solutions:
    solution.Start_Simulation("GUI")
