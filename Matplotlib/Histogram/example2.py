import matplotlib.pyplot as plt
B=[10,20,30,21,9]
G=[11,23,10,9,6]
O=[11,2,3,20,15]

plt.hist([B,G,O],bins=[0,10,20,30],rwidth=0.9,orientation='vertical',
         color=['r','k','g'],label=['Boys','Girls','Olds'],
         histtype='barstacked',edgecolor='k')
plt.xlabel('Range')
plt.ylabel('Ratio')
plt.legend()
plt.show()
