import os, sys
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DatasetGrabber.helper import DatasetGrabber

bostonPath = DatasetGrabber()
boston = pd.read_csv(bostonPath.getDatasetFilePath('Boston.csv'))

print(f'rows: {len(boston)}, columns: {len(boston.columns)}')


saveBase = os.path.join(os.getcwd(), 'Chapter_2')
saveData = os.path.join(saveBase, "AutoScattermatrix9.png")

fig, axs = plt.subplots(4, 2, figsize=(8, 8), sharex=True)
# Plot data in each subplot
axs[0, 0].scatter(boston['age'], boston['crim'], color='red')
axs[0, 0].set_title('Plot Y')
axs[0, 0].set_ylabel('proportion of owner occupied dwelling')
axs[0, 0].set_xlabel('crime')

axs[0, 1].scatter(boston['tax'], boston['crim'], color='green')
axs[0, 1].set_title('Plot Z')
axs[0, 1].set_ylabel('tax')
axs[0, 1].set_xlabel('crime')

axs[1, 0].scatter(boston['medv'], boston['crim'], color='black')
axs[1, 0].set_title('Plot K')
axs[1, 0].set_ylabel('median of owner occupied dwelling')
axs[1, 0].set_xlabel('crime')

axs[1, 1].scatter(boston['dis'], boston['crim'], color='pink')
axs[1, 1].set_title('Plot L')
axs[1, 1].set_ylabel('distance to employment center')
axs[1, 1].set_xlabel('crime')

axs[2, 0].scatter(boston['rad'], boston['crim'], color='blue')
axs[2, 0].set_title('Plot L')
axs[2, 0].set_ylabel('index of accessibe radical highways')
axs[2, 0].set_xlabel('crime')

axs[2, 1].scatter(boston['lstat'], boston['crim'], color='purple')
axs[2, 1].set_title('Plot L')
axs[2, 1].set_ylabel('lower status of population')
axs[2, 1].set_xlabel('crime')


saveData = os.path.join(saveBase, "subplots10.png")
plt.savefig(saveData)
plt.clf()

# Yes tax is highly associate dwith per capita crimerate, increased tax = increased crimerate

print(boston.iloc[boston['crim'].nlargest(10).index])

print(boston.iloc[boston['tax'].nlargest(10).index])

print(boston.iloc[boston['ptratio'].nlargest(10).index])

figs, plots = plt.subplots(1,2, figsize=(4,4), sharex=True)

plots[0].scatter(boston.iloc[boston['crim'].nlargest(10).index]['ptratio'], boston.iloc[boston['crim'].nlargest(10).index]['crim'])
plots[0].set_title('plot A top10 crime suburbs')
plots[0].set_ylabel('pupil to Student ratio')
plots[0].set_xlabel('crime')

plots[1].scatter(boston.iloc[boston['crim'].nlargest(10).index]['tax'], boston.iloc[boston['crim'].nlargest(10).index]['crim'])
plots[1].set_title('plot B top10 crime suburbs')
plots[1].set_ylabel('tax rates')
plots[1].set_xlabel('crime')

saveData = os.path.join(saveBase, "twosubplots10.png")
plt.savefig(saveData)
plt.clf()



print(boston['chas'].value_counts()[1])

print(boston['ptratio'].median())

print(boston['medv'].argmin())

sevenrooms = boston[boston['rm'] > 7]
eightrooms = boston[boston['rm'] > 8]

print(len(sevenrooms))
print(len(eightrooms))

print(sevenrooms.describe())
print(eightrooms.describe())

