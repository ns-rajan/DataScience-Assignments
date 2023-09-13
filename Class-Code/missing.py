#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:22:25 2019

@author: lovearora
"""

# Importing libraries
import pandas as pd
import numpy as np
from statistics import median

# Read csv file into a pandas dataframe
data = pd.read_csv(r".\property data.csv")

print(data)


# Take a look at the first few rows
print (data.head())

data.describe()

data.columns
data.values




# Looking at the ST_NUM column
#Standard Missing Values : missing values pandas can detect

print (data['ST_NUM'])

print(data['ST_NUM'].isnull())

print(data['ST_NUM'].notnull())


#Non-standard missing values
print(data['NUM_BEDROOMS'])
print(data['NUM_BEDROOMS'].isnull())


# Making a list of missing value types
missing_values = ["n/a", "na", "--"]
data = pd.read_csv(".\property data.csv", na_values = missing_values)

print(data['NUM_BEDROOMS'].isnull())

# Total missing values for each feature
print(data.isnull().sum())

# Any missing values?
print(data.isnull().values.any())

# Total number of missing values
print(data.isnull().sum().sum())

# checking the percentage of missing values in each variable
print(data.isnull().sum()/len(data)*100)

#Now we drop rows with at least one Nan value (Null value)
print(data.dropna())

#Now we drop a rows whose all data is missing or contain null values(NaN)
print(data.dropna(how = 'all'))

#Now we drop a columns which have at least 1 missing values
print(data.dropna(axis=1))

#Now we drop a ro which have at least 1 missing values
print(data.dropna(axis=0))

#Fill in missing values with zero
print(data.fillna(0))


# Replace using mean
m = data["ST_NUM"].mean()
print(m)
# fill missing values with mean column values
print(data['ST_NUM'].replace(np.nan, m))


# Replace using median ; inplace=True means that the changes are saved to the df right away
median = data['NUM_BEDROOMS'].median()
m1 = data['NUM_BEDROOMS'].fillna(median, inplace=True)
print(data['NUM_BEDROOMS'])

#Dropping the outlier rows with standard deviation
factor = 3
upper_lim = data['NUM_BEDROOMS'].mean () + data['NUM_BEDROOMS'].std () * factor
lower_lim = data['NUM_BEDROOMS'].mean () - data['NUM_BEDROOMS'].std () * factor

data = data[(data['NUM_BEDROOMS'] < upper_lim) & (data['NUM_BEDROOMS'] > lower_lim)]


#Dropping the outlier rows with Percentiles
upper_lim = data['NUM_BEDROOMS'].quantile(.95)
lower_lim = data['NUM_BEDROOMS'].quantile(.05)

data = data[(data['NUM_BEDROOMS'] < upper_lim) & (data['NUM_BEDROOMS'] > lower_lim)]
