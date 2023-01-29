from simulation import SIMULATION
from world import WORLD
from robot import ROBOT
import pybullet as p
import sys

# sys.argv = python3 simulate.py DIRECT


# sys.argv[0] = 'python3' 
directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(directOrGUI, solutionID)

simulation.Run()

# Intersting what we do here
simulation.Get_Fitness()

