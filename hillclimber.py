from solution import SOLUTION
import constants as c
import copy

class HILLCLIMBER:

    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate()
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()



    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        self.child.Evaluate()

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


    def Print(self):
        print("Parent fitness: " + str(self.parent.fitness) + " Child Fitness: " + str(self.child.fitness))