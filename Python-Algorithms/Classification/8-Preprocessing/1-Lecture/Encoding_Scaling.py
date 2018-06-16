# %%%%%%%%%%%%% Machine Learning %%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# Deepak Agarwal------>Email:deepakagarwal@gwmail.gwu.edu
# %%%%%%%%%%%%% Date:
# V1 June - 16 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Pre-processing  %%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%-----------------------------------------------------------------------
#%%-----------------------------------------------------------------------
# Importing the required packages

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import warnings
warnings.filterwarnings("ignore")

#%%-----------------------------------------------------------------------
# create a dataframe

df = pd.DataFrame([['green','M',10.1,5,'class1'], ['red','L',11.1,10,'class2'], ['blue','XL',12.1,15,'class1']])

# specify the column name
df.columns = ['color','size','price','count','classlabel']

# print the dataframe
print(df)

#%%-----------------------------------------------------------------------
# Manual Mapping of categorical column using dictionary

# specify the mapping
size_mapping = {'XL':3, 'L':2,'M':1}

# apply the mapping
df['size'] = df['size'].map(size_mapping)

# print the dataframe
print(df)

#%%-----------------------------------------------------------------------
# Manual Mapping of categorical column using dictionary
inv_size_mapping={v: k for k,v in size_mapping.items()}

# apply the inverse mapping
df['size'] = df['size'].map(inv_size_mapping)

# print the dataframe
print(df)

#%%-----------------------------------------------------------------------
# label encoding the target variable

class_le = LabelEncoder()

y = class_le.fit_transform(df['classlabel'].values)

print("Class variable after label encoding: ")
print(y)

#%%-----------------------------------------------------------------------
# revert label encoding to get original target variable

y_inv = class_le.inverse_transform(y)

print("Class variable inverse transform: ")
print(y_inv)

#%%-----------------------------------------------------------------------
# One Hot encoding using scikit learn
## copy the original dataframe for one hot encoding
df_copy = df.copy(deep=True)

## label encode the categorical variable
df_copy[['size','color']] = df_copy[['size','color']].apply(class_le.fit_transform)

## convert data type to object
df_copy[['size','color']] = df_copy[['size','color']].astype('object')

## exclude target variable
df_X = df_copy.iloc[:,:-1]

## check info of df
df_X.info()

## specify one hot encoder
ohe = OneHotEncoder(categorical_features='all', sparse=False)

## fit transform one hot encoder on categorical variables
print(ohe.fit_transform(df_X[['size','color']]))

#%%-----------------------------------------------------------------------
# One Hot encoding using pandas

## convert data type to object
df[['size','color']] = df[['size','color']].astype('object')

## one hot encode variables
print("Get dummy variables for all categorical predictor variables: ")

print(pd.get_dummies(df.iloc[:,:-1]))

#%%-----------------------------------------------------------------------
# Scaling the variables (We here assume X is array from train df where we fit and transform)
# select numerical columns
X = df[['price','count']].values

# print values
print("Values of the numeric columns: ")
print(X)

#%%-----------------------------------------------------------------------
# Standard scaling

stdsc = StandardScaler()

stdsc.fit(X)

X_std = stdsc.transform(X)

print("Values after standard scaling: ")
print(X_std)

#%%-----------------------------------------------------------------------
# Min Max scaling

minmax = MinMaxScaler()

minmax.fit(X)

X_minmax = minmax.transform(X)

print("Values after min-max scaling: ")
print(X_minmax)