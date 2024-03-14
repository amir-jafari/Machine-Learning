import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix
# -------------------------------------------------------------------------------------------------------
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

irisdata = pd.read_csv(url, names=names)
print(irisdata.head())

X = irisdata.iloc[:, 0:4]
y = irisdata.select_dtypes(include=[object])
print(y.Class.unique())
# -------------------------------------------------------------------------------------------------------
le = preprocessing.LabelEncoder()
y = y.apply(le.fit_transform)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
# -------------------------------------------------------------------------------------------------------

mlp = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=1000)
mlp.fit(X_train, y_train.values.ravel())

predictions = mlp.predict(X_test)

print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))