import pandas as pd

data = {
    'Name': ['Ananya', 'Bhavesh', 'Chirag', 'Divya', 'Esha'],
    'Physics': [87, 76, 91, 66, 93],
    'Chemistry': [78, 89, 84, 90, 88],
    'Biology': [85, 81, 79, 95, 77]
}

df = pd.DataFrame(data, index=['S1', 'S2', 'S3', 'S4', 'S5'])
print(df)

print(df.loc['S3',['Name']])
print(df.loc[['S1','S5'],'Biology'])
print(df.loc[['S2','S3','S4'],['Name','Physics']])
print(df.loc['S4',['Physics','Chemistry','Biology']])

print(df.iloc[2,:])
print(df.iloc[[0,-1],2])
print(df.iloc[1:-1,[0,3]])
print(df.iloc[:2,[1,2]])