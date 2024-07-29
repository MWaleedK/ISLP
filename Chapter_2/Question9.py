import os, sys
import pandas as pd


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DatasetGrabber.helper import DatasetGrabber

autoPath = DatasetGrabber()
auto = pd.read_csv(autoPath.getDatasetFilePath('Auto.csv'))
auto2 = auto.loc[:, auto.columns!='name']


for head in auto2.head(0):
    print(f'{head}: {auto2[head].min(axis=0)}, {auto2[head].min(axis=0)}')