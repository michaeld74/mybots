import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import constants as c
import numpy


# physicsClient = p.connect(p.GUI)

class ROBOT:

    def __init__(self):

        self.robotId = p.loadURDF("body.urdf")
        self.motors = {}
        

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
           
            # print(self.values)
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        # print(self.sensors)
        # print('blah')
        # Check this
        for s in self.sensors:
            self.sensors[s].Get_Value(t)
            # print(self.sensors[s].Get_Value(t))

    def Prepare_To_Act(self, robot):
        print('test')
        for self.jointName in pyrosim.jointNamesToIndices:
            self.motors[self.jointName] = MOTOR(self.jointName, robot)

    def Act(self, t):
        # print(self.motors)
        for jointName in self.motors:
            self.motors[jointName].Set_Value(t)
           

        

 
