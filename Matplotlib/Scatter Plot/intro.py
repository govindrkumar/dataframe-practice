import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5, 6, 7]
y = [2, 4, 5, 7, 6, 8, 9]

# Plot
plt.scatter(x, y, color='red', marker='o')
plt.title('Simple Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.show()
