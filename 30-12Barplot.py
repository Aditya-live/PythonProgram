"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

year=np.array([2015,2016,2017,2018,2019])  #used np.array to convert list into floating point int
bmw=[700,1500,2000,3500,6000]
mercedes=[2000,2500,2000,1800,1000]
maruti=[2000,4000,5000,6000,6500]
ford=[3000,3100,3500,2000,2300]

plt.bar(year+.2,bmw,label="BMW",width=.2,color='pink',edgecolor='black')
plt.bar(year,maruti,label="Maruti",width=.2,color='violet',edgecolor='black')
plt.bar(year-.2,mercedes,label="Mercedes",width=.2,color='black',edgecolor='green')
plt.bar(year-.40,ford,label="Ford",width=.2,color='green',edgecolor='pink')


plt.legend()

plt.grid()
plt.show()
"""

##For comparison============================================================
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

year=np.array([2015,2016,2017,2018,2019])  #used np.array to convert list into floating point int
bmw=[700,1500,2000,3500,6000]
mercedes=[2000,2500,2000,1800,1000]
maruti=[2000,4000,5000,6000,6500]
ford=[3000,3100,3500,2000,2300]

plt.bar(year,maruti,label="Maruti",width=.2,color='violet',edgecolor='black')

plt.bar(year,ford,bottom=maruti,label="Ford",width=.2,color='green',edgecolor='pink')


plt.legend()

plt.grid()
plt.show()
'''
##For comparison of multiple=================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

year=np.array([2015,2016,2017,2018,2019])  #used np.array to convert list into floating point int
bmw=np.array([700,1500,2000,3500,6000])
mercedes=np.array([2000,2500,2000,1800,1000])
maruti=np.array([2000,4000,5000,6000,6500])
ford=np.array([3000,3100,3500,2000,2300])

plt.bar(year,maruti,label="Maruti",width=.2,color='violet',edgecolor='black')

plt.bar(year,ford,bottom=maruti,label="Ford",width=.2,color='green',edgecolor='red')

plt.bar(year,bmw,bottom=maruti+ford,label="BMW",width=.2,color='yellow',edgecolor='violet')

plt.bar(year,mercedes,bottom=maruti+ford+bmw,label="Mercedes",width=.2,color='blue',edgecolor='black')

plt.legend()

plt.grid()
plt.show()


