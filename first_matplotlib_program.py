import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg', depending on your system
import matplotlib.pyplot as plt

num = [1, 2, 3, 4, 5]
num_squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(num, num_squares)
plt.show()
