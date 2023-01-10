import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = 0
y = 0
z= 0.5

x1 = 1
y1 = 0
z1 = 1.5
temp = 1

for j in range(10):
    for k in range(10):
        for i in range (10):
            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
            temp = temp*0.9
            z += temp
            length = length * 0.9
            width = width * 0.9
            height = height * 0.9
        z = 0.5
        temp = 1
        length = 1
        width = 1
        height = 1
        y+=1
    x +=1
    y = 0

    


# pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

# pyrosim.Send_Cube(name="Box2", pos=[x1,y1,z1] , size=[length,width,height])

pyrosim.End()

