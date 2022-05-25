import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table = pd.DataFrame(
    {'Avena':[3.0,3.9,4.3,4.3,5.0,8.1,6.2,6.5,6.5,7.0,6.8,7.0],
     'Trigo':[1.8,3.1,3.3,4.2,3.0,5.5,6.2,6.4,6.5,6.9,5.5,5.0],
     'Arroz':[2.9,3.9,4.5,4.4,6.0,6.8,6.2,7.5,6.5,6.8,7.3,7.8],
     'Maíz':[2.7,3.5,4.3,4.4,5.9,6.1,6.2,5.9,6.5,7.1,6.9,6.1],
     'Cebada':[2.3,3.3,4.3,3.4,2.9,5.9,6.9,6.5,6.5,7.0,6.2,5.0]},
    index = ['Enero','Febrero','Marzo','Abril','Mayo','Junio',
             'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'])

print(table,'\n')
print(table.describe())


#table.plot(title='Producción Anual de Cereales')
#table.plot.bar(title='Producción Anual de Cereales',subplots=True)
#table.plot.scatter(x=2,y=3,title='Producción Anual de Cereales',subplots=True)
plt.xlabel('I TRIMETRE - II TRIMESTRE - II TRIMESTRE - IV TRIMESTRE')
plt.ylabel('Toneladas Producidas')
plt.show()


