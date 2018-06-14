# import data
from sklearn import datasets
import numpy as np
iris = datasets.load_iris()
X = iris.data[:, [2,3]]
y = iris.target
#-----------------------------------------------------------------------------
# data pre processing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
X_combined_std = np.vstack((X_train_std, X_test_std))
y_combined = np.hstack((y_train, y_test))
#-----------------------------------------------------------------------------

from sklearn.linear_model import LogisticRegression
import plot_decision_regions as pp
import matplotlib.pyplot as plt


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1, p=2,metric='minkowski')
knn.fit(X_train_std, y_train)
pp.plot_decision_regions(X_combined_std, y_combined,classifier=knn, test_idx=range(105,150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.show()

# print(knn.score(X_test_std,y_test))

from sklearn.neighbors import NearestNeighbors
knn2 = NearestNeighbors(n_neighbors=3)
knn2.fit(X_train_std)
#print sum(sum((knn2.kneighbors(X_train_std)[0])))
print knn2.kneighbors(X_train_std)[0]
'''
def loss_function(x,k):
    sum_distance = sum(sum(k.kneighbors(X_test_std)[0]))
    return sum_distance

loss_array =[]
for i in xrange(1,6):
    knn2 = NearestNeighbors(n_neighbors=i)
    knn2.fit(X_train_std)
    loss_array.append(loss_function(X_test_std,knn2))

plt.figure(1)
plt.scatter([1,2,3,4,5], loss_array)
plt.show()
'''