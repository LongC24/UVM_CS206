import constants as c

import time
from cmath import pi
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

# set up variables


ampBack = pi / 4
freqBack = 20
phaseOffsetBack = 0

ampFront = pi / 4
freqFront = 20
phaseOffsetFront = pi / 4 + 3

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(4000)
frontLegSensorValues = np.zeros(4000)

print(robotId)

# create motor values vector
targetAnglesFront = ampFront * np.sin(freqFront * (np.linspace(0, 2 * pi, 4000)) + phaseOffsetFront)
print(targetAnglesFront)
targetAnglesBack = ampBack * np.sin(freqBack * (np.linspace(0, 2 * pi, 4000)) + phaseOffsetBack)

np.save("data/targetAnglesBack", targetAnglesFront)
np.save("data/targetAnglesFront", targetAnglesBack)
# exit()

for i in range(4000):
    p.setGravity(0, 0, -9.8)
    p.stepSimulation()
    time.sleep(1 / 240)

    # frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    # backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="Torso_FrontLeg", controlMode=p.POSITION_CONTROL,
                                targetPosition=targetAnglesFront[i], maxForce=40)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="Torso_BackLeg", controlMode=p.POSITION_CONTROL,
                                targetPosition=targetAnglesBack[i], maxForce=40)

# print(i)

np.save('./data/backLegSensorValues', frontLegSensorValues, allow_pickle=True, fix_imports=True)
np.save('./data/frontLegSensorValues', backLegSensorValues, allow_pickle=True, fix_imports=True)

p.disconnect()
