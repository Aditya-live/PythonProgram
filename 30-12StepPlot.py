import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

year=np.array([2015,2016,2017,2018,2019])  #used np.array to convert list into floating point int

lst=[1,0,0,0,0] #for seperating a piece of pie
#the 1 in the list represent the distance from the center

bmw=[700,1500,2000,3500,6000]
mercedes=[2000,2500,2000,1800,1000]
maruti=[2000,4000,5000,6000,6500]
ford=[3000,3100,3500,2000,2300]

plt.step(year,bmw)

plt.grid()
plt.show()
