# %%%%%%%%%%%%% Machine Learning %%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# Deepak Agarwal------>Email:deepakagarwal@gwmail.gwu.edu
# %%%%%%%%%%%%% Date:
# V1 June - 13 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% K-Nearest Neighbor  %%%%%%%%%%%%%%%%%%%%%
#%%-----------------------------------------------------------------------
# Importing the required packages
import csv
import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

#%%-----------------------------------------------------------------------
#importing Dataset

# open the file and subset for the lines where the data starts
with open('chronic_kidney_disease.arff') as file:
    lines = file.readlines()[29:]

# define empty list to store data
datalist = []

# strip data lines with comma
for line in lines:
    row = list(filter(None,[x.strip() for x in line.split(',')]))
    datalist.append(row)

# specify the csv file name
csvfile = "chronic_kidney.csv"

# open the csv file for writing data
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(datalist)

#%%-----------------------------------------------------------------------
# read data as panda dataframe
disease_data = pd.read_csv("/home/deepak/Desktop/test_pychrm/chronic_kidney.csv",header=None)

# define column names
disease_data.columns = ['age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc','sod','pot','hemo','pcv',
                'wbcc','rbcc','htn','dm','cad','appet','pe','ane','class']


#%%-----------------------------------------------------------------------

# printing the dataset shape
print("Dataset No. of Rows: ", disease_data.shape[0])
print("Dataset No. of Columns: ", disease_data.shape[1])

# printing the dataset observations
print("Dataset first few rows:\n ")
print(disease_data.head(2))

# printing the struture of the dataset
print("Dataset info:\n ")
print(disease_data.info())

# printing the summary statistics of the dataset
print(disease_data.describe(include='all'))

#%%-----------------------------------------------------------------------
# data preprocessing

# specify the numeric columns
numeric_cols = ['age','bp','bgr','bu','sc','sod','pot','hemo','pcv', 'wbcc','rbcc']

# convert the data type of specified columns to numeric
disease_data[numeric_cols] = disease_data[numeric_cols].apply(pd.to_numeric, errors='coerce')

# replace the special characters with NaN
disease_data.replace('?', np.NaN, inplace=True)

# total number of null column-wise
print(disease_data.isnull().sum())

#%%-----------------------------------------------------------------------

# data imputation

# median imputation
median_imputer = Imputer(missing_values='NaN', strategy='median', axis=0)

disease_data[numeric_cols]= median_imputer.fit_transform(disease_data[numeric_cols])

# specify categorical columns
cat_columns = disease_data.columns.difference(numeric_cols)

# most_frequent = Imputer(missing_values="NaN", strategy="most_frequent")
# disease_data[cat_columns]= most_frequent.fit_transform(disease_data[cat_columns])

# mode imputation
disease_data[cat_columns] = disease_data[cat_columns].apply(lambda x:x.fillna(x.value_counts().index[0]))


print(disease_data.isnull().sum())

#%%-----------------------------------------------------------------------
# split the dataset and encode the variables
# One Hot Encoding the variables

# encoding the features using get dummies
X_data = pd.get_dummies(disease_data.iloc[:, :-1])
X = X_data.values

# encoding the class with sklearn's LabelEncoder
Y_data = disease_data.values[:, -1]

class_le = LabelEncoder()

# fit and transform the class
y = class_le.fit_transform(Y_data)
#%%-----------------------------------------------------------------------

# split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100, stratify=y)

#%%-----------------------------------------------------------------------
# data pre-processing
# standardize the data
stdsc = StandardScaler()

stdsc.fit(X_train)

X_train_std = stdsc.transform(X_train)
X_test_std = stdsc.transform(X_test)

#%%-----------------------------------------------------------------------
# perform training
# creating the classifier object
clf = KNeighborsClassifier(n_neighbors=3)

# performing training
clf.fit(X_train_std, y_train)

#%%-----------------------------------------------------------------------
# make predictions

# prediction on test
y_pred = clf.predict(X_test_std)

# prediction probabilities on test
y_pred_score = clf.predict_proba(X_test_std)

#%%-----------------------------------------------------------------------
# calculate metrics

print("\n")
print("Classification Report: ")
print(classification_report(y_test,y_pred))
print("\n")


print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
print("\n")


print("ROC_AUC : ", roc_auc_score(y_test,y_pred_score[:,1]) * 100)
print("\n")

#%%-----------------------------------------------------------------------
# confusion matrix

conf_matrix = confusion_matrix(y_test, y_pred)
class_names = disease_data['class'].unique()


df_cm = pd.DataFrame(conf_matrix, index=class_names, columns=class_names )

plt.figure(figsize=(5,5))

hm = sns.heatmap(df_cm, cbar=False, annot=True, square=True, fmt='d', annot_kws={'size': 20}, yticklabels=df_cm.columns, xticklabels=df_cm.columns)
hm.yaxis.set_ticklabels(hm.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=10)
hm.xaxis.set_ticklabels(hm.xaxis.get_ticklabels(), rotation=0, ha='right', fontsize=10)
plt.ylabel('True label',fontsize=20)
plt.xlabel('Predicted label',fontsize=20)
plt.tight_layout()
plt.show()