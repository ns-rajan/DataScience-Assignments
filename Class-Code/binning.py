def equiwidth(arr1, m): 

    a = len(arr1) 

    w = int((max(arr1) - min(arr1)) / m) 

    min1 = min(arr1) 

    arr = [] 

    for i in range(0, m + 1): 

        arr = arr + [min1 + w * i] 

    arri=[] 

      

    for i in range(0, m): 

        temp = [] 

        for j in arr1: 

            if j >= arr[i] and j <= arr[i+1]: 

                temp += [j] 

        arri += [temp] 

    print(arri)  

  
#data to be binned 

data = [5, 10, 11, 13, 15, 35, 50, 55, 72, 92, 204, 215] 
#no of bins 

m = 3 
equiwidth(data,m)


import numpy as np   

import math 

from sklearn.datasets import load_iris 

from sklearn import datasets, linear_model, metrics  

  
# load iris data set 

dataset = load_iris()    

a = dataset.data 

b = np.zeros(150) 

  
# take 1st column among 4 column of data set  

for i in range (150): 

    b[i]=a[i,1]    

  

b=np.sort(b)  #sort the array 

  
# create bins 

bin1=np.zeros((30,5))  

bin2=np.zeros((30,5)) 

bin3=np.zeros((30,5)) 

  
# Bin mean 

for i in range (0,150,5): 

    k=int(i/5) 

    mean=(b[i] + b[i+1] + b[i+2] + b[i+3] + b[i+4])/5

    for j in range(5): 

        bin1[k,j]=mean 

print("Bin Mean: \n",bin1) 

     
# Bin boundaries 

for i in range (0,150,5): 

    k=int(i/5) 

    for j in range (5): 

        if (b[i+j]-b[i]) < (b[i+4]-b[i+j]): 

            bin2[k,j]=b[i] 

        else: 

            bin2[k,j]=b[i+4]        

print("Bin Boundaries: \n",bin2) 

  
# Bin median 

for i in range (0,150,5): 

    k=int(i/5) 

    for j in range (5): 

        bin3[k,j]=b[i+2] 

print("Bin Median: \n",bin3)