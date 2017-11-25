import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans
# ----------------------------------------------------------------------------------------------------------------------
x = [1, 5, 1.5, 8, 1, 9]
y = [2, 8, 1.8, 8, 0.6, 11]
plt.figure(1)
plt.scatter(x,y)
X = np.array([[1, 2],
              [5, 8],
              [1.5, 1.8],
              [8, 8],
              [1, 0.6],
              [9, 11]])
# ----------------------------------------------------------------------------------------------------------------------
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
# ----------------------------------------------------------------------------------------------------------------------
print(centroids)
print(labels)
# ----------------------------------------------------------------------------------------------------------------------
colors = ["g.","r.","c.","y."]
plt.figure(2)
for i in range(len(X)):
    print("coordinate:",X[i], "label:", labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)
plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)

plt.show()
# ----------------------------------------------------------------------------------------------------------------------