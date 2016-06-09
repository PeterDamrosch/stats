import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Load data on loans
loans = pd.read_csv('loansData.csv')

# Helper functions for cleaning data
def clean_interest(rate):
	just_numbers = rate.rstrip('%')
	percent_as_decimal = float(just_numbers)/100
	return round(percent_as_decimal, 4)

# Clean Interest.Rate and create Annual.Income column	 
loans['Interest.Rate'] = loans['Interest.Rate'].map(clean_interest)
loans['Annual.Income'] = loans['Monthly.Income'] * 12

# Pull out relevant series for interest rate model
interest_rate = loans['Interest.Rate']
annual_income = loans['Annual.Income']

# Transform series into columns for matrix
y = np.matrix(interest_rate).transpose()
x1 = np.matrix(annual_income).transpose()

# Add a column of 1's for the model
X = sm.add_constant(x1)

# Create OLS model and get a summary of how well it fits
est = sm.OLS(y,X).fit()
print est.summary()