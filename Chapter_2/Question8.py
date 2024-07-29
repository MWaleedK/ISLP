import pandas as pd
import sys, os
import matplotlib.pyplot as plt
import copy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DatasetGrabber.helper import DatasetGrabber

# Tasks
# a) Load Data

dbg = DatasetGrabber()

college = pd.read_csv(dbg.getDatasetFilePath("College.csv"))
college2 = pd.read_csv(dbg.getDatasetFilePath("College.csv"), index_col=0)

college3 = college.rename({'Unnamed: 0': 'College'}, axis=1)
college3 = college3.set_index('College')

college = college3

reduced_dataframe = college.loc[:, ['Top10perc', 'Apps', 'Enroll']]

value = pd.plotting.scatter_matrix(reduced_dataframe)
saveBase = os.path.join(os.getcwd(), 'Chapter_2')
saveData = os.path.join(saveBase, "CollegeScattermatrix.png")
plt.savefig(saveData)
plt.clf()


# Boxplot of 'Outstate' by 'Private'
college.boxplot(column='Outstate', by='Private')
saveData = os.path.join(saveBase, "BoxPlot.png")
plt.savefig(saveData)
plt.clf()

college['Elite'] = pd.cut(college['Top10perc']/100, bins=[0,0.5,1], labels=['No', 'Yes'])

eliteColleges = college['Elite']

college.boxplot(column = 'Outstate', by= 'Elite')
saveData = os.path.join(saveBase, "EliteOutstates.png")
plt.savefig(saveData)
plt.clf()

f, ((ax1,ax2), (ax3,ax4)) = plt.subplots(2,2,figsize=(10,10))
college.hist(column='Apps',ax=ax1)
college.hist(column='Accept',ax=ax2)
college.hist(column='Enroll',ax=ax3)
college.hist(column='Top10perc',ax=ax4)

saveData = os.path.join(saveBase, "subplots.png")
plt.savefig(saveData)
plt.clf()
