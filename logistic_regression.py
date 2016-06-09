import math
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Load data on loans
loans = pd.read_csv("loans_clean.csv")

# Create boolean column for interest rate < 12%
# I'm used to defining functions out like this, but there's probably something quicker for pandas
def less_than_12(rate):
	if rate < 0.12:
		return 1
	else:
		return 0

loans['IR_TF'] = loans['Interest.Rate'].map(less_than_12)

# Add 1's column for statsmodel
loans['Intercept'] = 1

# Create a list of column names for independent variables
ind_vars = ['FICO.Score', 'Amount.Requested', 'Intercept']

# Define the logistic regression model
logit = sm.Logit(loans['IR_TF'], loans[ind_vars])
result = logit.fit()

# Create coefficient object for our model
log_coeff = result.params

# Find P(interest rate < 12%) given logistic model coefficients, FICo score, and amount requested
def logistic_function(coeff, score, amount):
	a = coeff['Intercept'] + coeff['FICO.Score'] * score + coeff['Amount.Requested'] * amount
	prob = 1/(1 + math.e ** (-1 * a))
	return prob

# Example use of logistic_function
print logistic_function(log_coeff,720,10000)

# Visualize the model output with a range of FICO scores at $10,000 requested
x = range(600,800)
y = [logistic_function(log_coeff, i, 10000) for i in x]
plt.plot(x,y)
plt.show()