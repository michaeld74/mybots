import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import sys


phc = PARALLEL_HILL_CLIMBER()

# directOrGUI = sys.argv[1]

phc.Evolve()
phc.Show_Best()

# HILL_CLIMBER.Evolve()


# for i in range(5):
#     os.system('python3 ../mybots/generate.py')
#     os.system('python3 ../mybots/simulate.py')