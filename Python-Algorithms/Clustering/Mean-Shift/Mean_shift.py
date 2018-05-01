print(__doc__)

from sklearn.cluster import AffinityPropagation
from sklearn import datasets
import matplotlib.pyplot as plt
from itertools import cycle
print(__doc__)
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth

iris = datasets.load_iris()
X = iris.data[:, [2,3]]
y = iris.target


# data pre processing
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X)
X = sc.transform(X)


# The following bandwidth can be automatically detected using
#bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)

ms = MeanShift(bandwidth=None,seeds=None,n_jobs=1)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)

print("number of estimated clusters : %d" % n_clusters_)

plt.figure(1)
plt.clf()

colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    my_members = labels == k
    cluster_center = cluster_centers[k]
    plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
    plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()