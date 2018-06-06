import pydotplus
from sklearn.datasets import load_iris
from sklearn import tree
import collections

import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

# Data Collection
X = [[180, 15, 0],
     [177, 42, 0],
     [136, 35, 1],
     [174, 65, 0],
     [141, 28, 1]]

Y = ['man', 'woman', 'woman', 'man', 'woman']

data_feature_names = ['height', 'hair length', 'voice pitch']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

# Visualize data
dot_data = tree.export_graphviz(clf,
                                feature_names=data_feature_names,
                                out_file=None,
                                filled=True,
                                rounded=True)
graph = pydotplus.graph_from_dot_data(dot_data)

colors = ('turquoise', 'orange')
edges = collections.defaultdict(list)

for edge in graph.get_edge_list():
    edges[edge.get_source()].append(int(edge.get_destination()))

for edge in edges:
    edges[edge].sort()
    for i in range(2):
        dest = graph.get_node(str(edges[edge][i]))[0]
        dest.set_fillcolor(colors[i])

graph.write_png('tree.png')
graph.write_svg('tree.svg')

