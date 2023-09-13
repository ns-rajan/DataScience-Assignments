import pandas as pd

data = pd.read_csv("D:\WILP\Datamining\DataPreprocessing\sample.csv")
data1 = pd.read_csv("D:\WILP\Datamining\DataPreprocessing\\sample1.csv")

print(data)
#print(data1)

#melt Gather columns into rows.
print(pd.melt(data))
print(pd.melt(data1))


#Append rows of DataFrames
x = pd.concat([data,data1], sort = 'True')

print(x)

#Append columns of DataFrames
x1 = pd.concat([data,data1], axis=1)
print(x1)
