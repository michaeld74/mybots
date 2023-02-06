import pybullet as p
import pybullet_data



class BALL:

    def __init__(self):

        p.loadURDF("ball.urdf")
        # planeId = p.loadURDF("plane.urdf")
        
        