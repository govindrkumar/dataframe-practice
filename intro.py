import numpy as np
import pandas as pd

#to create a blank dataframe 
print('Blank Dataframe : ')
df1 = pd.DataFrame()
print(df1)

#creating dataframe with dictionary having list and ndarray
dict2 = {
    'Name' : ['Govind','Sanjeev','Roshni'],
    'Class' : [12, 12, 12],
    'Marks' : [99,67,53]
}
df2 = pd.DataFrame(dict2, index=[1,2,3])
print(df2)

#dictionary contains dictionary 
dict3 = {
    'Sales' : {
        'name' : 'Govind',
        'age' : 16,
        'sex' : 'Male'
    },
    'Prostitution' : {
        'name' : 'Roshni',
        'age' : 17,
        'sex' : 'Daily'

    }
}
df3 = pd.DataFrame(dict3)
print(df3)

