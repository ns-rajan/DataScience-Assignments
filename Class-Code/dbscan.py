# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:32:05 2020

@author: KIRAN
"""

import numpy as np
from sklearn.datasets.samples_generator import make_blobs
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import DBSCAN
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()


X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
plt.scatter(X[:,0], X[:,1])

#we find a suitable value for epsilon
neigh = NearestNeighbors(n_neighbors=2)
nbrs = neigh.fit(X)
#print(nbrs)
distances, indices = nbrs.kneighbors(X)
print(nbrs.kneighbors(X))

# sort and plot results.
distances = np.sort(distances, axis=0)
distances = distances[:,1]
plt.plot(distances)

#We train our model, selecting 0.3 for eps and setting min_samples to 5.

m = DBSCAN(eps=0.3, min_samples=5)
m.fit(X)

#The labels_ property contains the list of clusters and their respective points.
clusters = m.labels_

#we map every individual cluster to a color.
colors = ['royalblue', 'maroon', 'forestgreen', 'mediumorchid', 'tan', 'deeppink', 'olive', 'goldenrod', 'lightcyan', 'navy']
vectorizer = np.vectorize(lambda x: colors[x % len(colors)])

#plot and dark blue points were categorized as noise.
plt.scatter(X[:,0], X[:,1], c=vectorizer(clusters))

