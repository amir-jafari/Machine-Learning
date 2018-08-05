#%%--------------------------------------------------------------
#%% Source: https://peterwittek.com/somoclu-in-python.html
#%%--------------------------------------------------------------
#%% Install https://pypi.org/project/somoclu/1.6.1/
#%% for windows download the whl file and pip install it
#%% for mac and ubuntu pip install somoclu or download the whl file
#%%--------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import somoclu
#%%-------------------------------------------------------------------------------------
c1 = np.random.rand(50, 3)/5
c2 = (0.6, 0.1, 0.05) + np.random.rand(50, 3)/5
c3 = (0.4, 0.1, 0.7) + np.random.rand(50, 3)/5
data = np.float32(np.concatenate((c1, c2, c3)))
colors = ["red"] * 50
colors.extend(["green"] * 50)
colors.extend(["blue"] * 50)
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=colors)
labels = range(150)
#%%-------------------------------------------------------------------------------------
n_rows, n_columns = 100, 160
som = somoclu.Somoclu(n_columns, n_rows, data=data)
som.train(epochs=10)
som.view_umatrix(bestmatches=True, bestmatchcolors=colors, labels=labels)
#%%-------------------------------------------------------------------------------------
som.view_component_planes()
#%%-------------------------------------------------------------------------------------
som.view_umatrix(bestmatches=True, bestmatchcolors=colors, labels=labels)
#%%-------------------------------------------------------------------------------------
som.view_umatrix(bestmatches=True, bestmatchcolors=colors, labels=labels, zoom=((50, n_rows), (100, n_columns)))
#%%-------------------------------------------------------------------------------------
som = somoclu.Somoclu(n_columns, n_rows, data=data, maptype="toroid")
som.train()
som.view_umatrix(bestmatches=True, bestmatchcolors=colors)
#%%-------------------------------------------------------------------------------------
som = somoclu.Somoclu(n_columns, n_rows, data=data, gridtype="hexagonal")
som.train()
som.view_umatrix(bestmatches=True, bestmatchcolors=colors)
#%%-------------------------------------------------------------------------------------
som = somoclu.Somoclu(n_columns, n_rows, data=data, maptype="toroid", initialization="pca")
som.train()
som.view_umatrix(bestmatches=True, bestmatchcolors=colors)
#%%-------------------------------------------------------------------------------------
som.cluster()
som.view_umatrix(bestmatches=True)
#%%-------------------------------------------------------------------------------------
from sklearn.cluster import DBSCAN
algorithm = DBSCAN()
som.cluster(algorithm=algorithm)
som.view_umatrix(bestmatches=True)
#%%-------------------------------------------------------------------------------------
som = somoclu.Somoclu(n_columns, n_rows, data=data, maptype="toroid")
som.train()
#%%-------------------------------------------------------------------------------------
c2_shifted = c2 - 0.2
updated_data = np.float32(np.concatenate((c1, c2_shifted, c3)))
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(updated_data[:, 0], updated_data[:, 1], updated_data[:, 2], c=colors)
#%%-------------------------------------------------------------------------------------
som.view_umatrix(bestmatches=True, bestmatchcolors=colors, labels=labels)
som.update_data(updated_data)
som.train(epochs=2, radius0=20, scale0=0.02)
som.view_umatrix(bestmatches=True, bestmatchcolors=colors, labels=labels)
#%%-------------------------------------------------------------------------------------
