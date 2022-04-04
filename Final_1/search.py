import os
import platform
from time import sleep

from parallel_hillclimber import ParallelHillClimber
import constants as c

phc = ParallelHillClimber(c.num_gens, c.pop_size)
phc.evolve()
phc.show_best()

sleep(10)
# remove temp files:
if platform.system() == "Windows":
    os.system("del brain*.nndf")
    os.system("del body*.urdf")
    os.system("del fitness*.txt")
else:
    os.system("rm brain*.nndf")
    os.system("rm body*.urdf")
    os.system("rm fitness*.txt")