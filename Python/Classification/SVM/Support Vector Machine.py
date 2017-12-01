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

#-----------------------------------------------------------------------------

# Liner SVM
plt.figure(1)
from sklearn.svm import SVC
svm = SVC(kernel='linear', C=1.0, random_state=0)
svm.fit(X_train_std, y_train)

pp.plot_decision_regions(X_combined_std,y_combined, classifier=svm,test_idx=range(105,150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')






#Non-liner SVM
plt.figure(2)
svm2 = SVC(kernel='rbf', random_state=0, gamma=0.2, C=1.0)
svm2.fit(X_train_std, y_train)
pp.plot_decision_regions(X_combined_std,y_combined, classifier=svm2,test_idx=range(105,150))
plt.xlabel('petal length [standardized]')
plt.ylabel('petal width [standardized]')
plt.legend(loc='upper left')
plt.show()