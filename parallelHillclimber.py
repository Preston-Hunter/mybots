from solution import SOLUTION
import constants as c
import copy

class  PARALLEL_HILL_CLIMBER:

    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        for _ in range(c.populationSize):
            self.parents[_] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        for parent in self.parents:
            self.parents[parent].Evaluate("GUI")
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()

        pass


    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.children.Evaluate("DIRECT")

        self.Print()

        self.Select()



    def Spawn(self):
        self.children = copy.deepcopy(self.parent)
        for child in self.children:
            self.children[child].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1


    def Mutate(self):
        self.children.Mutate()


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
