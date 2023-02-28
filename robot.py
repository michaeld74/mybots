import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from world import WORLD
import constants as c
import numpy
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import math



# physicsClient = p.connect(p.GUI)

class ROBOT:

    def __init__(self, solutionID):
        self.solutionID = solutionID
        # self.world = p.loadSDF("world.sdf")
        self.ball = p.loadURDF("ball.urdf")
        self.robotId = p.loadURDF("body.urdf")
        self.motors = {}
        # self.nn = NEURAL_NETWORK("brain.nndf")
        # self.nn = NEURAL_NETWORK("brain.nndf")
        # os.system("rm brain.nndf")
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        os.system("rm brain" + str(solutionID) + ".nndf")

        # print(self.robotId,'sri')
        # print(self.ball,'sri')


    

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
        # print('test')
        for self.jointName in pyrosim.jointNamesToIndices:
            self.motors[self.jointName] = MOTOR(self.jointName, robot)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                print(neuronName)
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(desiredAngle)
                # jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)

                # print('neuron, joint, angle: ',neuronName, jointName, desiredAngle)
            # self.motors[jointName].Set_Value(desiredAngle)

        #Motion
        # for jointName in self.motors:
        

    def Think(self):
        self.nn.Update()
        # self.nn.Print()
        
    def Get_Fitness(self):
        
        # stateOfLinkZero = p.getLinkState(self.robotId,0)
        # basePositionAndOrientation1 = p.getBasePositionAndOrientation(self.ball)
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.ball)
        # basePositionAndOrientation = p.getBasePositionAndOrientation(WORLD.ball)
        basePositionAndOrientation1 = p.getBasePositionAndOrientation(self.robotId)
        # print(p.getBasePositionAndOrientation(self.ball))
        basePosition = basePositionAndOrientation[0]
        basePosition1 = basePositionAndOrientation1[0]
        # basePosition1 = basePositionAndOrientation1[0]

        # xCoordinateOfLinkZero = basePosition[0]*2+basePosition1[0]
        xCoordinateOfLinkZero = 1#basePosition1[1]
        
        # if basePosition[2] > 1:
        #     xCoordinateOfLinkZero = basePosition[0]+basePosition1[0]
        #     # xCoordinateOfLinkZero = basePosition1[0]**2
        # else:
        #     xCoordinateOfLinkZero = -3

        # basePosition = basePositionAndOrientation[0]
        # xPosition = basePosition[0]
        # print(solutionID)
        # print('ujn')
        
        print('cheerioooo')
        f = open("tmp" + self.solutionID + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.system("mv tmp" + self.solutionID + ".txt fitness" + self.solutionID + ".txt")
        
        




           

        

 
