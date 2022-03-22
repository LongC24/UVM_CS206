import pyrosim.pyrosim as pyrosim


def main():
    Create_world()
    Generate_Body()
    Generate_Brain()


def Create_world():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[2, 2, 0.5], size=[1, 1, 1])
    pyrosim.End()


def Generate_Body():
    pyrosim.Start_URDF("body.urdf")

    # Torso link - root --> absolute position
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[1, 1, 1])

    # BackLeg link --> the joint connected to the root is absolute
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[-0.5, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

    # FrontLeg link -- > the joint connected to the root is absolute
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0.5, 0, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

    pyrosim.End()


def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")

    # This particular neuron receives value from sensor stored in Torso.
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

    pyrosim.End()


main()
