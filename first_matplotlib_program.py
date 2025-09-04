import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg', depending on your system
import matplotlib.pyplot as plt

num = [1, 2, 3, 4, 5]
num_squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(num, num_squares, linewidth=3)
ax.set_title("square number", fontsize=24)

ax.set_xlabel("values", fontsize=24)
ax.set_ylabel("squared number",fontsize=24)

ax.tick_params(axis='both', labelsize=14)
plt.show()
