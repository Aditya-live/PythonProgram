import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

year=np.array([2015,2016,2017,2018,2019])  #used np.array to convert list into floating point int


bmw=[700,1500,2000,3500,6000]
mercedes=[2000,2500,2000,1800,1000]
maruti=[2000,4000,5000,6000,6500]
ford=[3000,3100,3500,2000,2300]

data=[1,5,4,3,8,6,9,4,3,2,0,1,2,6,5,3]
plt.hist(data)

plt.grid()
plt.show()



