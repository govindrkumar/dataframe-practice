import pandas as pd
s1 = pd.Series(
    10, index = range(0,1)
)

s2 = pd.Series(
    'Yet to Start', index = ['Delhi','Aagra','Mumbai']
)
print(s1)
print(s2)
