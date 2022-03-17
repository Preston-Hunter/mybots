from solution import SOLUTION
import constants as c
import copy

class HILLCLIMBER:

    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()




    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.child.Evaluate("DIRECT")

        self.Print()

        self.Select()



    def Spawn(self):
        self.child = copy.deepcopy(self.parent)


    def Mutate(self):
        self.child.Mutate()


    def Select(self):
        # if child has better fitness (more negative number) replace parent with child
        if self.child.fitness < self.parent.fitness:
            self.parent = self.child


    def Show_Best(self):
        print("Current Fitness: " + str(self.parent.fitness))

        self.parent.Evaluate("GUI")

    def Print(self):
        print("\nParent fitness: " + str(self.parent.fitness) + " Child Fitness: " + str(self.child.fitness))