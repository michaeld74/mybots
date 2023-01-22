import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy

class MOTOR:

    def __init__(self, jointName, robotId):
        self.robotId = robotId
        self.jointName = jointName
        # self.sensors = {}
        # self.values = numpy.zeros(c.loop)

   

    def Set_Value(self, desiredAngle):
        # Motors
        
        pyrosim.Set_Motor_For_Joint(
            
            bodyIndex = self.robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = c.maxForce)
        # print(self.motorValues[desiredAngle], 'aa')

