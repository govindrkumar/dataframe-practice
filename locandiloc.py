import pandas as pd

data = {
    'Player': ['Rohit', 'Virat', 'Gill', 'Surya', 'Hardik'],
    'Runs': [102, 87, 99, 45, 76],
    'Balls': [98, 91, 85, 60, 55],
    'StrikeRate': [104.1, 95.6, 116.4, 75.0, 138.1]
}

df = pd.DataFrame(data, index=['M1', 'M2', 'M3', 'M4', 'M5'])
print(df)

print(df.loc[['M2'],'Player'])
print(df.loc[['M1','M3'],'StrikeRate'])
print(df.loc[:,['Player','Runs']])

print(df.iloc[3])
print(df.iloc[[0,-1],2])
print(df.iloc[1:5,[0,3]])

print(df.loc[['M2'],'StrikeRate'])
print(df.iloc[4,[0,2]])