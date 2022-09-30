import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, Normalizer, Binarizer
from sklearn.metrics import mean_absolute_error, adjusted_rand_score, homogeneity_score, v_measure_score
from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn import neighbors
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

print("\t[TITLE]\n")

#DATA ANALYSIS#
 ###
#Read the csv document that contains the dataset
df = pd.read_csv(".csv")

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
print(f"The percentage of missing values is {percent}%.\n")

#Show the first and last rows to make sure you got the right data
print(f'This dataset contains (rows, colums) before cleaning: {df.shape}.\n')
print(df.head(25),'\n')
print(df.tail(25),'\n')
print(df.describe(),'\n')

#Press 1 to continue and fill empty spaces with a 0
dfcontinue1=int(input("Press 1 -> "))
df = df.fillna(0)

#Show the first and last rows after cleaning and apply a basic data analysis
print(f'\nThis dataset contains (rows, colums) after cleaning: {df.shape}.\n')
print(df.head(25),'\n')
print(df.tail(25),'\n')
print(df.describe(),'\n')

#Locate specific rows/columns to a new dataframe
#df_new = df.iloc['']
#df_new = df.loc['']



#DATA VISUALIZATION#
 ###
#Make graphs from the previous dataframe
#df_new.plot(title='')
#df_new.plot.bar(title='',subplots=True)
#df_new.plot.scatter(x=2,y=3,title='',subplots=True)
plt.xlabel('')
plt.ylabel('')
plt.show()



#MACHINE LEARNING#
 ###
#Training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

#Create your model
###Supervised Learning Estimators###

#Linear Regression
lr = LinearRegression(normalize=True)

#Support Vector Machines (SVM)
svc = SVC(kernel='Linear')

#Naive Bayes
gnb = GaussianNB

#KNN
knn = neigbors.KNeighborsClassifier(n_neighbors=5)

###Unsupervised Learning Estimators####
#Principal Component Analysis (PCA)
pca = PCA(n_components=0.95)

#K Means
k_means = KMeans(n_clusters=3,random_state=0)

#Fit the model to the data
###Supervised Learning###
lr.fit(X, y)
knn.fit(X_train, y_train)
svc.fit(X_train, y_train)

###Unsupervised Learning####
k_means.fit(X_train)
pca_model = pca.fit_transform(X_train)

#Make predictions with the data
###Supervised Estimators###
y_prediction = svc.predict(np.random.random((2,5)))
y_prediction = lr.predict(X_test)
y_prediction = knn.predict_proba(X_test)

###Unsupervised Estimators####
y_prediction = k_means.predict(X_test)

#Doing standarization to data
scaler = StandardScaler().fit(X_train)
standardized_X = scaler.transform(X_train)
standardized_X_test = scaler.transform(X_test)

#Doing normalization to data
scaler = Normalizer().fit(X_train)
normalized_X = scaler.transform(X_train)
normalized_X_test = scaler.transform(X_test)

#Doing binarization to data
binarizer = Binarizer(threshold = 0.0).fit(X)
binary_X = binarizer.transform(X)

#Calculating the mean absolute error (mae)
y_true = []
mean_absolute_error(y_true, y_prediction)

#Calculating the adjusted rand index
adjusted_rand_score(y_true, y_prediction)

#Calculating the homogeneity
homogeneity_score(y_true, y_prediction)

#Calculating the V-measure
metric.v_measure_score(y_true, y_prediction)

#Do the cross-validation of your model
print(cross_val_score(knn, X_train, y_train, cv=4),'\n')
print(cross_val_score(lr, X, y, cv=2))
