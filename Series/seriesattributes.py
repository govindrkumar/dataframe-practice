import pandas as pd
import numpy as np

ser1 = pd.Series([1,2,3], index = [0,1,2])
print(ser1.index)

ser1.index.name = 'Govind'
print(ser1)

ser1.name = 'Bakwas'
print(ser1)