import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR


# physicsClient = p.connect(p.GUI)

class ROBOT:

    def __init__(self):

        self.robotId = p.loadURDF("body.urdf")
        self.motors = {}

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

 
