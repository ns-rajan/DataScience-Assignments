from sklearn import preprocessing
import numpy as np


X = np.array([[0., 0., 5., 13., 9., 1.],[0., 0., 13., 15., 10., 15.],[0., 3., 15., 2., 0., 11.]])

print (preprocessing.scale(X))

#compute the mean and standard deviation 
scaler = preprocessing.StandardScaler().fit(X)

print(scaler.transform(X))

#scaling features to lie between a given minimum and maximum value, often between zero and one
#or so that the maximum absolute value of each feature is scaled to unit size


min_max_scaler = preprocessing.MinMaxScaler()
X_minmax = min_max_scaler.fit_transform(X)
print(X_minmax)

max_abs_scaler = preprocessing.MaxAbsScaler()
X_max = max_abs_scaler.fit_transform(X)
print(X_max)

