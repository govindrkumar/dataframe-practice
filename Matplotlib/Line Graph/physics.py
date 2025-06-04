import matplotlib.pyplot as plt

x = ['Kinematics', 'NLM', 'WEP', 'COM', 
     'Rotatioanl Motion', 'Gravitation', 'Elasticity',
     'Fluid', 'Thermal Property', 
     'KTG & ThermoD', 'Oscillation', 'Waves']

y = [32, 18, 13, 10, 14, 7, 4, 10, 12, 8, 9, 10]

plt.plot(x, y, linewidth=3.5, linestyle='--', marker='p')
plt.title('Physics Syllabus')
plt.xlabel('Chapters')  # Fixed typo
plt.ylabel('Lecture Count')
plt.xticks(rotation=45)  # Optional: makes x-labels easier to read
plt.tight_layout()       # Optional: adjusts layout so labels fit
plt.show()
