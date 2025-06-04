import pandas as pd
import numpy as np

staff = pd.Series([10,20,30])
salaries = pd.Series([16600,25000,45333])

employee = {
    'Empcode' : staff,
    'Empsal' : salaries
}

df = pd.DataFrame(employee)
print(df)

print(df.index)
print(df.columns,df.axes,df.dtypes,df.size,df.shape,df.ndim,df.empty)