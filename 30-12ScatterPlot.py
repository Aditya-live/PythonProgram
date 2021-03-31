import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

t=arange(50)*2*pi/50
y=sin(t)
x=cos(t)

plt.scatter(t,y)
plt.scatter(t,x)
plot(t,y)
plot(t,x)

plt.grid()
plt.show()
