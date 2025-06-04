import pandas as pd
import matplotlib.pyplot as plt

Df = pd.read_csv(r'/home/govind/Desktop/My Files.csv')

Df.plot(kind='barh',x='Day',color=['red','black','pink'],align='edge')
#Df.plot(kind='bar',x='Day',color=['red','black','pink'],width=1)

plt.title("Sales for May 2025")
plt.show()


#yaha par height use hoga, bar mei width hoga. thik hai for thickness