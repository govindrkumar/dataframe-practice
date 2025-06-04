import pandas as pd
import numpy as np

#creating a empty series
bt = pd.Series()
print(bt)

#create a sries using different words:
s5 = pd.Series(['I','am','Batman'],index=[1,2,3])
print(s5)

#specify data as ndarray
ser1 = pd.Series(np.arange(3,15,3.5))
print(ser1)

#create a series which has ndarray and 5 element 
s6 = pd.Series(np.linspace(24,64,5))
print(s6)

#create a tile a list [3,5], twice
s7 = pd.Series(np.tile([3,5],2), index=[1,2,3,4])
print(s7)
