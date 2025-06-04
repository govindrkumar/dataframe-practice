import matplotlib.pyplot as plt
balls = [12, 9, 18, 40, 29, 27, 15, 45]
plt.hist(balls, bins=[0,20,30,40,50],rwidth=0.6)
plt.show()