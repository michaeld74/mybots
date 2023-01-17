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

        ROBOT.Prepare_To_Sense(self)
        
        
        


        


    def Run():
        for i in range(1000):

            print(i)
            time.sleep(.000005)
            p.stepSimulation()

            # # Record back and front leg data at each step
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

            # # Motors
            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex = robotId,
            #     jointName = b"Torso_BackLeg",
            #     controlMode = p.POSITION_CONTROL,
            #     targetPosition = targetAnglesBackLeg[i],
            #     maxForce = c.maxForce)

            # pyrosim.Set_Motor_For_Joint(
            #     bodyIndex = robotId,
            #     jointName = b"Torso_FrontLeg",
            #     controlMode = p.POSITION_CONTROL,
            #     targetPosition = targetAnglesFrontLeg[i],#random.uniform(-3.1415/2.0, 3.1415/2.0),
            #     maxForce = c.maxForce)

    # def __del__(self):

    #     p.disconnect()

            