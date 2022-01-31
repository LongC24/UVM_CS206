import time
import pybullet as p
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = p.loadURDF("plane.urdf")
robotId= p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

for i in range(10000000):
    p.setGravity(0, 0, -9.8)
    p.stepSimulation()
    time.sleep(1 / 60)
    print(i)

p.disconnect()


