import pandas as pd
import numpy as np

print("\tEVOLUTION OF CRYPTOCURRENCY PRICE: USDC\n")

#Read the csv document that contains the dataset
df = pd.read_csv("coin_USDCoin.csv")

#Obtain a detailed info
print(df.info(),'\n')

#Get the name of the columns
print(df.columns,'\n')

#Show if there are missing values in the dataset
missing = df.isnull().sum()
print('Missing Values ->\n')
print(missing[:],'\n')

#Get the percentage representing the missing values
cells = np.product(df.shape)
missing = missing.sum()
percent = (missing/cells) * 100
print("The percentage of missing values is",percent,"%.\n")

#Show the first and last rows to make sure you got the right data
print('This dataset contains (rows, colums) before cleaning:',df.shape,'\n')
print(df.head(25),'\n')
print(df.tail(25),'\n')
print(df.describe(),'\n')

#Press 1 to continue and fill empty spaces with a 0
dfcontinue1=int(input("Press 1 -> "))
df = df.fillna(0)

#Show the first and last rows after cleaning and apply a basic data analysis
print('\nThis dataset contains (rows, colums) after cleaning:',df.shape,'\n')
print(df.head(25),'\n')
print(df.tail(25),'\n')
print(df.describe(),'\n')
