'''
Tail:
    The long narrow portion of a frequency distribution, 
    where relatively extreme values occur at low frequency.

Skew:
    Where one tail of a distribution is longer than the other.

Implications in Data Analysis
1) Outliers: 
    Long-tailed distributions often imply the presence of significant outliers.

2) Predictive Modeling: 
    When modeling data with long tails, traditional methods that assume a 
    normal distribution (like least squares regression) may not be appropriate.
'''
import numpy as np
import matplotlib.pyplot as plt

# Generate a sample from a Pareto distribution
alpha = 3.0 # Shape parameter
size = 1000 # Sample size
samples = np.random.pareto(alpha, size)

# Create a histogram of the sample
plt.figure(figsize=(10, 6))
count, bins, ignored = plt.hist(samples, 100, density=True, alpha=0.7, color='blue')

# Fit a line to the histogram to show the long tail
fit = alpha * size * (bins**(alpha-1)) / (bins**alpha).sum()
plt.plot(bins, max(count)*fit/max(fit), linewidth=2, color='red')

# Annotations
plt.title("Pareto Distribution Histogram (Long-Tailed Distribution)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.text(5, 0.05, 'Long Tail\nRegion', horizontalalignment='center', verticalalignment='center',
         bbox=dict(facecolor='red', alpha=0.5))
plt.axvline(x=1, linestyle='--', color='green', label='x_min (minimum value for Pareto)')
plt.legend()
plt.tight_layout()
# Show the plot
plt.show()


'''
* The x-axis represents the values of the distribution.
* The y-axis shows the frequency of these values.
* The red line is a fit to the histogram, highlighting the long-tail characteristic.
* The green dashed line represents the minimum value (x_min) for the Pareto distribution, 
    beyond which the long-tail behavior is observed.
* The area labeled 'Long Tail Region' indicates where the tail of the distribution extends, 
    demonstrating that values far from the mean are more frequent than they would be in a 
    short-tailed distribution (like a normal distribution).
'''