import numpy as numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('./data/backLegSensorValues.py.npy', mmap_mode=None, allow_pickle=False,
                                 fix_imports=True, encoding='ASCII')

frontLegSensorValues = numpy.load('./data/frontLegSensorValues.py.npy', mmap_mode=None, allow_pickle=False,
                                  fix_imports=True, encoding='ASCII')
print(backLegSensorValues)
print(frontLegSensorValues)

matplotlib.pyplot.plot(frontLegSensorValues, label='FrontLeg sensor', linewidth=3, markersize=12)
matplotlib.pyplot.plot(backLegSensorValues, label='BackLeg sensor')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
