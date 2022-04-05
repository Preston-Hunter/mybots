from solution import SOLUTION
import constants as c
import copy
import os
class  PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del tmp*.txt")

        self.parents = {}
        self.nextAvailableID = 0
        for _ in range(c.populationSize):
            self.parents[_] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    def Evaluate(self, solutions, directOrGUI):
        for solution in solutions:
            solutions[solution].Start_Simulation(directOrGUI)
        for solution in solutions:
            solutions[solution].Wait_For_Simulation_To_End()

    def Evolve(self):
        self.Evaluate(self.parents, "DIRECT")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()



    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.Evaluate(self.children, "DIRECT")

        #self.Print()

        self.Select()



    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            child = copy.deepcopy(self.parents[parent])
            child.Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

            self.children[parent] = child
        # for child in self.children:
        #     print( "Child ", end = "")
        #     print(child)
        # exit()

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()


    def Select(self):
        # if child has better fitness (more negative number) replace parent with child
        for child in self.children:
            if self.children[child].fitness < self.parents[child].fitness:
                    self.parents[child] = self.children[child]


    def Show_Best(self):
        firstParent = True
        for parent in self.parents:
            if firstParent:
                bestParent = self.parents[parent]
                firstParent = False

            if self.parents[parent].fitness < bestParent.fitness:
                bestParent = self.parents[parent]

        print("Current Fitness: " + str(bestParent.fitness))
        bestParent.Evaluate("GUI")


    def Print(self):
        for parent in self.parents:
            print("\nParent fitness: " + str(self.parents[parent].fitness))
            print("Child Fitness: " + str(self.children[parent].fitness))
