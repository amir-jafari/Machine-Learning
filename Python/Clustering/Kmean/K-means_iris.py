# import data
from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
X = iris.data[:, [2,3]]
y = iris.target
#-----------------------------------------------------------------------------
# data pre processing
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))
#-----------------------------------------------------------------------------

def loss_function(x,z):
    predict1 = z.fit_predict(x)
    sum_distance = 0
    for i in range(0,len(z.cluster_centers_)):
        sum_distance += sum(sum((x[predict1 == i]-z.cluster_centers_[i])**2))
    return sum_distance

import plot_decision_regions as pp
import matplotlib.pyplot as plt
plt.figure(1)
from sklearn.cluster import KMeans

loss_array = []

for i in range(1,6):
    kmeans = KMeans(n_clusters = i, random_state = 0)
    kmeans.fit(X_train_std)
    loss_array.append(loss_function(X_test_std,kmeans))
plt.figure(1)
plt.scatter([1,2,3,4,5], loss_array)

kmeans  = KMeans(n_clusters = 5, random_state= 0)
# -learn without label
kmeans.fit(X_train_std)
loss = loss_function(X_test_std,kmeans)
print('loss is : {} when k = 5'.format(loss))
plt.figure(2)
pp.plot_decision_regions(X_combined_std, y_combined,classifier=kmeans, test_idx=range(105,150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')


plt.figure(3)
kmeans2 = KMeans(n_clusters = 3, random_state= 0)
kmeans2.fit(X_train_std)
# loss2 = loss_function(X_test_std, kmeans2)
# print(loss2)
pp.plot_decision_regions(X_combined_std, y_combined,classifier=kmeans2, test_idx=range(105,150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')


plt.figure(4)

kmeans_test = KMeans(n_clusters = 5, random_state= 0)
kmeans_test.fit(X_train_std)
loss_test = loss_function(X_test_std,kmeans_test)
print(loss_test)
print (kmeans_test.cluster_centers_ )
print (kmeans_test.fit_predict(X_test_std))
pp.plot_decision_regions(X_combined_std, y_combined,classifier=kmeans_test, test_idx=range(105,150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.show()
