# Decision Tree

* Lctures code

* Sample Example and Exercise


## Guide

* Graph viz (Ubuntu Installation)

You need to install the pydotplus package to be able to see the graph.

```
sudo pip install pydotplus
```

* Graph viz (Windows Installation)

Firs, you need to install the pydotplus package

```
pip install pydotplus
```

```
pip install pydot
```

```
pip install graphvis
```

Second you need to download the msi file and:

Install [graphvis](https://graphviz.gitlab.io/_pages/Download/Download_windows.html)

The add the following command in your python code.

```
import os     
```

then 

```
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
```

