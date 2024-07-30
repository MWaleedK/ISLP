import os, sys
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DatasetGrabber.helper import DatasetGrabber

autoPath = DatasetGrabber()
auto = pd.read_csv(autoPath.getDatasetFilePath('Auto.csv'))
auto2 = auto.loc[:, auto.columns!='name']


print(auto.describe().loc[['min', 'max'],:])

print(auto.describe().loc[['mean', 'std'],:])

auto3 = auto.drop(index=range(10,85))

print(auto3.describe().loc[['min', 'max'],:])

print(auto3.describe().loc[['mean', 'std'],:])

pd.plotting.scatter_matrix(auto)
saveBase = os.path.join(os.getcwd(), 'Chapter_2')
saveData = os.path.join(saveBase, "AutoScattermatrix9.png")
plt.savefig(saveData)
plt.clf()


X = auto['mpg']

fig, axs = plt.subplots(2, 2, figsize=(12, 8), sharex=True)
# Plot data in each subplot
axs[0, 0].scatter(X, auto['cylinders'], color='red')
axs[0, 0].set_title('Plot Y')
axs[0, 0].set_ylabel('cylinders')
axs[0, 0].set_xlabel('mpg')

axs[0, 1].scatter(X, auto['displacement'], color='green')
axs[0, 1].set_title('Plot Z')
axs[0, 1].set_ylabel('displacement')
axs[0, 1].set_xlabel('mpg')

axs[1, 0].scatter(X, auto['weight'], color='black')
axs[1, 0].set_title('Plot K')
axs[1, 0].set_ylabel('weight')
axs[1, 0].set_xlabel('mpg')

axs[1, 1].scatter(X, auto['year'], color='pink')
axs[1, 1].set_title('Plot L')
axs[1, 1].set_ylabel('year')
axs[1, 1].set_xlabel('mpg')

saveData = os.path.join(saveBase, "subplots9.png")
plt.savefig(saveData)
plt.clf()

