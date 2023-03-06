import numpy as np
import matplotlib.pyplot as plt

x = np.array([-3,-2,-1,0,1,2,3])
y = np.array(x**2)

plt.plot(x,y)
plt.xlabel('X values')
plt.ylabel('Y values (x^2)')
plt.title('Quadractic value')
plt.show()
