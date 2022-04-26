from solution import SOLUTION
import numpy
import constants as c
import copy
import os


class PARALLEL_HILL_CLIMBER:

    def __init__(self, useCPG):
        dim1 = c.numberOfGenerations
        dim2 = c.populationSize
        output = [[0.0 for i in range(dim1)] for j in range(dim2)]
        self.generation_fitness = numpy.array(output)





        self.useCPG = useCPG
        self.current_generation = 0
        self.best_parents = []
        self.best_of_each_generation_fitness = []
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del tmp*.txt")

        self.parents = {}
        self.nextAvailableID = 0
        for _ in range(c.populationSize):
            self.parents[_] = SOLUTION(self.nextAvailableID, self.useCPG)
            self.nextAvailableID += 1

    def Evaluate(self, solutions, directOrGUI):
        for solution in solutions:
            solutions[solution].Start_Simulation(directOrGUI)
        for solution in solutions:
            solutions[solution].Wait_For_Simulation_To_End()

    def Evolve(self):
        n = self.current_generation
        self.Evaluate(self.parents, "DIRECT")

        # self.initialize_all_generations_fitness_data(all_simulations_data_filename)
        self.save_best_from_current_generation(n)
        for currentGeneration in range(c.numberOfGenerations):
            self.current_generation += 1
            n = self.current_generation
            self.Evolve_For_One_Generation(n)

    # todo should this be done on parents?
    def save_all_generations_fitness_data(self, generation):
        # file = open(filename, "a")
        # file.write("generation " + str(generation) + ",")
        current_member = 0
        for parent in self.parents:
            self.generation_fitness[current_member, generation - 1] = self.parents[parent].fitness
            current_member += 1

        #     fitness = self.children[child].fitness
        #     file.write(str(fitness) + ",")
        # file.write("\n")
        # file.close()
    #
    # def initialize_all_generations_fitness_data(self, filename):
    #     file = open(filename, "w")
    #     file.write(",population_member\n")
    #     for index in range(len(self.parents)):
    #         if index != len(self.parents) - 1:
    #             file.write(str(index) + ",")
    #         else:
    #             file.write(str(index) + ",\n")
    #     for parent in self.parents:
    #         fitness = self.parents[parent].fitness
    #         file.write(str(fitness) + ",")
    #
    #     file.write("\n")
    #     file.close()

    def Evolve_For_One_Generation(self, generation):
        self.Spawn()

        self.Mutate()

        self.Evaluate(self.children, "DIRECT")

        # self.Print()

        self.Select()

        self.save_all_generations_fitness_data(generation)


        self.save_best_from_current_generation(generation)


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

    def return_Best(self):
        firstParent = True
        for parent in self.parents:
            if firstParent:
                bestParent = self.parents[parent]
                firstParent = False

            if self.parents[parent].fitness < bestParent.fitness:
                bestParent = self.parents[parent]

        return bestParent


    def save_best_from_current_generation(self, generation):
        firstParent = True
        for parent in self.parents:
            if firstParent:
                bestParent = self.parents[parent]
                firstParent = False

            if self.parents[parent].fitness < bestParent.fitness:
                bestParent = self.parents[parent]

        bestParent.generation = generation
        self.best_parents.append(bestParent)
        self.best_of_each_generation_fitness.append(bestParent.fitness)

    def save_best_fitness_of_each_generation(self, output_filename):

        allFitnessesFile = open(output_filename, "w")

        for i in range(len(self.best_of_each_generation_fitness)):
            if i != len(self.best_of_each_generation_fitness) - 1:
                allFitnessesFile.write(str(i) + ",")
            else:
                allFitnessesFile.write(str(i) + "\n")

        for i in range(len(self.best_of_each_generation_fitness)):
            if i != len(self.best_of_each_generation_fitness) - 1:
                allFitnessesFile.write(str(self.best_of_each_generation_fitness[i]) + ",")
            else:
                allFitnessesFile.write(str(self.best_of_each_generation_fitness[i]))

        allFitnessesFile.close()

    def write_simulation_data_to_file(self, file_name):
        numpy.save(file_name, self.generation_fitness)

    def print_best_fitness_of_each_generation(self):
        print(self.best_of_each_generation_fitness)

    def Print(self):
        for parent in self.parents:
            print("\nParent fitness: " + str(self.parents[parent].fitness))
            print("Child Fitness: " + str(self.children[parent].fitness))
