import pandas as pd
import matplotlib.pyplot as plt

Df = pd.read_csv(r'/home/govind/Desktop/My Files.csv')

Df.plot(kind='bar',x='Day',color=['red','black','pink'],align='edge')
#Df.plot(kind='bar',x='Day',color=['red','black','pink'],width=1)

plt.title("Sales for May 2025")
plt.show()

#bar mei x and y value dono required hai, line chart mei wo khud se v create kar lega

#df mei main y-axis v plot kar sakta hu. 
