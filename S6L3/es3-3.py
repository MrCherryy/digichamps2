import pandas as pd

file_path = "~/AI/datasets/wine/wine.data"

iris_data = pd.read_csv(file_path, delimiter=",")

'''
df = pd.read_json("iris.data")

df = pd.read_csv("wine.csv")

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

df = pd.read_csv(url, names=column_names)
print(df.head())
print(df.tail())
print(df.describe())'''