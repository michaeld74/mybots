import numpy 
import matplotlib.pyplot



a = numpy.load('matrix.npy')
print(a)
# print( )

matplotlib.pyplot.plot(a[2,:])
matplotlib.pyplot.show()