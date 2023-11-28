import matplotlib.pyplot as plt
import numpy as np
months = np.arange(1, 13)
temperature_data = [25, 28, 30, 32, 35, 36, 34, 32, 30, 28, 26, 24]
rainfall_data = [50, 40, 30, 20, 10, 5, 8, 15, 25, 35, 45, 55]
plt.figure(figsize=(8, 5))
plt.plot(months, temperature_data, marker='o', linestyle='-', color='red')
plt.title('Monthly Temperature Data (Line Plot)')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()
plt.figure(figsize=(8, 5))
plt.scatter(months, rainfall_data, color='blue')
plt.title('Monthly Rainfall Data (Scatter Plot)')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.show()
