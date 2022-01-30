import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

pyrosim.Start_SDF("boxes.sdf")
for i in range(0, 5):
    x = 0
    for i_1 in range(0, 5):
        z = 0.5
        length = 1
        width = 1
        height = 1
        for i_2 in range(0, 10):
            pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
            length = length * 0.9
            width = width * 0.9
            height = height * 0.9
            z = z + 1
        x = x + 1
    y = y + 1
pyrosim.End()
