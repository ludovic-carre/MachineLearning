#!/usr/bin/python3.5
# -*-coding:Utf-8 -*
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

wine_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
df_wine = pd.read_csv(wine_url,header=None)
columns = ["Class label","Alcohol","Malic acid","Ash","Alcalinity of ash","Magnesium","Total phenols","Flavanoids","Nonflavanoid phenols","Proanthocyanins","Color intensity","Hue","OD280/OD315 of diluted wines","Proline"]
df_wine.columns = columns 

print("Class labels: ", np.unique(df_wine["Class label"]),'\n')
print(df_wine.head(),'\n')

# First column is class label
classes =  df_wine.iloc[:, 0].values
# the rest is the data
values =  df_wine.iloc[:, 1:].values
# 30 percent of the dataset will the test set
train_values, test_values, train_classes, test_classes = train_test_split(values,classes,test_size=0.3,random_state=0)

stdsc  = StandardScaler()
std_train_values = stdsc.fit_transform(train_values)
std_test_values = stdsc.transform(test_values)
print(std_train_values[0:5,:])
