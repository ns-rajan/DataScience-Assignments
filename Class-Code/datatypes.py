
import pandas as pd

df = pd.read_csv(r".\diabetes.csv")

print(df)

print(type(df))
print(df.dtypes)

# Drop the rows with 'nan' values 
df = df.dropna() 
print(df.info())


df = df.astype({"BMI":'int64', "Age":'float64'}) 
print(df.info())

