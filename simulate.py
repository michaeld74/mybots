from simulation import SIMULATION
from world import WORLD
from robot import ROBOT
import pybullet as p



simulation = SIMULATION()


SIMULATION.Run()



# import pybullet as p
# import time
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import numpy
# import random
# import constants as c


# physicsClient = p.connect(p.GUI)

# p.setAdditionalSearchPath(pybullet_data.getDataPath())

# # Create Gravity, Floor, body, and world block
# p.setGravity(0,0,-9.8)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")

# pyrosim.Prepare_To_Simulate(robotId)

# # Create empty vectors to fill with sensor data
# backLegSensorValues = numpy.zeros(c.loop)
# frontLegSensorValues = numpy.zeros(c.loop)

# # amplitude, frequency and offset variables (moved to constants)
# # amplitude = numpy.pi/4
# # frequency = 10
# # phaseOffset = 0

# # Create Target angle array for back and front leg motors
# targetAnglesBackLeg = c.amplitude*numpy.sin(c.frequency*(numpy.linspace(0, numpy.pi*2, 1000)) + c.phaseOffset)
# targetAnglesFrontLeg = c.amplitude*numpy.sin(c.frequency*(numpy.linspace(0, numpy.pi*2, 1000)) + numpy.pi/4)

# numpy.save('data/sinVals.npy',targetAnglesBackLeg,targetAnglesFrontLeg)


# # Simulation Runs
# for i in range(c.loop):
#     time.sleep(.0005)
#     p.stepSimulation()

#     # Record back and front leg data at each step
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

#     # Motors
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = b"Torso_BackLeg",
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = targetAnglesBackLeg[i],
#         maxForce = c.maxForce)

#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex = robotId,
#         jointName = b"Torso_FrontLeg",
#         controlMode = p.POSITION_CONTROL,
#         targetPosition = targetAnglesFrontLeg[i],#random.uniform(-3.1415/2.0, 3.1415/2.0),
#         maxForce = c.maxForce)

#     print(i)


# # print(backLegSensorValues)

# # print(frontLegSensorValues)

# # Save the data to numpy
# numpy.save('data/backLegVals.npy',backLegSensorValues)

# numpy.save('data/frontLegVals.npy',frontLegSensorValues)


# p.disconnect()
