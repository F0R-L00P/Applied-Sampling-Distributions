"""
NOTE: NULL Expectation is defined loosely as “nothing unusual in the data"
also termed the “null hypothesis” or “null model”. The statistics that measures the 
extent to which results depart from the null expectation of independence 
is the chi-square statistic.
"""

import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt

# Values for degrees of freedom
dfs = [1, 2, 3, 5, 10]

# Generate values from 0 to 20 for x-axis
x = np.linspace(0, 20, 1000)

# Plot the chi-square distribution for each degrees of freedom
plt.figure(figsize=(10, 6))
for df in dfs:
    plt.plot(x, chi2.pdf(x, df), label=f'DF={df}')

plt.title('Chi-square Distribution for Different Degrees of Freedom')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()