import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Create Gravity, Floor, body, and world block
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")

robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

# Create empty vectors to fill with sensor data

backLegSensorValues = numpy.zeros(1000)

frontLegSensorValues = numpy.zeros(1000)

# Simulation Runs
for i in range(1000):
    time.sleep(.0005)
    p.stepSimulation()
    
    # Record back and front leg data at each step
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    print(i)

print(backLegSensorValues)

print(frontLegSensorValues)

# Save the data to numpy
numpy.save('data/backLegVals.npy',backLegSensorValues)

numpy.save('data/frontLegVals.npy',frontLegSensorValues)



p.disconnect()
