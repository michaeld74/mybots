from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        os.system("rm brain*.nndf")
        os.system("rm fitness*.nndf")
        # os.system("rm brain" + str(solutionID) + ".nndf")
        # self.parent = SOLUTION()
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
            # print(self.parents)
        
        

    def Evolve(self):
        self.Evaluate(self.parents)
        # exit()
        # for i in range(c.populationSize):
        #     self.parents[i].Start_Simulation('DIRECT ' + str(i))
        #     print('fields')
        # for i in range(c.populationSize):
        #     # pass
        #     self.parents[i].Wait_For_Simulation_To_End()
        # self.parent.Evaluate()
        # os.system("python3 simulate.py GUI")
        for j in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        
        self.Print()
        self.Select()
        

    def Spawn(self):
        self.children = {}
        for i in range(len(self.parents)):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        # print(self.children, 'eivbuebvyu')
        # exit()
        # self.child = copy.deepcopy(self.parent)
        # self.child.Set_ID(self.nextAvailableID)
        # self.nextAvailableID += 1

    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()
        # print(self.child.weights, 'scw')
        # print(self.parent.weights, 'spw')
        # exit()

    def Evaluate(self, solutions):
        for i in solutions:
            solutions[i].Start_Simulation("DIRECT")
        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()

    def Select(self):
        
        for i in self.children:
            # print(self.children[i])
            if self.children[i].fitness > self.parents[i].fitness:
                self.parents[i] = self.children[i]
        
        # print(self.parent.fitness,'pf')
        # print(self.child.fitness, 'cf')
        
    def Print(self):
        for i in self.parents:
            print("Fitty:", self.parents[i].fitness, self.children[i].fitness)

    def Show_Best(self):
        # os.system("python3 simulate.py GUI")
        print('openses')
        
        z = 0
        val = self.parents[0].fitness
        for i in self.parents:
            print(val, self.parents[i].fitness, 'comparing')
            if val < self.parents[i].fitness:
                val = self.parents[i].fitness
                z = i
        print(z, self.parents[z].fitness, 'final')
        self.parents[z].Start_Simulation("GUI")