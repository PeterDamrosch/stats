import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Find linear regreesion coefficients - inputs are pandas series
def linear_regression(x, y):
	# Define constants so don't have to recalculate
	mean_y, mean_x = y.mean(), x.mean()
	std_y, std_x = y.std(), x.std()

	# Pearson's R calculations using Z-scores
	correlation_sum = 0
	for i in range(len(y)):
		z_y = (y[i] - mean_y) / std_y
		z_x = (x[i] - mean_x) / std_x
		correlation_sum += z_y * z_x

	r = correlation_sum / (len(y) - 1)
	
	# Regression coefficient
	weight = r * (std_y / std_x)

	# Intercept
	intercept = mean_y - weight * mean_x

	# Return as dictionary
	return {'weight': weight, 'intercept': intercept}

# Test out linear_regression algorithm using cricket chirps vs. temp data
df = pd.read_csv('cricketsData.csv')
temp = df['TEMPERATURE']
chirp = df['CHIRPRATE']
coeff = linear_regression(temp, chirp)

# Plot the regression line and scatter plot
x1 = 60
y1 = 60 * coeff['weight'] + coeff['intercept']
x2 = 100
y2 = 100 * coeff['weight'] + coeff['intercept']
plt.scatter(temp, chirp)
plt.plot([x1,x2],[y1,y2])
