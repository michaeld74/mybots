import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy

class MOTOR:

    def __init__(self, jointName, robotId):
        self.robotId = robotId
        self.jointName = jointName
        # self.sensors = {}
        self.Prepare_To_Act()
        # self.values = numpy.zeros(c.loop)

    def Prepare_To_Act(self):
        self.frequency = c.frequency
        self.amplitude = c.amplitude
        self.offset = c.phaseOffset
        if self.jointName == b'Torso_BackLeg':
            self.frequency = 3

        self.motorValues = self.amplitude*numpy.sin(self.frequency*(numpy.linspace(0, numpy.pi*2, 1000)) + self.offset)
        # if self.jointName == b'Torso_BackLeg':
        #     self.frequency = 3
        # targetAnglesBackLeg = c.amplitude*numpy.sin(c.frequency*(numpy.linspace(0, numpy.pi*2, 1000)) + c.phaseOffset)

   

    def Set_Value(self, t):
        # Motors
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = self.robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[t],
            maxForce = c.maxForce)

