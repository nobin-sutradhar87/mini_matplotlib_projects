import matplotlib
# Only force backend if your default is broken (optional)
 matplotlib.use('TkAgg')   # or 'Qt5Agg'

import matplotlib.pyplot as plt

# Data
num = [1, 2, 3, 4, 5]
num_squares = [n**2 for n in num]  # cleaner than hardcoding

# Create figure + axes
fig, ax = plt.subplots()

# Plot
ax.plot(num, num_squares, linewidth=2)

# Titles and labels
ax.set_title("Square Numbers", fontsize=18)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squared Value", fontsize=14)

# Ticks
ax.tick_params(axis='both', labelsize=12)

# Show
plt.show()
