#Use the script to generate and save a boxplot, histogram, 
#and QQ-plot for the values in the "Amount.Requested" column.

import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd

# Load data on loans and drop null entries
loans = pd.read_csv("https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv")
loans.dropna(inplace=True)

# Create and save boxplot, histogram, and qq-plot for Amount.Requested
loans.boxplot(column="Amount.Requested")
plt.savefig("boxplotRequested.png")

loans.hist(column="Amount.Requested")
plt.savefig("histogramRequested.png")

plt.figure()
stats.probplot(loans["Amount.Requested"], dist="norm", plot=plt)
plt.savefig("qqplotRequested.png")

