import numpy as np
import matplotlib.pyplot as plt

# making up data and uncertainties to test plot and show code off
x = np.linspace(0,10,10)
y = np.linspace(0,10,10)
dy = np.linspace(0.1, 10, 10)

weights = 1/(dy**2)

# For solving normal equations
weight_sum = np.sum(weights)
S_x = np.sum(weights*x)
S_xx = np.sum(weights*(x**2))
S_xy = np.sum(weights*x*y)
S_y = np.sum(weights*y)

# Finding cool fit parameters
delta = S_xx*weight_sum - (S_x**2)
A = (weight_sum*S_xy - S_x*S_y)/delta
B = (S_xx*S_y - S_x*S_xy)/delta
A_uncertainty = np.sqrt(weight_sum/delta)
B_uncertainty = np.sqrt(S_xx/delta)
residuals = y - (A * x + B)
chi_squared = np.sum(weights*(residuals)**2)
print("residuals: ", residuals)
print("Chi^2 value is: ", chi_squared)

print("Slope : ", A, "+/-", A_uncertainty)
print("Y-intercept : ", B, "+/-", B_uncertainty)


# Plotting the fitted line
y_fit = A * x + B
#plt.scatter(x, y, label='testing', color='blue')
plt.errorbar(x, y, yerr=dy, fmt='o', label='Data with uncertainties', color='blue', ecolor='gray', capsize=5)
plt.plot(x, y_fit, label=f'Fit: y = {A:.2f}x + {B:.2f}', color='red')

# Add axis labels
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Add a title
plt.title('Graph of Linear Fit')

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)


plt.show()
