from robot import ROBOT
from world import WORLD
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(*c.gravity)
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(0, c.maxTimeStep):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()
            # print(t)
            time.sleep(1 / c.fps)
        # for s in self.robot.sensors:
        #     s.Save_Values()
        # for m in self.robot.motors:
        #     m.Save_Values()

    def __del__(self):
        p.disconnect()
