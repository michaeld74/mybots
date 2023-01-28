from solution import SOLUTION
import constants as c
import copy
import os

class HILL_CLIMBER:

    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate()
        os.system("python3 simulate.py GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        # pass

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
        os.system("python3 simulate.py GUI")