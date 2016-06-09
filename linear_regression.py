import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import numpy as np
import statsmodels.api as sm
import collections

# Load data on loans
loans = pd.read_csv("https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv")

# Helper functions for cleaning data
def clean_interest(rate):
	rate = round(float(rate.rstrip('%'))/100, 4)
	return rate

def clean_length(length):
	length = length.rstrip(' months')
	return int(length)

def split_fico(score):
	score = score.split('-')
	return int(score[0])

# Clean Interest.Rate and Loan.Length columns
loans['Interest.Rate'] = loans['Interest.Rate'].map(clean_interest)
loans['Loan.Length'] = loans['Loan.Length'].map(clean_length)

# Create FICO.Score column
loans['FICO.Score'] = loans['FICO.Range'].map(split_fico)

# For future reference: can just use list comprehensions, e.g.:
# loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]

# Plot histogram of FICO.Score
plt.figure()
p = loans['FICO.Score'].hist()

# Create a scattermatrix - good for getting an overview of all variables against all variables
a = pd.scatter_matrix(loans, alpha=0.05, figsize=(10,10), diagonal='hist')

# Pull out relevant series from df for interest rate model
intrate = loans['Interest.Rate']
loanamt = loans['Amount.Requested']
fico = loans['FICO.Score']

# Transform series into columns for matrix
# np.matrix will make matrix rows so need to transpose
y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

# Combine the two independent columns
x = np.column_stack([x1, x2])

# Add a column of 1's, not exactly sure why
X = sm.add_constant(x)

# Create OLS model and get a summary of how well the model fit
model = sm.OLS(y,X)
f = model.fit()
f.summary()