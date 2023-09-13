# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:43:41 2020

@author: KIRAN
"""

#Importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#Dataset
dataset = pd.read_csv('D:\WILP\Datamining\Linear Regression\student_scores.csv')

dataset

dataset.shape

dataset.head()

dataset.describe()

#And finally, let's plot our data points on 2-D graph to eyeball our dataset and see if we can manually find any relationship between the data. 
#We can create the plot with the following script.

dataset.plot(x='Hours', y='Scores', style='o')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.show()

#Preparing the Data


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
X_train
X_test
y_train
y_test
#Training the Algorithm
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#plot train data
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.show()
#To retrieve the intercept:
print(regressor.intercept_)

#For retrieving the slope (coefficient of x):
print(regressor.coef_)

#This means that for every one unit of change in hours studied, the change in the score is about 9.91%. 
#Or in simpler words, if a student studies one hour more than they previously studied for an exam, they can expect to achieve an increase of 9.91% in the score achieved by the student previously.

#Making Predictions

y_pred = regressor.predict(X_test)

#The y_pred is a numpy array that contains all the predicted values for the input values in the X_test series.
#To compare the actual output values for X_test with the predicted values, execute the following script:

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
df


#Evaluating the Algorithm
from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print('R-Square:', metrics.r2_score(y_test, y_pred))

#Plot on test data
plt.scatter(X_test, y_test, color ='red') 
plt.plot(X_test, y_pred, color ='blue') 
  
plt.show() 