import time
import pybullet as p
# for i in range(1000):
physicsClient = p.connect(p.GUI)
for i in range(10000):

    p.stepSimulation()
    time.sleep(1/60)
    #print(i)

p.disconnect()

#
