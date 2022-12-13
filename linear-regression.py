# CODE A LINEAR REGRESSION USING NUMPY & MATPLOTLIB

import matplotlib.pyplot as plt
import numpy as np

#FIRST STEP: Generate the data with numpy
np.random.seed(0)
x=np.random.rand(100,1)
y=2+3*x+np.random.rand(100,1)

#SECOND STEP: Calculate the coeficient (cf) of the linear regression
cf=np.polyfit(x.flatten(),y.flatten(),deg=1)

#THIRD STEP: Create a function to represent the linear regression
reg_line=np.poly1d(cf)

#FOURTH STEP: Plot the linear regression in a graph
plot=np.linspace(0,1,100)
plt.plot(x,y,'o',plot,reg_line(plot),'-')
plt.show()
