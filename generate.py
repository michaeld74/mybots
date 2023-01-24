import pyrosim.pyrosim as pyrosim
import random

def Create_World():
    pyrosim.Start_SDF("world.sdf")

    

    length = 1
    width = 1
    height = 1

    x = 2
    y = 2
    z = 0.5  

    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])



    pyrosim.End()



def Generate_Body():
    pyrosim.Start_URDF("body.urdf")

    length = 1
    width = 1
    height = 1

    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length,width,height])

    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])


    pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5] , size=[length,width,height])

    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])

    pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0,-.5] , size=[length,width,height])

    pyrosim.End()

def Generate_Brain():

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
    pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 0.5 )
    pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = 0.5 )
    pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 0.5 )

    for i in range(3):
        for j in range(3,5):
            pyrosim.Send_Synapse( sourceNeuronName = i , targetNeuronName = j , weight = random.uniform(-1,1))

    pyrosim.End()




# def Create_Robot():
    

    # pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [0,0,1])

    # pyrosim.Send_Cube(name="Link2", pos=[0,0,.5] , size=[length,width,height])

    # pyrosim.Send_Joint( name = "Link2_Link3" , parent= "Link2" , child = "Link3" , type = "revolute", position = [0,.5,.5])

    # pyrosim.Send_Cube(name="Link3", pos=[0,.5,0] , size=[length,width,height])


    

Create_World()

Generate_Body()

Generate_Brain()
# Create_Robot()