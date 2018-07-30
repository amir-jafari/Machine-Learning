#%%==================================================================================
import pandas as pd
from sklearn import tree

#%%-----------------------------------------------------------------------
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
#%%-----------------------------------------------------------------------

# Libraries to display decision tree
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz
import webbrowser
#==================================================================================
#%%
#Set up all our data in a couple of data frames.
customers = pd.DataFrame()
customers['purchases_amount'] = [105, 65, 89, 99, 149, 102, 34, 120, 129, 39,
                                 20, 30, 109, 40, 55, 100, 23, 20, 70, 10]

customers['purchases_items'] = [1, 4, 5, 4, 7, 1, 2, 10, 6, 5,
                                1, 3, 2, 1, 5, 10, 3, 3, 1, 1]

customers['promo'] = [1, 1, 0, 1, 0, 0, 0, 0, 0, 1,
                      1, 1, 1, 0, 1, 1, 1, 0, 1, 1]

customers['email_list'] = [1, 0, 1, 1, 1, 0, 1, 1, 1, 1,
                           0, 1, 1, 0, 1, 0, 1, 1, 0, 0]

customers['checkouts'] = [1, 5, 3, 3, 1, 2, 4, 4, 1, 1,
                          1, 1, 2, 4, 1, 1, 2, 1, 1, 1]

repeat_customers = pd.DataFrame()

repeat_customers['repeat'] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
customers.head()
repeat_customers.head()
customers.info()
repeat_customers.info()
#%%==================================================================================
# Need to install graphviz and pydotplus
# To install pydotplus use !pip install pydotplus in the console, let's you use the console vice a command window
# Alternatively you can also use the anaconda command prompt
# from IPython.display import Image
# The package above makes things easier to visualize 
# Below we are calling the packages we just installed
#%%==================================================================================

# Initialize and train our tree.
clf_1 = tree.DecisionTreeClassifier(criterion='entropy', max_features=1, max_depth=2, random_state = 1000)

clf_1.fit(customers, repeat_customers)
l = customers.columns
#%%==================================================================================

dot_data = export_graphviz(clf_1, filled=True, rounded=True, feature_names=list(l), out_file=None)

graph = graph_from_dot_data(dot_data)
graph.write_pdf("Tennis.pdf")
webbrowser.open_new(r'Tennis.pdf')