import pandas as pd

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

marks=[1,45,60,78,79,80,99,92]


#bins will decide equi depth or equi width
bins = [18, 25, 35, 60, 100]

binswidth=[0,20,40,60,80,100]

cats2 = pd.cut(marks,binswidth)

cats = pd.cut(ages, bins)

print(cats)

print(cats.categories)

print(pd.value_counts(cats))

#a parenthesis means that the side is open while the square bracket means it is closed (inclusive).
#Which side is closed can be changed by passing right=False :




cats1 =  pd.cut(ages, [18, 26, 36, 61, 100], right=False)

print(cats1)

# pass your own bin names by passing a list or array to the labels option
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']

cats3 = pd.cut(ages, bins, labels=group_names)

print(cats3)


#one hot encoding
gas = ["deisel", "deisel", "gas", "petrol" , "gas", "deisel"]
dummies = pd.get_dummies(gas)

print(dummies)



from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer

onehot_encoder = DictVectorizer()

instances = [{'city': 'New York'},{'city': 'San Francisco'},{'city': 'Chapel Hill'}]
print (onehot_encoder.fit_transform(instances).toarray())
print(onehot_encoder.vocabulary_)
