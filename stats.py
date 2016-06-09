from scipy import stats
import pandas as pd

# Avg weekly spending on alcohol and tobacco in pounds (Great Britain)
# http://lib.stat.cmu.edu/DASL/Datafiles/AlcoholandTobacco.html
data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

# Split on lines and commas
data = data.splitlines()
data = [i.split(',') for i in data]

# Create dataframe
column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)

# Convert columns
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

# Find mean, median, mode, range, variance, and standard deviation
mean = df['Alcohol'].mean()
median = df['Alcohol'].median()
mode = stats.mode(df['Alcohol'])[0][0]
range = max(df['Alcohol']) - min (df['Alcohol'])
variance = df['Alcohol'].var()
standard_deviation = df['Alcohol'].std()

summary_stats = {
    "mean" : mean,
    "median" : median,
    "mode" : mode,
    "range" : range,
    "variance": variance,
    "standard deviation" : standard_deviation
}

# Print the result for each value
for k,v in summary_stats.iteritems():
    print "The {} for Alcohol in the Alcohol and Tobacco dataset is {}".format(k, str(v))

