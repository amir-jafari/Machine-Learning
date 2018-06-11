# %%-----------------------------------------------------------------------
# Importing the required packages

import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# %%-----------------------------------------------------------------------
#importing Dataset

# read data as panda dataframe
pima_data = pd.read_csv('pima_diabetes.csv', sep=',', header=0)

# printing the dataset shape
print("Dataset No. of Rows: ", pima_data.shape[0])
print("Dataset No. of Columns: ", pima_data.shape[1])

# printing the dataset observations
print("Dataset first few rows:\n ")
print(pima_data.head(2))

# printing the struture of the dataset
print("Dataset info:\n ")
print(pima_data.info())

# printing the summary statistics of the dataset
print(pima_data.describe(include='all'))

# %%-----------------------------------------------------------------------
# split the dataset

# separate the target variable
X = pima_data.values[:, :-1]
Y = pima_data.values[:, -1]

# split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)

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
print(classification_report(y_test,y_pred))
print("\n")


print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
print("\n")

print("ROC_AUC : ", roc_auc_score(y_test,y_pred_score[:,1]) * 100)
print("\n")

# %%-----------------------------------------------------------------------
# confusion matrix

conf_matrix = confusion_matrix(y_test, y_pred)
class_names = pima_data['Outcome'].unique()


df_cm = pd.DataFrame(conf_matrix, index=class_names, columns=class_names )

plt.figure(figsize=(5,5))
hm = sns.heatmap(df_cm, cbar=False, annot=True, square=True, fmt='d', annot_kws={'size': 20}, yticklabels=df_cm.columns, xticklabels=df_cm.columns)
hm.yaxis.set_ticklabels(hm.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
hm.xaxis.set_ticklabels(hm.xaxis.get_ticklabels(), rotation=0, ha='right', fontsize=20)
plt.ylabel('True label',fontsize=20)
plt.xlabel('Predicted label',fontsize=20)
# Show heat map
plt.tight_layout()
plt.show()
