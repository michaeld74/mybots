import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import constants as c
import numpy
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os




# physicsClient = p.connect(p.GUI)

class ROBOT:

    def __init__(self, solutionID):
        self.solutionID = solutionID

        self.robotId = p.loadURDF("body.urdf")
        self.motors = {}
        # self.nn = NEURAL_NETWORK("brain.nndf")
        self.nn = NEURAL_NETWORK("brain" + str(solutionID) + ".nndf")
        os.system("rm brain" + str(solutionID) + ".nndf")

        #Deletes
        # 
    
        

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
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        xCoordinateOfLinkZero = stateOfLinkZero[0][0]
        print(xCoordinateOfLinkZero, 'xcoord')
        # print('ujn')

        f = open("tmp" + self.solutionID + ".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()
        os.system("mv tmp" + self.solutionID + ".txt fitness" + self.solutionID + ".txt")
        




           

        

 
