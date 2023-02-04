import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c


class SOLUTION:

    def __init__(self, nextAvailableID):
        self.weights = np.random.rand(3,2)
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID
        # self.Create_Brain()
        
    
    def Evaluate(self, directOrGUI):
        pass
        
        # os.system("python3 simulate.py GUI")
        
        # os.system('python3 ../mybots/simulate.py')
        
        # python simulate.py

    def Start_Simulation(self, directOrGUI):
        
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
        fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(fitnessFile.read())
        
        os.system("rm fitness" + str(self.myID) + ".txt")
        #Delete here  stpe 62
        # print(self.fitness, 'fitty')

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-2,2,0.5] , size=[1,1,1])
        pyrosim.End()

    def Create_Body(self):
            pyrosim.Start_URDF("body.urdf")

            length = 1
            width = 1
            height = 1

            pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[length,width,height])

            pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")

            pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])

            pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,0.5,1], jointAxis = "1 0 0")

            pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])

            pyrosim.End()

            ##################################################################

    def Create_Brain(self):
        # pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        # Send Sensor Neurons
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

        # Send Motor Neurons for joints
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = 'Torso_BackLeg')
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = 'Torso_FrontLeg')

        # Send Synapse
        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 1.5 )
        # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -0.5 )
        # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -0.5 )
        # pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = -0.5 )


        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn])
                
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