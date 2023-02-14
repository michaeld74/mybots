import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c


class SOLUTION:

    def __init__(self):
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons) #* 2 - 1
        self.weights = self.weights * 2 - 1
        # self.myID = nextAvailableID
        self.roof = np.random.randint(2,3)
        self.links = np.random.randint(5,15)
        


        
        # self.Create_Brain()
        
    
    def Evaluate(self, directOrGUI):
        pass
        
        # os.system("python3 simulate.py GUI")
        
        # os.system('python3 ../mybots/simulate.py')
        
        # python simulate.py

    def Start_Simulation(self):
        
        self.Create_Ball()
        self.Create_Brain()
        self.Create_Body()
        self.Create_World()
        
    
        os.system("python3 simulate.py GUI 2&>1 &")

        # os.system("python3 simulate.py " + directOrGUI + " &" + str(self.myID))
        

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
            # print('ege')
        fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(fitnessFile.read())
        # print(, 'checkee')
        os.system("rm fitness" + str(self.myID) + ".txt")
        
        # print(self.fitness, 'fitty')

    def Create_Ball(self):

        pass


    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[10,2,0.5] , size=[0.7,0.7,0.7])
        pyrosim.End()
        # pass

    def Create_Body(self):
            pyrosim.Start_URDF("body.urdf")



            x = (np.random.randint(0,15)+15)/10
            y = (np.random.randint(0,15)+15)/10
            z = (np.random.randint(0,15)+15)/10

            pyrosim.Send_Cube(name='Limb0', pos=[0,0,self.roof/2], size=[x,y,z])
            pyrosim.Send_Joint(name='Limb0_Limb1', parent='Limb0', child='Limb1', type='revolute', position=[0,(np.random.randint(0,15)+15)/40,0], jointAxis="1 0 0")
        

            for i in range(1, self.links-1):
                x = (np.random.randint(0,15)+15)/10
                y = (np.random.randint(0,15)+15)/10
                z = (np.random.randint(0,15)+15)/10
                pyrosim.Send_Cube(name='Limb'+str(i), pos=[0,y/2,self.roof/2], size=[x,y,z])
                pyrosim.Send_Joint(name='Limb'+str(i)+'_Limb'+str(i+1), parent='Limb'+str(i), child='Limb'+str(i+1), type='revolute', position=[0,y,0], jointAxis="1 0 0")
      
            y = (np.random.randint(0,15)+15)/10
            pyrosim.Send_Cube(name='Limb'+str(self.links-1), pos=[0,y/2,self.roof/2], size=[x,y,z])



            pyrosim.End()

            ##################################################################

    def Create_Brain(self):
        # pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Start_NeuralNetwork("brain.nndf")

        # Send Sensor Neurons
        # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")


        # # Send Motor Neurons for joints
        pyrosim.Send_Motor_Neuron( name = 2 , jointName = "Limb0_Limb1")
        # pyrosim.Send_Motor_Neuron( name = 22 , jointName = "Torso_BackLeg1")
        count = 0
        for i in range(self.links):
            pyrosim.Send_Sensor_Neuron(name = count, linkName='Limb'+str(i))
            count += 1

        for i in range(self.links-1):
            pyrosim.Send_Motor_Neuron( name = i+count , jointName = 'Limb'+str(i)+'_Limb'+str(i+1))


        for i in range(self.links):
            for j in range(self.links-1):
                pyrosim.Send_Synapse( sourceNeuronName = i , targetNeuronName = j+count , weight = np.random.rand() * 2 - 1 )


        # Send Synapse



        # for currentRow in range(c.numSensorNeurons):
        #     for currentColumn in range(c.numMotorNeurons):
        #         pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn])
                
        pyrosim.End()

    def Mutate(self):
        # print(self.pweights, 'weights1')
        randomRow = random.randint(0,c.numSensorNeurons-1)
        randomColumn = random.randint(0,c.numMotorNeurons-1)
        # print(randomRow, randomColumn, 'row column')
        self.weights[randomRow,randomColumn] = random.random() * 2 - 1


    def Set_ID(self, id):
        self.myID = id