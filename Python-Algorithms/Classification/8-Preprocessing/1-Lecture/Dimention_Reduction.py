# %%%%%%%%%%%%% Machine Learning %%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# Deepak Agarwal------>Email:deepakagarwal@gwmail.gwu.edu
# %%%%%%%%%%%%% Date:
# V1 June - 16 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Pre-processing  %%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%-----------------------------------------------------------------------
### Citation : The code has been taken from chapter 5 of book 'Python with Machine Learning' by Sebastian Raschka ###

#%%-----------------------------------------------------------------------
# Importing the required packages

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings("ignore")

# Plot decision regions
import plot_decision_regions as pp

#%%-----------------------------------------------------------------------
# Importing dataset

## read data as panda dataframe
df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',header=None)

# assign the column names
df_wine.columns = ['Class label', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols',
                   'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',  'Color intensity', 'Hue',
                   'OD280/OD315 of diluted wines', 'Proline']


# printing the dataset shape
print("Dataset No. of Rows: ", df_wine.shape[0])
print("Dataset No. of Columns: ", df_wine.shape[1])

# printing the dataset observations
print("Dataset first few rows:\n ")
print(df_wine.head())

# printing the struture of the dataset
print("Dataset info:\n ")
print(df_wine.info())

# printing the summary statistics of the dataset
print(df_wine.describe(include='all'))


#%%-----------------------------------------------------------------------
# Split the data

## specify predictor and target variables
X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values

## split data for train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)


#%%-----------------------------------------------------------------------
# Scale the data

sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)

#%%-----------------------------------------------------------------------
# Apply PCA

pca = PCA()
X_train_pca = pca.fit_transform(X_train_std)

print("Explained Variance:\n")
print(pca.explained_variance_ratio_)


#%%-----------------------------------------------------------------------
# Plot the explained variance

plt.bar(range(1, 14), pca.explained_variance_ratio_, alpha=0.5, align='center')
plt.step(range(1, 14), np.cumsum(pca.explained_variance_ratio_), where='mid')
plt.ylabel('Explained variance ratio')
plt.xlabel('Principal components')
plt.show()



#%%-----------------------------------------------------------------------
# Apply PCA by specify components

pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train_std)
X_test_pca = pca.transform(X_test_std)

#%%-----------------------------------------------------------------------
# Plot the principal components

plt.scatter(X_train_pca[:, 0], X_train_pca[:, 1])
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.show()

# %%-----------------------------------------------------------------------
# Apply logistic regression after PCA

lr = LogisticRegression()
lr = lr.fit(X_train_pca, y_train)

# %%-----------------------------------------------------------------------
# Plot decision regions on train data

pp.plot_decision_regions(X_train_pca, y_train, classifier=lr)
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.legend(loc='lower left')
plt.tight_layout()
plt.show()


# %%-----------------------------------------------------------------------
# Plot decision regions on test data

pp.plot_decision_regions(X_test_pca, y_test, classifier=lr)
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.legend(loc='lower left')
plt.tight_layout()
plt.show()


# %%-----------------------------------------------------------------------
# Apply LDA

lda = LDA(n_components=2)
X_train_lda = lda.fit_transform(X_train_std, y_train)

# %%-----------------------------------------------------------------------
# Apply logistic regression after LDA

lr = LogisticRegression()
lr = lr.fit(X_train_lda, y_train)

pp.plot_decision_regions(X_train_lda, y_train, classifier=lr)
plt.xlabel('LD 1')
plt.ylabel('LD 2')
plt.legend(loc='lower left')
plt.tight_layout()
plt.show()

# %%-----------------------------------------------------------------------
X_test_lda = lda.transform(X_test_std)

pp.plot_decision_regions(X_test_lda, y_test, classifier=lr)
plt.xlabel('LD 1')
plt.ylabel('LD 2')
plt.legend(loc='lower left')
plt.tight_layout()
plt.show()