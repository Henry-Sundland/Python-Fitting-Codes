import numpy as np
import matplotlib.pyplot as plt


# generating fake data to test power fit (you would just use your own x, y and dy values)
# Parameters for the power law y = a * x^b
a_true = 2.0
b_true = 1.5
# Generate synthetic data
np.random.seed(42)
x = np.linspace(1, 10, 20)
y_true = a_true * x**b_true
# Adding noise to the data (uncertainty)
dy = np.abs(0.2 * y_true * np.random.normal(size=x.size))  # 20% noise, ensuring positive uncertainties
y = y_true + dy


# linearizing data
Y = np.log(y)
X = np.log(x)
Y_uncertainty = (dy)/(y)
weights = 1/Y_uncertainty**2

# then follows least linear weighted squares method
# For solving normal equations
weight_sum = np.sum(weights)
S_x = np.sum(weights*X)
S_xx = np.sum(weights*(X**2))
S_xy = np.sum(weights*X*Y)
S_y = np.sum(weights*Y)

# Finding cool fit parameters
delta = S_xx*weight_sum - (S_x**2)
A = (weight_sum*S_xy - S_x*S_y)/delta
B = (S_xx*S_y - S_x*S_xy)/delta
A_uncertainty = np.sqrt(weight_sum/delta)
B_uncertainty = np.sqrt(S_xx/delta)

# Convert back to original space
a_fit = np.exp(B)
b_fit = A

# Recalculate the fit in original space
y_fit = a_fit * x**b_fit

# Calculate residuals and chi-squared
residuals = Y - (A * X + B)
chi_squared = np.sum(weights * residuals**2)

print("Chi^2 value is: ", chi_squared)
print("A (slope) is: ", A, "+/-", A_uncertainty)
print("B (intercept) is: ", B, "+/-", B_uncertainty)
print("a (coefficient) is: ", a_fit)
print("b (exponent) is: ", b_fit)

# Plotting the fit function
plt.errorbar(x, y, yerr=dy, fmt='o', label='Data with uncertainties', color='blue', ecolor='gray', capsize=5)
plt.plot(x, y_fit, label=f'Fit: y = {a_fit:.2f} * x^{b_fit:.2f}', color='red')

# Add axis labels
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Add a title
plt.title('Graph of Power-Law Fit')

# Add a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
