import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'



balance_data = pd.read_csv(
'https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.data',
                           sep= ',', header= None)



print("Dataset Lenght:: ", len(balance_data))
print ("Dataset Shape:: ", balance_data.shape)



X = balance_data.values[:, 1:5]
Y = balance_data.values[:,0]



X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)



clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100,
                               max_depth=3, min_samples_leaf=5)
clf_gini.fit(X_train, y_train)



DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=3,
            max_features=None, max_leaf_nodes=None, min_samples_leaf=5,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            presort=False, random_state=100, splitter='best')

clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
 max_depth=3, min_samples_leaf=5)
clf_entropy.fit(X_train, y_train)


print (clf_gini.predict([[4, 4, 3, 3]]))

y_pred = clf_gini.predict(X_test)
print( y_pred)




y_pred_en = clf_entropy.predict(X_test)
print( y_pred_en)

print( "Accuracy is ", accuracy_score(y_test, y_pred) * 100)


print ("Accuracy is ", accuracy_score(y_test,y_pred_en)*100)

tree.export_graphviz(clf_gini,  out_file='tree.dot')

# http://webgraphviz.com/

