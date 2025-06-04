#isme range ki baat hoti hai, wo bhi defined range.
import pandas as pd
import matplotlib.pyplot as plt
Marks = [40,60,55,20,35,70,60,89,20,33]
plt.hist(Marks,bins=10,rwidth=0.9,cumulative=False,histtype="barstacked",orientation='vertical')
plt.show()


#agar bin nhi dala tab wo khud se kar lega, default = 10 bins
#cumulative piche wali values ko v add karta hai. 