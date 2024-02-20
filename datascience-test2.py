# import pandas, numpy and matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# create a dataframe from scratch

df = pd.DataFrame(
    {'Age':[24,33,44,12,32,25,23,18],
     'Height':[1.61,1.78,1.63,1.56,1.45,1.61,1.69,1.43],
     'Weight':[40,62,79,43,84,66,65,58]},
    index = ['Allie','Paul',
             'Larry','Jane',
             'Steve','Wendy',
             'Henry','Diane'])


# check what the dataframe that you just created looks like

print(df,'\n')
print(df.describe())



# make plots off the dataframe

#df.plot(title='Demographics')
#df.plot.bar(title='Demographics',subplots=True)
#df.plot.scatter(x=1,y=2,title='Demographics',subplots=True)
plt.xlabel('Allie   -   Paul   -   Larry   -   Jane   -   Steve   -   Wendy   -   Henry   -   Diane')
plt.show()
