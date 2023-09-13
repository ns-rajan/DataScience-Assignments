# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 16:28:27 2020

@author: Vishal
"""


import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


play_tennis = pd.read_csv(r"C:\Users\Vishal\Desktop\PlayTennis.csv")
play_tennis.head()
number = LabelEncoder()
play_tennis['Outlook'] = number.fit_transform(play_tennis['Outlook'])

play_tennis['Temperature'] = number.fit_transform(play_tennis['Temperature'])

play_tennis['Humidity'] = number.fit_transform(play_tennis['Humidity'])

play_tennis['Wind'] = number.fit_transform(play_tennis['Wind'])

play_tennis['Play Tennis'] = number.fit_transform(play_tennis['Play Tennis'])
play_tennis
###########################
# Train Naive Bayes Model
###########################
#def Naive_Bayes(data):
# Step 1: Calculate Prior Probability
y_unique = play_tennis['Play Tennis'].unique()
y_unique
prior_probability = np.zeros(len(play_tennis['Play Tennis'].unique()))
for i in range(0,len(y_unique)):
    prior_probability[i]=sum(play_tennis['Play Tennis']==y_unique[i])/len(play_tennis['Play Tennis'])
    print(prior_probability[i])
    
# Step 2: Calculate Conditional Probability
play_tennis.shape
conditional_probability = {}
type(conditional_probability)

conditional_probability = {}
for column in play_tennis.columns:
    x_unique = list(set(play_tennis[column]))
    x_conditional_probability = np.zeros((len(play_tennis[column].unique()),len(set(play_tennis[column]))))
    for j in range(0,len(y_unique)):
        for k in range(0,len(x_unique)):
            x_conditional_probability[j,k]=play_tennis.loc[(play_tennis[column]==x_unique[k])&(play_tennis['Play Tennis']==y_unique[j])].shape[0]/sum(play_tennis['Play Tennis']==y_unique[j])
            print(column,j,k,x_conditional_probability[j,k])

  
