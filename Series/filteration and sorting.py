import pandas as pd
s1 = pd.Series([1,2,3,4,5,6])

print("Vales greater than 2 : ")
print(s1[s1>2])

s1.sort_values(ascending = True)
s1.sort_values(descending = True)
