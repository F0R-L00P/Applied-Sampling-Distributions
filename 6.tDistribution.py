'''
The t-distribution is a normally shaped distribution, 
except that it is a bit thicker and longer on the tails.

n
    Sample size.

Degrees of freedom
    A parameter that allows the t-distribution to adjust to 
    different sample sizes, statistics, and numbers of groups.

NOTE:The Student's t-distribution is a type of statistical graph 
(or distribution) that's used when you're working with small groups of data
and you don't know the standard deviation 
(which is a measure of how spread out the data is) of the entire population 
you're interested in. When you have a small sample (like less than 30 data points), 
the t-distribution helps you make better guesses about the whole population. 
For larger samples, it behaves almost like the normal distribution.
'''

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Sample values for degrees of freedom
dfs = [1, 5, 10, 30]

# Generate a range of t-values
t_values = np.linspace(-5, 5, 100)

# Plot the t-distributions for different degrees of freedom
plt.figure(figsize=(10, 6))

for df in dfs:
    plt.plot(t_values, stats.t.pdf(t_values, df), label=f'DF={df}')

plt.title('Student\'s t-Distributions for Different Degrees of Freedom')
plt.xlabel('t-value')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
