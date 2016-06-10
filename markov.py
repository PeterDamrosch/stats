import pandas as pd

# Example markov with 2 x 2 matrix
df = pd.DataFrame({'rainy': [.4,.7],
					'sunny': [.6,.3]
					},
					index=['rainy', 'sunny'])
print(df.dot(df))

# Example markv with 3 x 3 matrix
market_markov = {'bull': [0.9, 0.15, 0.25],
				'bear': [0.075, 0.8, 0.25],
				'stagnant': [0.025, 0.05, 0.5]
				}
df2 = pd.DataFrame(market_markov, index=['bull', 'bear', 'stagnant'])
print df2

# Find steady state probabilities
x = 10
while x > 0:
	df2 = df2.dot(df2)
	print df2
	x -= 1
