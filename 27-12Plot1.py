import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

year=[2015,2016,2017,2018,2019]
bmw=[700,1500,2000,3500,6000]
mercedes=[2000,2500,2000,1800,1000]
maruti=[2000,4000,5000,6000,6500]
ford=[3000,3100,3500,2000,2300]

#subplot is passed above the plot

#plt.subplot(141)
plt.subplot(221)
l1,=plt.plot(year,bmw,label="BMW",color='red',linestyle=":",linewidth="3",marker="*",markerfacecolor="yellow",markersize="10")
#other options for line style "-.", "-",":"
#line width for increasing or decreasing line width
#marker used for marking the intersection points
#markerfacecolor
plt.legend([l1],loc="upper left") #For postioning label
plt.grid()

#plt.subplot(142)
plt.subplot(222)
l2,=plt.plot(year,mercedes,label="Mercedes")
plt.legend([l2],loc='upper left')
plt.grid()

#plt.subplot(143)
plt.subplot(223)
l3,=plt.plot(year,maruti,label="Maruti",color='orange',linestyle="--",linewidth="3",marker="*",markerfacecolor="yellow",markersize="10")
plt.legend()
plt.grid()

#plt.subplot(144)
plt.subplot(224)
plt.plot(year,ford,label="Ford",color='green',linestyle="-.",linewidth="2",marker="o",markerfacecolor="purple",markersize="5")
plt.legend() #To display the labels
plt.grid()

#For labelling x and y axis
plt.xlabel("Years")
plt.ylabel("Units sold")

plt.show()
