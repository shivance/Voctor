import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, _tree
import joblib
import matplotlib.pyplot as plt

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

x = train.iloc[:, 0:132].values
y = train.iloc[:, -1].values

red_dim = train.groupby(train["prognosis"]).max()
labelenc = LabelEncoder()
y = labelenc.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=2)

dtree = DecisionTreeClassifier()
dtree.fit(x_train, y_train)

joblib.dump(dtree, "dtree.pkl")

'''
# For running code in terminal :
def main_execution():

    def print_disease(node):
        node = node[0]
        val = node.nonzero()
        disease = labelenc.inverse_transform(val[0])
        return disease
    
'''
