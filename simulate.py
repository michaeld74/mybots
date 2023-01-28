from simulation import SIMULATION
from world import WORLD
from robot import ROBOT
import pybullet as p
import sys

# sys.argv = python3 simulate.py DIRECT


# sys.argv[0] = 'python3' 
directOrGUI = sys.argv[1]

simulation = SIMULATION(directOrGUI)

simulation.Run()

simulation.Get_Fitness()

