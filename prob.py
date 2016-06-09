#Write a script called "prob.py" that outputs frequencies, 
#as well as creates and saves a boxplot, a histogram, and a QQ-plot for the data in this lesson. 

import collections
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Test data
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

# Frequency
freq = collections.Counter(x)

# Create and save boxplot, histogram, and QQ-plot
plt.boxplot(x)
plt.savefig("boxplotX.png")

plt.figure()
plt.hist(x)
plt.savefig("histogramX.png")

plt.figure()
qq_plot = stats.probplot(x, dist="norm", plot=plt)
plt.savefig("qqplotX.png")






