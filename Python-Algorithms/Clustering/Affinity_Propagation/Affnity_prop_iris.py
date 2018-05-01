print(__doc__)

from sklearn.cluster import AffinityPropagation
from sklearn import datasets
import matplotlib.pyplot as plt
from itertools import cycle

iris = datasets.load_iris()
X = iris.data[:, [2,3]]
y = iris.target


# data pre processing
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X)
X = sc.transform(X)


#-----------------------------------------------------------------------------


af = AffinityPropagation(damping=0.9,max_iter=500,convergence_iter=150,
                         copy=True,preference=-30,affinity='euclidean')
af.fit(X)
# this methods infer there are 5 class
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

n_clusters_ = len(cluster_centers_indices)

print('Estimated number of clusters: %d' % n_clusters_)

plt.figure(1)
plt.clf()

colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    class_members = labels == k
    cluster_center = X[cluster_centers_indices[k]]
    plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
    plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)
    for x in X[class_members]:
        plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()