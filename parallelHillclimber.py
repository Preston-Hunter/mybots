from solution import SOLUTION
import constants as c
import copy
import os
class  PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.nndf")

        self.parents = {}
        self.nextAvailableID = 0
        for _ in range(c.populationSize):
            self.parents[_] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1


    def Evaluate(self):
        pass


    def Evolve(self):
        for parent in self.parents:
            self.parents[parent].Start_Simulation("DIRECT")
        for parent in self.parents:
            self.parents[parent].Wait_For_Simulation_To_End()


        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()



    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()
        #
        # self.children.Evaluate("DIRECT")
        #
        # self.Print()
        #
        # self.Select()



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
        if self.children.fitness < self.parent.fitness:
            self.parent = self.children


    def Show_Best(self):
        # print("Current Fitness: " + str(self.parent.fitness))
        #
        # self.parent.Evaluate("GUI")
        pass

    def Print(self):
        print("\nParent fitness: " + str(self.parent.fitness) + " Child Fitness: " + str(self.children.fitness))
