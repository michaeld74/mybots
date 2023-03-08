import numpy 
import matplotlib.pyplot as plt
import constants as c
import numpy as np



a = numpy.load('matrix.npy')
print(a)
# print( )

x = [10,20,30,40,50]
count = np.arange(c.numberOfGenerations)
print(count)
  
# # plot lines
plt.plot(count, a[0,:], label = "Bot 1")
plt.plot(count, a[1,:], label = "Bot 2")
plt.plot(count, a[2,:], label = "Bot 3")
plt.plot(count, a[3,:], label = "Bot 4")
plt.plot(count, a[4,:], label = "Bot 5")
plt.plot(count, a[5,:], label = "Bot 6")
plt.plot(count, a[6,:], label = "Bot 7")
plt.plot(count, a[7,:], label = "Bot 8")
plt.plot(count, a[8,:], label = "Bot 9")
plt.plot(count, a[9,:], label = "Bot 10")

# matplotlib.pyplot.plot(a[0,:],a[1,:],a[2,:])
plt.title('Distance from Origin by Generation v5')
plt.xlabel('Generation')
plt.ylabel('Distance From Origin x10')
plt.legend()
plt.savefig('V5.png')
plt.show()