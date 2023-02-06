import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c


class SOLUTION:

    def __init__(self, nextAvailableID):
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons) #* 2 - 1
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID
        # self.Create_Brain()
        
    
    def Evaluate(self, directOrGUI):
        pass
        
        # os.system("python3 simulate.py GUI")
        
        # os.system('python3 ../mybots/simulate.py')
        
        # python simulate.py

    def Start_Simulation(self, directOrGUI):
        
        self.Create_Ball()
        self.Create_Brain()
        self.Create_Body()
        self.Create_World()
        
        # print('jtan1')
        # print("python3 simulate.py " + directOrGUI + " &" + str(self.myID))
        # print("python3 simulate.py " + directOrGUI + " " + str(self.myID))
        # os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID))
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1 &")
        # os.system("python3 simulate.py " + directOrGUI + " &" + str(self.myID))
        

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
            # print('ege')
        fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(fitnessFile.read())
        # print(, 'checkee')
        os.system("rm fitness" + str(self.myID) + ".txt")
        #Delete here  stpe 62
        # print(self.fitness, 'fitty')

    def Create_Ball(self):
        pyrosim.Start_URDF("ball.urdf")

        pyrosim.Send_Cube(name="Ball", pos=[2,0,2] , size=[0.5,0.5,0.5])

        pyrosim.End()
        # pass


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[10,2,0.5] , size=[1,1,1])
        pyrosim.End()
        # pass

    def Create_Body(self):
            pyrosim.Start_URDF("body.urdf")


            pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.25] , size=[2,2,0.5])

            pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")

            pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5] , size=[1,1,1])

            pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2.5,0,1], jointAxis = "0 1 0")

            pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0,-0.5] , size=[1,1,1])

            # pyrosim.Send_Joint( name = "Torso_BackFlap" , parent= "Torso" , child = "BackFlap" , type = "revolute", position = [0.5,0,1.5], jointAxis = "0 1 0")

            # pyrosim.Send_Cube(name="BackFlap", pos=[-.5,0,-.5] , size=[,1,1])



            # pyrosim.Send_Cube(name='Torso', pos=[0,0,1] , size=[2,2,.5])
            # pyrosim.Send_Joint( name = 'Torso_BackLeg' , parent= 'Torso' , child = 'BackLeg' , type = 'revolute', position = [0,-0.5,1], jointAxis = "1 0 0")
            # pyrosim.Send_Cube(name='BackLeg', pos=[-0.6,-0.5,0] , size=[0.2,1,0.2])
            # pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
            # pyrosim.Send_Cube(name="FrontLeg", pos=[0.6,0.5,0] , size=[0.2,1,0.2])

            # pyrosim.Send_Joint( name = "Torso_FrontLeg1" , parent= "Torso" , child = "FrontLeg1" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")
            # pyrosim.Send_Cube(name="FrontLeg1", pos=[-0.6,0.5,0] , size=[0.2,1,0.2])
            # pyrosim.Send_Joint( name = "FrontLeg1_LowerFrontLeg1" , parent= "FrontLeg1" , child = "LowerFrontLeg1" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
            # pyrosim.Send_Cube(name="LowerFrontLeg1", pos=[-0.6,0,-0.5] , size=[0.2,0.2,1])

            # pyrosim.Send_Joint( name = 'Torso_BackLeg1' , parent= 'Torso' , child = 'BackLeg1' , type = 'revolute', position = [0,-0.5,1], jointAxis = "1 0 0")
            # pyrosim.Send_Cube(name='BackLeg1', pos=[0.6,-0.5,0] , size=[0.2,1,0.2])
            # pyrosim.Send_Joint( name = 'BackLeg1_LowerBackLeg1' , parent= 'BackLeg1' , child = 'LowerBackLeg1' , type = 'revolute', position = [0,-1,0], jointAxis = "1 0 0")
            # pyrosim.Send_Cube(name='LowerBackLeg1', pos=[0.6,0,-0.5] , size=[0.2,0.2,1])

            # pyrosim.Send_Cube(name='LeftLeg', pos=[0.5,0,0] , size=[1,0.2,0.2])
            # pyrosim.Send_Joint( name = 'Torso_LeftLeg' , parent= 'Torso' , child = 'LeftLeg' , type = 'revolute', position = [0.5,0,1], jointAxis = "0 1 0")
            # pyrosim.Send_Cube(name='RightLeg', pos=[-0.5,0,0] , size=[1,0.2,0.2])
            # pyrosim.Send_Joint( name = 'Torso_RightLeg' , parent= 'Torso' , child = 'RightLeg' , type = 'revolute', position = [-0.5,0,1], jointAxis = "0 1 0")

            # pyrosim.Send_Joint( name = "FrontLeg_LowerFrontLeg" , parent= "FrontLeg" , child = "LowerFrontLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
            # pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0.6,0,-0.5] , size=[0.2,0.2,1])
            # pyrosim.Send_Joint( name = 'BackLeg_LowerBackLeg' , parent= 'BackLeg' , child = 'LowerBackLeg' , type = 'revolute', position = [0,-1,0], jointAxis = "1 0 0")
            # pyrosim.Send_Cube(name='LowerBackLeg', pos=[-0.6,0,-0.5] , size=[0.2,0.2,1])
            # pyrosim.Send_Joint( name = 'LeftLeg_LowerLeftLeg' , parent= 'LeftLeg' , child = 'LowerLeftLeg' , type = 'revolute', position = [1,0,0], jointAxis = "0 1 0")
            # pyrosim.Send_Cube(name='LowerLeftLeg', pos=[0,0,-0.5] , size=[0.2,0.2,1])
            # pyrosim.Send_Joint( name = 'Right_LowerRightLeg' , parent= 'RightLeg' , child = 'LowerRightLeg' , type = 'revolute', position = [-1,0,0], jointAxis = "0 1 0")
            # pyrosim.Send_Cube(name='LowerRightLeg', pos=[0,0,-0.5] , size=[0.2,0.2,1])

            pyrosim.End()

            ##################################################################

    def Create_Brain(self):
        # pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        # Send Sensor Neurons
        # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        # pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        # pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "BackLeg1")
        # pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "FrontLeg")
        # pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "LeftLeg")
        # pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "RightLeg")
        # pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "LowerFrontLeg")
        # pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LowerBackLeg")
        # pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "LowerBackLeg1")
        # pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "LowerLeftLeg")
        # pyrosim.Send_Sensor_Neuron(name = 10 , linkName = "LowerRightLeg")
        # pyrosim.Send_Sensor_Neuron(name = 11, linkName = "FrontLeg1")
        # pyrosim.Send_Sensor_Neuron(name = 12, linkName = "LowerFrontLeg1")

        # # Send Motor Neurons for joints
        # pyrosim.Send_Motor_Neuron( name = 21 , jointName = "Torso_BackLeg")
        # pyrosim.Send_Motor_Neuron( name = 22 , jointName = "Torso_BackLeg1")
        # pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Torso_FrontLeg")
        # pyrosim.Send_Motor_Neuron( name = 14 , jointName = "Torso_LeftLeg")
        # pyrosim.Send_Motor_Neuron( name = 15 , jointName = "Torso_RightLeg")
        # pyrosim.Send_Motor_Neuron( name = 16 , jointName = "BackLeg_LowerBackLeg")
        # pyrosim.Send_Motor_Neuron( name = 17 , jointName = "BackLeg1_LowerBackLeg1")
        # pyrosim.Send_Motor_Neuron( name = 18 , jointName = "FrontLeg_LowerFrontLeg")
        # pyrosim.Send_Motor_Neuron( name = 19 , jointName = "LeftLeg_LowerLeftLeg")
        # pyrosim.Send_Motor_Neuron( name = 20 , jointName = "Right_LowerRightLeg")
        # pyrosim.Send_Motor_Neuron( name = 23 , jointName = "Torso_FrontLeg1")
        # pyrosim.Send_Motor_Neuron( name = 24 , jointName = "FrontLeg1_LowerFrontLeg1")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

        # Send Synapse
        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 1.5 )
        # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -0.5 )
        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -0.5 )
        # pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = -0.5 )


        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn])
                
        pyrosim.End()

    def Mutate(self):
        # print(self.pweights, 'weights1')
        randomRow = random.randint(0,c.numSensorNeurons-1)
        randomColumn = random.randint(0,c.numMotorNeurons-1)
        # print(randomRow, randomColumn, 'row column')
        self.weights[randomRow,randomColumn] = random.random() * 2 - 1
        # self.weights[0,0] = random.random() * 2 - 1
        # self.weights[1,1] = random.random() * 2 - 1
        # self.weights[0,1] = random.random() * 2 - 1
        # return self.weights
        # print(self.weights, 'weigs2')

    def Set_ID(self, id):
        self.myID = id