import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return pow(x,2)
fx_name = r'$f(x)= pow(x,2)$'

x=np.setdiff1d(np.linspace(-10,10,100),[0])
y=f(x)
plt.plot(x, y, label=fx_name)
plt.legend(loc='upper left')
plt.show()

