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

import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings("ignore")
# %%-----------------------------------------------------------------------
# Importing dataset

df = pd.read_csv("housing.csv")
print(df.head())

# %%-----------------------------------------------------------------------
# Information about dataset

## this provides us total number of non null observations present including the total number of entries.
## once number of entries isn’t equal to number of non null observations, we can begin to suspect missing values.
df.info()

print('\n')

## get total number of NAs in the dataset and sort them to see column with maximum NAs at the top
print(df.isnull().sum().sort_values(ascending=False))
print('\n')

## print the number of rows and columns
print('\n'+"Data set rows and columns: "+str(df.shape)+'\n')



# %%-----------------------------------------------------------------------
# Dropping missing values row-wise

## drop rows with any column value zero in a row
print(df.dropna())

## drop rows with any column value zero in a row
print(df.dropna(axis=0))

## drop rows with all column value zero in a row
print(df.dropna(how='all'))

# %%-----------------------------------------------------------------------
# Dropping missing values column-wise

## drop columns with NA values and save it as seperate df
df_no_missing_cols = df.dropna(axis=1)

## get total number of NAs in the dataset and sort them to see column with maximum NAs at the top
print(df_no_missing_cols.isnull().sum().sort_values(ascending=False))

## print the number of rows and columns
print('\n'+"Data set rows and columns: "+str(df_no_missing_cols.shape)+'\n')

# %%-----------------------------------------------------------------------
# Inspect Missing Columms

## subset the dataframe with columns having missing values
null_data = df.loc[:,df.isna().any()]

print('\n')
## print the number of rows and columns
print(null_data.shape)

print('\n')
## print the name of columns
print(null_data.columns)

print('\n')
## information about dataset
null_data.info()

print('\n')
## get total number of NAs in the dataset and sort them to see columns with maximum NAs at the top
print(null_data.isnull().sum().sort_values(ascending=False))

print('\n')
## get percent of of NAs in the dataset and sort them to see column with maximum percent NAs at the top
print(null_data.isnull().sum().sort_values(ascending=False)/len(df)*100)

# %%-----------------------------------------------------------------------
# Dropping on basis of null values in columns (one or the other)

## print the number of rows and columns
print('\n'+"Data set rows and columns: "+str(null_data.shape)+'\n')

## drop columns with too many NAs (more than 50%)
null_data.drop(['PoolQC','MiscFeature','Alley','Fence'],axis=1,inplace=True)

## again print the number of rows and columns
print('\n'+"Data set rows and columns: "+str(null_data.shape)+'\n')

## get total number of NAs in the dataset and sort them to see columns with maximum NAs at the top
print(null_data.isnull().sum().sort_values(ascending=False))

print('\n')
# %%-----------------------------------------------------------------------
# Imputation using pandas

## get the numeric columns
numeric_cols = null_data.select_dtypes(include=[np.number]).columns

print('\n')
## print the numeric columns
print(numeric_cols)

## get the categorical columns
cat_columns = null_data.columns.difference(numeric_cols)

print('\n')
## print the categorical columns
print(cat_columns)


# %%-----------------------------------------------------------------------
# Copy the dataframe

null_data_imp_pandas = null_data.copy(deep=True)

# %%-----------------------------------------------------------------------
# Impute numerical columns using median

print('\n')

## get total number of NAs in the dataset and sort them to see columns with maximum NAs at the top
print(null_data_imp_pandas.isnull().sum().sort_values(ascending=False))

# impute numerical columns with respective median values
null_data_imp_pandas[numeric_cols] = null_data_imp_pandas[numeric_cols].apply(lambda x:x.fillna(x.median))

print('\n')

## get total number of NAs in the dataset and sort them to see columns with maximum NAs at the top
print(null_data_imp_pandas.isnull().sum().sort_values(ascending=False))

# %%-----------------------------------------------------------------------
# Impute categorical columns using mode

# impute categorical columns with respective mode values
null_data_imp_pandas[cat_columns] = null_data_imp_pandas[cat_columns].apply(lambda x:x.fillna(x.value_counts().index[0]))

print('\n')

## get total number of NAs in the dataset and sort them to see columns with maximum NAs at the top
print(null_data_imp_pandas.isnull().sum().sort_values(ascending=False))

print('\n')
# %%-----------------------------------------------------------------------
# Imputation using scikit-learn

# Copy the dataframe
null_data_imp_scikit = null_data.copy(deep=True)

## get total number of NAs in the dataset and sort them to see columns with maximum NAs at the top
print(null_data_imp_scikit.isnull().sum().sort_values(ascending=False))

print('\n')
# %%-----------------------------------------------------------------------
# Mean Imputation

# specify the imputer
imp = Imputer(missing_values='NaN',strategy='median',axis=0)

# fit and transform the imputer
null_data_imp_scikit[numeric_cols] = imp.fit_transform(null_data_imp_scikit[numeric_cols])

## get total number of NAs in the dataset and sort them to see columns with maximum NAs at the top
print(null_data_imp_scikit.isnull().sum().sort_values(ascending=False))

print('\n')
# %%-----------------------------------------------------------------------

# print categorical columns data
print(null_data_imp_scikit[cat_columns].head(10))

# print information about data
null_data_imp_scikit.info()

print('\n')
# %%-----------------------------------------------------------------------
# check category-wise values in a columns before imputation
print(null_data_imp_scikit['FireplaceQu'].value_counts())

print('\n')
# %%-----------------------------------------------------------------------
# replace NaN with 0 for LabelEncoder
null_data_imp_scikit.replace(np.NaN,0,inplace=True)

# %%-----------------------------------------------------------------------
# check category-wise values in a columns after replacing NaN with 0 for LabelEncoder
print(null_data_imp_scikit['FireplaceQu'].value_counts())

print('\n')
# %%-----------------------------------------------------------------------
# change datatype of all columns to string for LabelEncoding
null_data_imp_scikit[cat_columns] = null_data_imp_scikit[cat_columns].astype('str')

# %%-----------------------------------------------------------------------
# Label encode the categorical variables to apply scikit learn mode imputation

# specify label encoder
le = LabelEncoder()

# fit transform label encoder
null_data_imp_scikit[cat_columns] = null_data_imp_scikit[cat_columns].apply(le.fit_transform)

# check category-wise values in a columns before imputation
print(null_data_imp_scikit['FireplaceQu'].value_counts())

print('\n')
# %%-----------------------------------------------------------------------

# replace 0 back with NaN
null_data_imp_scikit.replace(0,np.NaN,inplace=True)

# print the categorical columns after label encoding
print(null_data_imp_scikit[cat_columns].head(10))

print('\n')
# %%-----------------------------------------------------------------------
# Mode Imputation

# specify the imputer
catimp=Imputer(missing_values="NaN", strategy="most_frequent")

# fit and transform the imputer
null_data_imp_scikit[cat_columns] = catimp.fit_transform(null_data_imp_scikit[cat_columns])

# %%-----------------------------------------------------------------------

# check category-wise values in a columns after imputation
print(null_data_imp_scikit['FireplaceQu'].value_counts())

print('\n')
# change datatype of all columns to int
null_data_imp_scikit[cat_columns] = null_data_imp_scikit[cat_columns].astype('int')

# print the categorical columns after label encoding
print(null_data_imp_scikit[cat_columns].head(10))
