import time
import numpy as np
import pyrosim.pyrosim as pyrosim
import platform
import os
import constants as c


class Solution():
    def __init__(self, id):
        self.weights = np.random.rand(c.num_sensor_neurons, c.num_motor_neurons)
        self.weights = self.weights * 2. - 1.
        self.set_id(id)

    def start_simulation(self, headless):
        self.generate_body()
        self.generate_brain()
        if platform.system() == "Windows":
            # os.system(f"conda activate evo-robots & start /B python simulate.py {'DIRECT' if headless else 'GUI'}")
            os.system(f"start /B python simulate.py {'DIRECT' if headless else 'GUI'} --id {self.id} > nul 2> nul")
        else:
            os.system(f"python simulate.py {'DIRECT' if headless else 'GUI'} --id {self.id} 2&>1" + " &")

    def wait_for_simulation(self):
        fit_file = f"fitness{self.id}.txt"

        while not os.path.exists(fit_file):
            time.sleep(0.01)

        with open(fit_file) as f:
            self.fitness = float(f.read())

        if platform.system() == "Windows":
            os.system(f"del fitness{self.id}.txt")
        else:
            os.system(f"rm fitness{self.id}.txt")

        f.close()

    def set_id(self, id):
        self.id = id

    def mutate(self):
        mutate_row = np.random.randint(0, 3)
        mutate_col = np.random.randint(0, 2)
        self.weights[mutate_row, mutate_col] = np.random.rand() * 2. - 1.

    def generate_body(self):
        pyrosim.Start_URDF(f"body{self.id}.urdf")
        # pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])
        # pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
        #                    position=[0, -0.5, 1.0], jointAxis="1 0 0")
        # pyrosim.Send_Cube(name="BackLeg", pos=[0.0, -0.5, 0.0], size=[.2, 1., .2])
        # pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
        #                    position=[0.0, 0.5, 1.0], jointAxis="1 0 0")
        # pyrosim.Send_Cube(name="FrontLeg", pos=[0.0, 0.5, 0], size=[.2, 1., .2])
        # pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0.0, 0.0], size=[1.0, 0.2, 0.2])
        # pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
        #                    position=[-0.5, 0, 1.], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0.0, 0.0], size=[1.0, 0.2, 0.2])
        # pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
        #                    position=[0.5, 0, 1.], jointAxis="0 1 0")
        # Torso link - root --> absolute position
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])

        # FrontLeg link -- > the joint connected to the root is absolute
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

        # FrontFeet link --> both link and joint are relative to the last joint
        pyrosim.Send_Joint(name="FrontLeg_FrontFeet", parent="FrontLeg", child="FrontFeet", type="revolute",
                           position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontFeet", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # BackLeg link --> the joint connected to the root is absolute
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[0, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

        # BackFeet link --> both joint and link are relative to upstream joint
        pyrosim.Send_Joint(name="BackLeg_BackFeet", parent="BackLeg", child="BackFeet", type="revolute",
                           position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackFeet", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # LeftLeg link --> the joint connected to the root is absolute
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position=[-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])

        # LeftFeet link --> both joint and link are relative to upstream joint
        pyrosim.Send_Joint(name="LeftLeg_LeftFeet", parent="LeftLeg", child="LeftFeet", type="revolute",
                           position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftFeet", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        # RightLeg link --> the joint connected to the root is absolute
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position=[0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])

        # RightFeet link --> both joint and link are relative to upstream joint
        pyrosim.Send_Joint(name="RightLeg_RightFeet", parent="RightLeg", child="RightFeet", type="revolute",
                           position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightFeet", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.End()

    def generate_brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.id}.nndf")

        # Neurons:
        # -Input
        pyrosim.Send_Sensor_Neuron(name=0, linkName="BackFeet")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontFeet")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="LeftFeet")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="RightFeet")

        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=5, jointName="FrontLeg_FrontFeet")
        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=7, jointName="BackLeg_BackFeet")
        pyrosim.Send_Motor_Neuron(name=8, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=9, jointName="LeftLeg_LeftFeet")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="RightLeg_RightFeet")

        # Synapses:
        # fully connected:
        for row in range(c.num_sensor_neurons):
            for col in range(c.num_motor_neurons):
                pyrosim.Send_Synapse(sourceNeuronName=row, targetNeuronName=col + 3, weight=self.weights[row][col])

        pyrosim.End()

        while not os.path.exists(f"brain{self.id}.nndf"):
            time.sleep(0.01)
