import pandas as pd
import numpy as np

#creating value as NaN
s1 = pd.Series([6.5,np.nan,34])
print(s1)

#specificy index as well as data
arr = ['Govind','Sanjeev','Roshni','Kaushal']
mon = [1,2,3,4]
s2 = pd.Series(data = arr, index = mon)
print(s2)

#using loop and data type
s3 = pd.Series(range(10,20,2), index=[x for x in 'abcde'], dtype = float)
print(s3)

#using math
a = np.arange(9,13) #supports vector operation
s4 = pd.Series(index = a, data = a **2 )
s5 = pd.Series(index = a*2, data = a*2)
print(s4)
print(s5)

#but see
Lst = [1,2,3,4]
s6 = pd.Series(index = [1,2,3,4,5,6,7,8], data = Lst*2)
print(s6) #you got repition only cause only numpy god support vector operation