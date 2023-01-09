import pybullet as p
import time

physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")

for i in range(1000):
    time.sleep(.005)
    p.stepSimulation()
    print(i)

p.disconnect()
