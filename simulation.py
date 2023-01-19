from world import WORLD
from robot import ROBOT
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import time




class SIMULATION:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # Initialize self.world and self.robot
        
        self.world = WORLD()
        self.robot = ROBOT()
        
    
        # Set gravity and set addionatl search path
        # self.physicsClient = p.connect(p.GUI)
        
        p.setGravity(0,0,-9.8)
        
        # Insert plane, body and world
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act(self.robot.robotId)

        
        
        


        


    def Run(self):
        for i in range(1000):

            print(i)
            time.sleep(.0005)
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)
            

            # self.robot.Sense(i)

            # print(self.robot.Sense.sensor.Get_Value())

            # # Record back and front leg data at each step
            # 



    # def __del__(self):

    #     p.disconnect()

            