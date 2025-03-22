import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def logistic_map(x):
    """Define the logistic map function."""
    return 4.0 / (1 + 3 * x)

t = np.linspace(0, 15, 1000)
x = odeint(logistic_map, 0.25, t)

plt.plot(t, x)
plt.xlabel('t')
plt.ylabel('f(x)')
plt.title('Logistic Map Function')
plt.show()
