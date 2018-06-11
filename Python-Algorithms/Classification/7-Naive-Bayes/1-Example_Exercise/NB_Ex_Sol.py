# %%-----------------------------------------------------------------------
# Importing the required packages

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score

# %%-----------------------------------------------------------------------

data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases" + "/adult/adult.data", sep=',\s', header=None, engine='python')

data.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education_num',
                'marital_status', 'occupation', 'relationship',
                'race', 'sex', 'capital_gain', 'capital_loss',
                'hours_per_week', 'native_country', 'income']

# %%-----------------------------------------------------------------------
# Data preprocessing

# look at first few rows
data.head()

# replace missing characters as NaN
data.replace('?', np.NaN, inplace=True)

# check the structure of data
data.info()

# check the null values in each column
data.isnull().sum()

# check the summary of the data
data.describe(include='all')

# replace categorical data with the most frequent value in that column
data = data.apply(lambda x: x.fillna(x.value_counts().index[0]))

# again check the null values in each column
data.isnull().sum()

# %%-----------------------------------------------------------------------
# One Hot Encoding the variables

# encoding the features using get dummies
X_data = pd.get_dummies(data.iloc[:, :-1])

X = X_data.values


# encoding the class with sklearn's LabelEncoder
Y_data = data.values[:, -1]

class_le = LabelEncoder()

# fit and transform the class
y = class_le.fit_transform(Y_data)

# %%-----------------------------------------------------------------------
# split the data

# Spliting the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

# %%-----------------------------------------------------------------------
# perform training

# creating the classifier object
clf = GaussianNB()

# performing training
clf.fit(X_train, y_train)

# %%-----------------------------------------------------------------------
# make predictions

# predicton on test
y_pred = clf.predict(X_test)

y_pred_score = clf.predict_proba(X_test)

# %%-----------------------------------------------------------------------
# calculate metrics

print("\n")

print("Classification Report: ")
print(classification_report(y_test, y_pred))
print("\n")

print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
print("\n")

print("ROC_AUC : ", roc_auc_score(y_test, y_pred_score[:, 1]) * 100)
print("\n")

# %%-----------------------------------------------------------------------
# confusion matrix

# create consufion matrix and get label names
conf_matrix = confusion_matrix(y_test, y_pred)
class_names = data['income'].unique()

# create a dataframe for confusion matrix
df_cm = pd.DataFrame(conf_matrix, index=class_names, columns=class_names)

# provide figure size
plt.figure(figsize=(5, 5))
hm = sns.heatmap(df_cm, cbar=False, annot=True, square=True, fmt='d', annot_kws={'size': 20}, yticklabels=df_cm.columns, xticklabels=df_cm.columns)
hm.yaxis.set_ticklabels(hm.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
hm.xaxis.set_ticklabels(hm.xaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
plt.ylabel('True label', fontsize=20)
plt.xlabel('Predicted label', fontsize=20)

# show heat map
plt.tight_layout()
plt.show()