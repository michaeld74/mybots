import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.loop)

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        # return self.values[t]
        # print(self.values[t])
        # print(t)