import matplotlib.pyplot as plt
import numpy as np

subjects = ['Physics','Chemistry','Biology']
student_A = [88, 76, 92, 85, 90]
student_B = [82, 79, 85, 87, 94]

x = np.arange(len(subjects))  # [0, 1, 2, 3, 4]
width = 0.35  # width of the bars

plt.bar(x - width/2, student_A, width, label='Student A')
plt.bar(x + width/2, student_B, width, label='Student B')

plt.xticks(x, subjects)
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title('Marks Comparison')
plt.legend()

plt.show()
