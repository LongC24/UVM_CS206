import time
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(300)
frontLegSensorValues = numpy.zeros(300)

for i in range(300):
    p.setGravity(0, 0, -9.8)
    p.stepSimulation()
    time.sleep(1 / 60)

    # frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    # backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

# print(i)

print(backLegSensorValues)
numpy.save('./data/backLegSensorValues.py', frontLegSensorValues, allow_pickle=True, fix_imports=True)
numpy.save('./data/frontLegSensorValues.py', backLegSensorValues, allow_pickle=True, fix_imports=True)

p.disconnect()
