
import matplotlib.pyplot as plt
import numpy as np

x = np.array([-3, -2,-1, 0, 1, 2,3])
y = np.array(x**2)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^2')

plt.show()



