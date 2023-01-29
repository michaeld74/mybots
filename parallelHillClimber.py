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
        for i in range(c.populationSize):
            self.parents[i].Start_Simulation('DIRECT ' + str(i))
        for i in range(c.populationSize):
            # pass
            self.parents[i].Wait_For_Simulation_To_End()
        # self.parent.Evaluate()
        # os.system("python3 simulate.py GUI")
        for j in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        pass

    def Evolve_For_One_Generation(self):
        self.Spawn()
        
        
        # self.Mutate()
        # self.child.Evaluate()
        # self.Print()
        # self.Select()
        

    def Spawn(self):
        self.children = {}
        for i in range(len(self.parents)):
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        print(self.children, 'eivbuebvyu')
        exit()
        # self.child = copy.deepcopy(self.parent)
        # self.child.Set_ID(self.nextAvailableID)
        # self.nextAvailableID += 1

    def Mutate(self):
        self.child.Mutate()
        # print(self.child.weights, 'scw')
        # print(self.parent.weights, 'spw')
        # exit()

    def Select(self):
        if self.parent.fitness < self.child.fitness:
            self.parent = self.child
        # print(self.parent.fitness,'pf')
        # print(self.child.fitness, 'cf')
        
    def Print(self):
        print(self.parent.fitness, self.child.fitness, 'parent, child')

    def Show_Best(self):
        # os.system("python3 simulate.py GUI")
        pass