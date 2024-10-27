"""
This script demonstrates the training of the Iris dataset using SOM algorithm, leveraging GPU acceleration.

Requirements:
- This script is specifically designed for execution in environments with GPU support.
- The SOMGpu class from the NNSOM library is used for SOM operations on GPU.

Key Operations:
- Data loading and preprocessing using sklearn.
- SOM initialization and training on GPU using SOMGpu.
- Saving the trained SOM model externally.

Note:
- Ensure a compatible GPU and necessary driver support are available in the execution environment.
- The script uses absolute paths and assumes a specific directory structure for saving the model.

To execute this script:
- A Python environment with the necessary libraries (NNSOM, numpy, cupy) installed is required.
- The script assumes the presence of a CUDA-compatible GPU and appropriate setup for PyCUDA.
"""
#%%-----------------------------------------------------------------------------------------------------------

# Importing Library
from NNSOM.som_gpu import SOMGpu

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler

import os
#%%-----------------------------------------------------------------------------------------------------------

# SOM Parameters
SOM_Row_Num = 4  # The number of row used for the SOM grid.
Dimensions = (SOM_Row_Num, SOM_Row_Num) # The dimensions of the SOM grid.

# Training Parameters
Epochs = 500
Steps = 100
Init_neighborhood = 3

# Random State
SEED = 1234567
rng = default_rng(SEED)

# Data Preparation
iris = load_iris()
X = iris.data
y = iris.target

# Preprocessing data
X = X[rng.permutation(len(X))]
y = y[rng.permutation(len(X))]

# Define the normalize funciton
scaler = MinMaxScaler(feature_range=(-1, 1))
#%%-----------------------------------------------------------------------------------------------------------

# Training
som = SOMGpu(Dimensions)
som.init_w(X, norm_func=scaler.fit_transform)
som.train(X, Init_neighborhood, Epochs, Steps, norm_func=scaler.fit_transform)
#%%-----------------------------------------------------------------------------------------------------------

# Define the directory path for saving the model outside the repository
model_dir = os.path.abspath(os.path.join(os.getcwd(), "..", "..", "..", "..", "Model"))
# Create the directory if it doesn't exist
if not os.path.exists(model_dir):
    os.makedirs(model_dir)
Trained_SOM_File = "SOM_Model_iris_Epoch_" + str(Epochs) + '_Seed_'  + str(SEED) + '_Size_' + str(SOM_Row_Num) + '.pkl'
#%%-----------------------------------------------------------------------------------------------------------

# Save the model
som.save_pickle(Trained_SOM_File, model_dir + os.sep)
#%%-----------------------------------------------------------------------------------------------------------

# Extract Cluster details
clust, dist, mdist, clustSize = som.cluster_data(X)
#%%-----------------------------------------------------------------------------------------------------------

# Find quantization error
quant_err = som.quantization_error(dist)
print('Quantization error: ' + str(quant_err))
#%%-----------------------------------------------------------------------------------------------------------

# Find topological error
top_error_1, top_error_1_2 =  som.topological_error(X)
print('Topological Error (1st neighbor) = ' + str(top_error_1) + '%')
print('Topological Error (1st and 2nd neighbor) = ' + str(top_error_1_2) + '%')
#%%-----------------------------------------------------------------------------------------------------------

# Find Distortion Error
som.distortion_error(X)

"""
Note: 
The 'SOMGpu' class is used exclusively for training the Self-Organizing Maps using GPU acceleration. 
For visualization purposes, including the display of SOM topology, histograms, and other graphical 
representations of the SOM structure, use the 'SOMPlots' class. The 'SOMPlots' class is designed 
to automatically detect and utilize GPU capabilities via CuPy if available; otherwise, it falls 
back to CPU processing. This ensures optimal performance in environments with GPU support while 
still maintaining functionality in CPU-only environments.
"""
