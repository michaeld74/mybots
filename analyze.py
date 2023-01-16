import numpy
import matplotlib.pyplot



backLegSensorValues = numpy.load('data/backLegVals.npy')

frontLegSensorValues = numpy.load('data/frontLegVals.npy')

print(backLegSensorValues)

matplotlib.pyplot.axis([0, 1000, -1.5, 1.5])

matplotlib.pyplot.plot(backLegSensorValues)

matplotlib.pyplot.plot(frontLegSensorValues)

matplotlib.pyplot.legend(['Back Leg','Front Leg'])

matplotlib.pyplot.show()

sinValues = numpy.load('data/sinVals.npy')

matplotlib.pyplot.plot(sinValues)

matplotlib.pyplot.show()
