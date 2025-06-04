#isme range ki baat hoti hai, wo bhi defined range.
import pandas as pd
import matplotlib.pyplot as plt
Marks = [40,60,55,20,35,70,60,89,20,33]
plt.hist(Marks,bins=[0,33,50,70,100],rwidth=0.9)
plt.show()