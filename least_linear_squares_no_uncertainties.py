<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np

#let's generate data for the fit
x = np.linspace(0,10,10)
y = np.linspace(0,10,10)

#plotting this data
plt.scatter(x,y, label = "testing", color = 'blue')

# Add axis labels
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Add a title
plt.title('Graph of test')

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()


# ok, now to fit to this data set using linear least squares regression method......
x_sum = sum(x)
y_sum = sum(y)
x_squared_sum = sum(x**2)
x_y_sum = sum(x*y)
N = len(x)

slope = (N*x_y_sum - x_sum*y_sum)/(N*x_squared_sum -(x_sum)**2)
y_intercept = (y_sum - slope*x_sum)/(N)

print("Slope:", slope)
print("Y-Intercept:", y_intercept)

# Plotting the fitted line
y_fit = slope * x + y_intercept
plt.scatter(x, y, label='testing', color='blue')
plt.plot(x, y_fit, label=f'Fit: y = {slope:.2f}x + {y_intercept:.2f}', color='red')

# Add axis labels
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Add a title
plt.title('Graph of Linear Fit')

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)
