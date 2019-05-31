from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()
X = iris.data
y = iris.target

model = RandomForestClassifier()
model.fit(X,y)

newX = selectKImportance(model,X,2)