import matplotlib.pyplot as plt

# Step 1: Data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2.1, 4.3, 5.9, 8.2, 10.1, 12.3, 13.8, 16.1, 17.9, 20.2]

# Step 2: Scatter plot
plt.scatter(x, y, color='blue', label='Data Points', s=50)

# Step 3: Trend line (linear)
m, b = 2, 0.1  # slope and intercept (pretend you calculated it)
y_trend = [m*i + b for i in x]
plt.plot(x, y_trend, color='red', linestyle='--', label='Trend Line')

# Step 4: Labels, title, grid, legend
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot with Trend Line")
plt.legend()
plt.grid(True)

# Step 5: Show
plt.show()
