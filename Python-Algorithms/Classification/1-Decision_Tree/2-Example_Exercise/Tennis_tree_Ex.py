# %%%%%%%%%%%%% Machine Learning %%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Authors  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Dr. Amir Jafari------>Email: amir.h.jafari@okstate.edu
# Deepak Agarwal------>Email:deepakagarwal@gwmail.gwu.edu
# %%%%%%%%%%%%% Date:
# V1 June - 05 - 2018
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%% Decision Tree  %%%%%%%%%%%%%%%%%%%%%%%%%%
#%%-----------------------------------------------------------------------
#%%-----------------------------------------------------------------------
# Exercise
#%%-----------------------------------------------------------------------

# 1:
# Build the simple tennis table we just reviewed, in python as a dataframe. Label the columns.
# We are going to calculate entropy manually, but in python.
# Make sure to enter all variables as binary vs. the actual categorical names
# Name the dataframe tennis_ex.
#%%-----------------------------------------------------------------------




#%%-----------------------------------------------------------------------
# 2:
# Build a function that will calculate entropy. Calculate entropy for the table we just went over
# in the example, but in python
# This is for the first split.
#%%-----------------------------------------------------------------------








#%%-----------------------------------------------------------------------
# 3:
# Run the decision tree algorithm and find out the best feature and graph it.
#%%-----------------------------------------------------------------------
# Importing the required packages
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn import tree
#%%-----------------------------------------------------------------------
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
#%%-----------------------------------------------------------------------

# Libraries to display decision tree
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz
import webbrowser
#%%--------------------------------Save Console----------------------------

# old_stdout = sys.stdout
# log_file = open("console.txt", "w")
# sys.stdout = log_file

#%%-----------------------------------------------------------------------
tennis = pd.read_csv('tennis.csv')




