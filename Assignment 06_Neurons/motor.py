import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

    # save the motor values
    def Set_Value(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=c.maxForce)

    # should be Prepare_To_Act in MOTOR class according to instructions
    # def Prepare_To_Act(self):
    #     self.amplitude = c.amp
    #     if self.jointName == "Torso_FrontLeg":
    #         self.frequency = c.freqFront
    #     else:
    #         self.frequency = c.freqBack
    #     self.offset = c.phaseOffset
    #     self.motorValues = self.amplitude * np.sin(
    #         self.frequency * (np.linspace(0, 2 * np.pi, c.maxTimeStep)) + self.offset)
    #
    # def Set_Value(self, robotId, t):
    #     pyrosim.Set_Motor_For_Joint(
    #         bodyIndex=robotId,
    #         jointName=self.jointName,
    #         controlMode=p.POSITION_CONTROL,
    #         targetPosition=self.motorValues[t],
    #         maxForce=c.maxForce)
