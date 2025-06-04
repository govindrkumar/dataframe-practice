import matplotlib.pyplot as plt

# Data
labels = ['Python', 'Java', 'C++', 'Ruby']
sizes = [40, 30, 20, 10]
colors = ['gold', 'skyblue', 'lightgreen', 'pink']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, colors=colors, explode=explode, 
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.title('Programming Language Usage')
plt.show()
