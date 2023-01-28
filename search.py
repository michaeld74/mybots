import os
from hillclimber import HILL_CLIMBER


hc = HILL_CLIMBER()

hc.Evolve()
hc.Show_Best()

# HILL_CLIMBER.Evolve()


# for i in range(5):
#     os.system('python3 ../mybots/generate.py')
#     os.system('python3 ../mybots/simulate.py')