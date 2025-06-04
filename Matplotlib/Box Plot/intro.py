import matplotlib.pyplot as plt
import numpy as np

# Random data
math_marks = [88, 92, 85, 78, 90, 95, 91, 89, 84, 86]

# Plot
plt.boxplot(math_marks)
plt.title("Math Marks Box Plot")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
