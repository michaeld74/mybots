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
        self.links = np.random.randint(3,9)
        self.binSensor = np.random.randint(0,2,self.links)
        

        # assign7
        self.positions = ((np.random.rand(self.links+1, 2) + 0.5) * 2).round(1) #1.6 to 3
        # x = (np.random.randint(0,15)+15)/10 # 1.5 to 3
        # y = (np.random.randint(0,15)+15)/10
        # z = (np.random.randint(0,15)+15)/10
        print(self.positions,self.positions[0][1])
        self.extensions = np.random.randint(3,10)
        self.epositions = ((np.random.rand(self.extensions+5, 2) + 0.5) * 2).round(1) #1.6 to 3
        

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
            color = "blue"
            if self.binSensor[0] == 1:
                color = "green"



            x = (np.random.randint(0,15)+15)/10
            y = (np.random.randint(0,15)+15)/10
            z = (np.random.randint(0,15)+15)/10

            pyrosim.Send_Cube(name='Limb0', pos=[0,0,self.roof/2], size=[self.positions[0][0],self.positions[0][1],z],color=color)
            pyrosim.Send_Joint(name='Limb0_Limb1', parent='Limb0', child='Limb1', type='revolute', position=[0,self.positions[0][1]/2,0], jointAxis="1 0 0")
        

            for i in range(1, self.links-1):
                color = "blue"
                if self.binSensor[i] == 1:
                    color = "green"
                # x = (np.random.randint(0,15)+15)/10
                # y = (np.random.randint(0,15)+15)/10
                # z = (np.random.randint(0,15)+15)/10
                pyrosim.Send_Cube(name='Limb'+str(i), pos=[0,self.positions[i][1]/2,self.roof/2], size=[self.positions[i][0],self.positions[i][1],z],color=color)
                pyrosim.Send_Joint(name='Limb'+str(i)+'_Limb'+str(i+1), parent='Limb'+str(i), child='Limb'+str(i+1), type='revolute', position=[0,self.positions[i][1],0], jointAxis="1 0 0")
      
            x = (np.random.randint(0,15)+15)/10
            y = (np.random.randint(0,15)+15)/10
            z = (np.random.randint(0,15)+15)/10

            color = "blue"
            if self.binSensor[self.links-1] == 1:
                color = "green"

            y = (np.random.randint(0,15)+15)/10
            pyrosim.Send_Cube(name='Limb'+str(self.links-1), pos=[0,self.positions[self.links-1][1]/2,self.roof/2], size=[self.positions[self.links-1][0],self.positions[self.links-1][1],z], color=color)

            # Initiatlize some variables for upcoming loop
            coinflip1=0
            linked = []
            skipper = 2

            for i in range(self.extensions):
                # Skip iteration of loop if we have completed extra branch offs
                if skipper != 0:
                    skipper -= 1
                    continue
                coinflip = np.random.randint(0,2)
                # Determines which existing snake link to branch off of
                linkoff = np.random.randint(2,self.links)
                #Checks if there is already a branch at this "linkoff"
                if linkoff in linked: pass
                else:
                    linked.append(linkoff)
                # Build off in the positive direction
                if coinflip == 1:
                    pyrosim.Send_Joint(name='Limb'+str(linkoff)+'_Limb'+str(self.links+i), parent='Limb'+str(linkoff), child='Limb'+str(self.links+i), type='revolute', position=[self.positions[linkoff][0]/2,0,0], jointAxis="0 1 0")
                    pyrosim.Send_Cube(name='Limb'+str(self.links+i), pos=[self.epositions[i][0]/2,0,self.roof/2], size=[self.epositions[i][0],y,z],color=color)
                    # Keep Branching?
                    while coinflip1 != 2:
                        # print('gothere',i)
                        pyrosim.Send_Joint(name='Limb'+str(self.links+i)+'_Limb'+str(self.links+1+i), parent='Limb'+str(self.links+i), child='Limb'+str(self.links+i+1), type='revolute', position=[self.epositions[i][0],0,0], jointAxis="0 1 0")
                        pyrosim.Send_Cube(name='Limb'+str(self.links+i+1), pos=[self.epositions[i+1][0]/2,0,self.roof/2], size=[self.epositions[i+1][0],y,z],color=color)
                        skipper+=1
                        coinflip1 = np.random.randint(0,3)
                        i +=1
                # Build off in the other direction
                if coinflip == 0:
                    pyrosim.Send_Joint(name='Limb'+str(linkoff)+'_Limb'+str(self.links+i), parent='Limb'+str(linkoff), child='Limb'+str(self.links+i), type='revolute', position=[-self.positions[linkoff][0]/2,0,0], jointAxis="0 1 0")
                    pyrosim.Send_Cube(name='Limb'+str(self.links+i), pos=[-self.epositions[i][0]/2,0,self.roof/2], size=[self.epositions[i][0],y,z],color=color)
                    while coinflip == 0:
                        coinflip = np.random.randint(0,2)



            pyrosim.End()

            ##################################################################

    def Create_Brain(self):
        # pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Start_NeuralNetwork("brain.nndf")

        # Send Sensor Neurons
        # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")

        # pyrosim.Send_Motor_Neuron(name=1, jointName = "Limb0_Limb1")
        # pyrosim.Send_Sensor_Neuron(name=5,linkName='Limb'+str(3))
        # pyrosim.Send_Motor_Neuron(name=6, jointName = "Limb"+str(3)+"_Limb1")


        # # Send Motor Neurons for joints
        # pyrosim.Send_Motor_Neuron(name=2, jointName = "Limb0_Limb1")
        # pyrosim.Send_Motor_Neuron( name = 22 , jointName = "Torso_BackLeg1")
        count = 0
        for i in range(self.links):
            pyrosim.Send_Sensor_Neuron(name=count,linkName='Limb'+str(i))
            count += 1

        for i in range(self.links-1):
            pyrosim.Send_Motor_Neuron(name=i+count, jointName='Limb'+str(i)+'_Limb'+str(i+1))


        for i in range(self.links):
            if self.binSensor[i] == 1:
                for j in range(self.links-1):
                    pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j+count, weight=np.random.rand()*2-1)


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