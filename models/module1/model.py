import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

x = train.iloc[:, 0:132].values
y = train.iloc[:, -1].values

red_dim = train.groupby(train["prognosis"]).max()
labelenc = LabelEncoder()
y = labelenc.fit_transform(y)
