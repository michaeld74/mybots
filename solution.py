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

        np.random.seed(26)
        self.roof = np.random.randint(4,9)
        # print(self.roof)

        self.links = np.random.randint(5,10)
        self.binSensor = np.random.randint(0,2,self.links*2)
        # print(self.links)
    
        

        # assign7
        self.positions = ((np.random.rand(self.links+1, 3) + 0.5)*1.5).round(1) #1.6 to 3
        # self.positions[0] = [1,1,1]
        # self.positions[1] = [1,1,1]
        # self.positions[2] = [1,1,1]
        
        # x = (np.random.randint(0,15)+15)/10 # 1.5 to 3
        # y = (np.random.randint(0,15)+15)/10
        # z = (np.random.randint(0,15)+15)/10
        # print(self.positions,self.positions[0][1])
        self.extensions = np.random.randint(6,9)
        self.epositions = ((np.random.rand(self.extensions+10, 2) + 0.5)*1.5).round(1) #1.6 to 3
        

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
        
        
    
        # os.system("python3 simulate.py GUI 2&>1 &")
        
        os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2&>1")

        # os.system("python3 simulate.py " + directOrGUI + " &" + str(self.myID))
        

    def Wait_For_Simulation_To_End(self):
        
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
            # print('cheers7')
        print(self.myID)
        fitnessFile = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(fitnessFile.read())
        # print(, 'checkee')
        os.system("rm fitness" + str(self.myID) + ".txt")
        
        # print(self.fitness, 'fitty')

    def Create_Ball(self):
        pyrosim.Start_URDF("ball.urdf")
        pyrosim.Send_Cube(name="Ball", pos=[0,0,2] , size=[1,1,1])
        pyrosim.End()
        


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

            pyrosim.Send_Cube(name='Limb0', pos=[0,0,self.positions[0][2]/2+1], size=self.positions[0],color=color)
            pyrosim.Send_Joint(name='Limb0_BotLimb0', parent='Limb0', child='BotLimb0', type='revolute', position=[0,self.positions[0][1]/2,self.positions[0][2]+1], jointAxis="1 0 0")
            
            pyrosim.Send_Cube(name='BotLimb0', pos=[0,self.positions[0][1]/2,self.positions[0][2]/2], size=self.positions[0],color=color)
            pyrosim.Send_Joint(name='BotLimb0_Limb1', parent='BotLimb0', child='Limb1', type='revolute', position=[0,self.positions[0][1],0], jointAxis="1 0 0")

            # print(self.positions)
            # pyrosim.Send_Joint(name='Limb0_Arm0', parent='Limb0', child='Arm0', type='revolute', position=[0,self.positions[0][1]/2,self.positions[0][2]], jointAxis="1 0 0")
            # pyrosim.Send_Cube(name='Arm0', pos=[self.positions[0][0]/2,0,0], size=[0.3,0.3,self.positions[0][2]*3],color=color)

            # pyrosim.Send_Joint(name='Limb0_Arm1', parent='Limb0', child='Arm1', type='revolute', position=[0,self.positions[0][1]/2,self.positions[0][2]], jointAxis="1 0 0")
            # pyrosim.Send_Cube(name='Arm1', pos=[-self.positions[0][0]/2,0,0], size=[0.3,0.3,self.positions[0][2]*3],color=color)
            
            

            for i in range(1, self.links-1):
                
                # print(i, 'cheers1')
                
                color = "blue"
                if self.binSensor[i] == 1:
                    color = "green"
                # x = (np.random.randint(0,15)+15)/10
                # y = (np.random.randint(0,15)+15)/10
                # z = (np.random.randint(0,15)+15)/10
                pyrosim.Send_Cube(name='Limb'+str(i), pos=[0,self.positions[i][1]/2,-self.positions[i][2]/2], size=self.positions[i],color=color)
                pyrosim.Send_Joint(name='Limb'+str(i)+'_BotLimb'+str(i), parent='Limb'+str(i), child='BotLimb'+str(i), type='revolute', position=[0,self.positions[i][1],0], jointAxis="1 0 0")
                
                pyrosim.Send_Cube(name='BotLimb'+str(i), pos=[0,self.positions[i][1]/2,self.positions[i][2]/2], size=self.positions[i],color=color)
                pyrosim.Send_Joint(name='BotLimb'+str(i)+'_Limb'+str(i+1), parent='BotLimb'+str(i), child='Limb'+str(i+1), type='revolute', position=[0,self.positions[i][1],0], jointAxis="1 0 0")
      
            x = (np.random.randint(0,15)+15)/10
            y = (np.random.randint(0,15)+15)/10
            z = (np.random.randint(0,15)+15)/10

            color = "blue"
            if self.binSensor[self.links-1] == 1:
                color = "green"

            # print(y, 'cheers2')

            y = (np.random.randint(0,15)+15)/10
            pyrosim.Send_Cube(name='Limb'+str(self.links-1), pos=[0,self.positions[0][1]/2,self.positions[0][2]/2], size=self.positions[0], color=color)

            # Initiatlize some variables for upcoming loop
            coinflip1=0
            linked = []
            skipper = 2

            # print('cheers4')
            #### EXSTENSIONS

            for i in range(self.extensions*2):
                # Skip iteration of loop if we have completed extra branch offs
                if skipper != 0:
                    skipper -= 1
                    continue
                coinflip = np.random.randint(0,2)
                arg = coinflip
                # Determines which existing snake link to branch off of
                linkoff = np.random.randint(2,self.links)
                # print()
                # print(linkoff)
                #Checks if there is already a branch at this "linkoff"
                test = linked.count(linkoff)
                if arg == 0: arg = -1
                if test == 1: 
                    pass
                else:
                    linked.append(linkoff*arg)
                    # print(coinflip)
                    # print(linked)
                # Build off in the positive direction
                    if coinflip == 1:
                        
                        pyrosim.Send_Joint(name='Limb'+str(linkoff)+'_Limb'+str(self.links+i), parent='Limb'+str(linkoff), child='Limb'+str(self.links+i), type='revolute', position=[self.positions[linkoff][0]/2,0, -self.positions[linkoff][1]/2], jointAxis="0 1 0")
                        pyrosim.Send_Cube(name='Limb'+str(self.links+i), pos=[self.epositions[i][0]/2,0,0], size=[self.epositions[i][0],y,z],color=color)
                        # Keep Branching?
                        # while coinflip1 != 2:
                        #     # print('gothere',i)
                        #     pyrosim.Send_Joint(name='Limb'+str(self.links+i)+'_Limb'+str(self.links+1+i), parent='Limb'+str(self.links+i), child='Limb'+str(self.links+i+1), type='revolute', position=[self.epositions[i][0],0,0], jointAxis="0 1 0")
                        #     pyrosim.Send_Cube(name='Limb'+str(self.links+i+1), pos=[self.epositions[i+1][0]/2,0,self.roof/2], size=[self.epositions[i+1][0],y,z],color=color)
                        #     skipper+=1
                        #     coinflip1 = np.random.randint(0,3)
                        #     i +=1
                    # Build off in the other direction
                    if coinflip == 0:
                        
                        pyrosim.Send_Joint(name='Limb'+str(linkoff)+'_Limb'+str(self.links+i), parent='Limb'+str(linkoff), child='Limb'+str(self.links+i), type='revolute', position=[-self.positions[linkoff][0]/2,0,-self.positions[linkoff][1]/2], jointAxis="0 1 0")
                        pyrosim.Send_Cube(name='Limb'+str(self.links+i), pos=[-self.epositions[i][0]/2,0,0], size=[self.epositions[i][0],y,z],color=color)
                        # while coinflip == 0:
                        #     coinflip = np.random.randint(0,2)
            # print('outofloop')



            pyrosim.End()

            ##################################################################

    def Create_Brain(self):
        # pyrosim.Start_NeuralNetwork("brain.nndf")
        
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        # pyrosim.Start_NeuralNetwork("brain.nndf")

        # Send Sensor Neurons
        # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")

        # pyrosim.Send_Motor_Neuron(name=1, jointName = "Limb0_Limb1")
        # pyrosim.Send_Sensor_Neuron(name=5,linkName='Limb'+str(3))
        # pyrosim.Send_Motor_Neuron(name=6, jointName = "Limb"+str(3)+"_Limb1")


        # # Send Motor Neurons for joints
        # pyrosim.Send_Motor_Neuron(name=2, jointName = "Limb0_Limb1")
        # pyrosim.Send_Motor_Neuron( name = 22 , jointName = "Torso_BackLeg1")
        count = 1
        # pyrosim.Send_Sensor_Neuron(name=0,linkName='Arm'+str(0))
        # pyrosim.Send_Sensor_Neuron(name=0,linkName='Arm'+str(1))
        pyrosim.Send_Sensor_Neuron(name=0,linkName='Limb'+str(0))
        pyrosim.Send_Sensor_Neuron(name=0,linkName='BotLimb'+str(0))
        for i in range(1,self.links):
            
            
            pyrosim.Send_Sensor_Neuron(name=count,linkName='Limb'+str(i))
            count += 1
            pyrosim.Send_Sensor_Neuron(name=count,linkName='BotLimb'+str(i))
        
        # for i in range(self.links-2):
        #     pyrosim.Send_Sensor_Neuron(name=count+self.links,linkName='BotLimb'+str(i))
        #     count += 1

        for i in range(self.extensions):
            pyrosim.Send_Sensor_Neuron(name=count,linkName='Limb'+str(i+self.links))

        # pyrosim.Send_Motor_Neuron(name=30, jointName='Limb'+str(0)+'_Arm'+str(0))
        # pyrosim.Send_Motor_Neuron(name=31, jointName='Limb'+str(0)+'_Arm'+str(1))

        for i in range(self.links-1):
            pyrosim.Send_Motor_Neuron(name=i+count, jointName='Limb'+str(i)+'_BotLimb'+str(i))
            count +=1
            pyrosim.Send_Motor_Neuron(name=i+count, jointName='BotLimb'+str(i)+'_Limb'+str(i+1))
            

        # for i in range(self.links-1):
        #     pyrosim.Send_Motor_Neuron(name=i+count, jointName='Limb'+str(i)+'_Limb'+str(i+1))

        # for i in range(self.extensions-1):
        #     pyrosim.Send_Motor_Neuron(name=i+count, jointName='Limb'+str(i+self.links-1)+'_Limb'+str(i+self.links))

        count=self.links*2-1
        for i in range(self.links*2-1):
            if self.binSensor[i] == 1:
                for j in range(self.links*2-2):
                    pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j+count, weight=np.random.rand()*4-1)


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
        self.weights[randomRow,randomColumn] = random.random() * 4 - 1


    def Set_ID(self, id):
        self.myID = id