import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

# Load data on loans
loans = pd.read_csv('loansData.csv')

# Helper functions for cleaning data
def clean_interest(rate):
	just_numbers = rate.rstrip('%')
	percent_as_decimal = float(just_numbers)/100
	return round(percent_as_decimal, 4)

# Clean Interest.Rate and create Annual.Income column	 
loans['RateClean'] = loans['Interest.Rate'].map(clean_interest)
loans['AnnualIncome'] = loans['Monthly.Income'] * 12

# Visualize the relationship
loans.plot(kind='scatter', x='AnnualIncome', y='RateClean')

# Linear regression model
#lin_model = smf.ols(formula='RateClean ~ AnnualIncome', data=loans).fit()
#print lin_model.summary()
# I'm getting an R-Squared of 0.000. AnnualIncome coeff of < 0.000001. That seems odd.

# Multiple regression model
mult_lin_model = smf.ols(formula='RateClean ~ AnnualIncome + Ownership', data=loans).fit()
# Definitely something going on, I'm getting R2 of 0.008


# Pull out relevant series for interest rate model
#interest_rate = loans['Interest.Rate']
#annual_income = loans['Annual.Income']

# Transform series into columns for matrix
#y = np.matrix(interest_rate).transpose()
#x1 = np.matrix(annual_income).transpose()

# Add a column of 1's for the model
#X = sm.add_constant(x1)

# Create OLS model and get a summary of how well it fits
#est = sm.OLS(y,X).fit()
#print est.summary()