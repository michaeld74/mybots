import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random


class SOLUTION:

    def __init__(self):
        self.weights = np.random.rand(3,2)
        self.weights = self.weights * 2 - 1
        # self.Create_Brain()
        
    
    def Evaluate(self):
        self.Create_Brain()
        self.Create_Body()
        self.Create_World()
        os.system("python3 simulate.py DIRECT")
        # os.system('python3 ../mybots/simulate.py')
        fitnessFile = open("fitness.txt", "r")
        self.fitness = fitnessFile.read()
        # python simulate.py

    def Create_World(self):
        pass

    def Create_Body(self):
        pass

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")

        # Send Sensor Neurons
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

        # Send Motor Neurons for joints
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = 'Torso_BackLeg')
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = 'Torso_FrontLeg')

        # Send Synapse
        pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 1.5 )
        pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = -0.5 )
        pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -0.5 )
        pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = -0.5 )


        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn])
                
        pyrosim.End()

    def Mutate(self):
        # print(self.pweights, 'weights1')
        randomRow = random.randint(0,2)
        randomColumn = random.randint(0,1)
        # print(randomRow, randomColumn, 'row column')
        self.weights[randomRow,randomColumn] = random.random() * 2 - 1
        # self.weights[0,0] = random.random() * 2 - 1
        # self.weights[1,1] = random.random() * 2 - 1
        # self.weights[0,1] = random.random() * 2 - 1
        # return self.weights
        # print(self.weights, 'weigs2')

