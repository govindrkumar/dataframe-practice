import pandas as pd
ob1 = pd.Series([39,41,42,44])

ob1[1] = 1.85
print(ob1)
ob1[1:3] = 2.56
print(ob1)

ob1.index = ['A','B','C','D']
print(ob1.index)

#head and tail function
print(ob1.head(2))
print(ob1.tail(1))

#vector operations on series object
ob2 = pd.Series([1.50,12.75,24.00,35.25,46.50], index = ['a','b','c','d','e'])
print(ob2 + 2)
print(ob2*3)

print(ob2>15)
print(ob2**2)