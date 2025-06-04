import matplotlib.pyplot as plt
IP = [10,23,10,50]
Eng = [8,19,15, 45]
Sci = [9,42,33,23]
Math = [3,50,29,39]
x = ['IP','Eng','Science','Math']
plt.plot(x,IP,color='b',label='IP',linewidth=3,linestyle='--',marker='d')
plt.plot(x,Eng,color='m',label='English',linestyle='dashdot',marker='p',markeredgecolor='red')
plt.plot(x,Sci,color='c',label='Science',linestyle='dotted')
plt.plot(x,Math,'r8:',label='Math',linestyle='solid')
plt.xlabel('Subject')
plt.ylabel('Marks')
plt.legend(loc='upper left')
plt.title('Student Mark distributions')
plt.savefig(r"") #to save graph
plt.show()