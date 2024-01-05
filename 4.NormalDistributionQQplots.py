'''
In a normal distribution 68% of the data lies within 
one standard deviation of the mean, and 95% lies within 
two standard deviations, and 99.7% lies within three standard deviations.  

A QQ-Plot is used to visually determine how close a sample is 
to a specified distribution—in this case, the normal distribution. 

QQ-Plot orders the z-scores from low to high and plots each value's z-score on the y-axis; 
the x-axis is the corresponding quantile of a normal distribution for that value's rank

NOTE: If the points roughly fall on the diagonal line, 
then the sample distribution can be considered close to normal

in essence QQ-Plots compares the quantiles of the sample data 
to the quantiles of the specified theoretical distribution
'''

import numpy as np 
import matplotlib.pyplot as plt 
import scipy.stats as stats

'''
NOTE: The resulting image shows that the normally distributed data 
closely follow the diagonal line in the QQ-Plot, 
indicating that the data is consistent with a normal distribution. 
If your dataset were not normally distributed, the points on the 
QQ-Plot would deviate from this line, providing a visual indication 
of how the data distribution differs from the normal distribution.
'''

# Generate a normally distributed random sample
np.random.seed(0)
normal_data = np.random.normal(loc=0, scale=1, size=1000)

# Set up the matplotlib figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot a histogram of the normally distributed data on the left subplot (ax1)
ax1.hist(normal_data, bins=30, alpha=0.7, color='blue', edgecolor='black')
ax1.set_title('Histogram of Normal Distribution')
ax1.set_xlabel('Value')
ax1.set_ylabel('Frequency')
ax1.grid(True)  # Optional: add gridlines

# Generate a QQ plot of the normally distributed data on the right subplot (ax2)
stats.probplot(normal_data, dist="norm", plot=ax2)
ax2.set_title('QQ Plot of Normal Distribution')
ax2.get_lines()[1].set_color('red')  # Optional: change the color of the line
ax2.grid(True)  # Optional: add gridlines

# Show the plots side by side
plt.tight_layout()
plt.show()

#######################################################################
#NOTE: If the distribution is non-normal and plotted on normal QQ-Plot,
# the points will deviate from the diagonal line

# Generate a non-normal distribution sample (for example, exponential)
np.random.seed(0)
non_normal_data = np.random.exponential(scale=1, size=1000)

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot histogram for the non-normal distribution
ax1.hist(non_normal_data, bins=30, alpha=0.7, color='blue', edgecolor='black')
ax1.set_title('Histogram of Non-Normal Distribution')
ax1.set_xlabel('Value')
ax1.set_ylabel('Frequency')
ax1.grid(True)  

# Plot QQ-Plot for the non-normal distribution against a normal theoretical distribution
stats.probplot(non_normal_data, dist="norm", plot=ax2)
ax2.set_title('QQ Plot Against Normal Distribution')
ax2.set_xlabel('Theoretical Quantiles')
ax2.set_ylabel('Sample Quantiles')
ax2.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()


#######################################################################
# Generate a sample from an exponential distribution
np.random.seed(0)
exponential_data = np.random.exponential(scale=1, size=1000)

# Create subplots for the exponential distribution
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot histogram for the Exponential distribution
ax1.hist(exponential_data, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
ax1.set_title('Histogram of Exponential Distribution')
ax1.set_xlabel('Value')
ax1.set_ylabel('Frequency')
ax2.grid(True) 

# Plot QQ-Plot for the Exponential distribution
stats.probplot(exponential_data, dist="expon", plot=ax2)
ax2.set_title('QQ Plot of Exponential Distribution')
ax2.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()
#######################################################################
# Generate a sample from a Weibull distribution
np.random.seed(0)
weibull_data = np.random.weibull(a=1.5, size=1000)  # 'a' is the shape parameter of the Weibull distribution

# Create subplots for the Weibull distribution
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot histogram for the Weibull distribution
ax1.hist(weibull_data, bins=30, alpha=0.7, color='purple', edgecolor='black')
ax1.set_title('Histogram of Weibull Distribution')
ax1.set_xlabel('Value')
ax1.set_ylabel('Frequency')
ax1.grid(True)

# Plot QQ-Plot for the Weibull distribution
stats.probplot(weibull_data, dist="weibull_min", sparams=(1.5,), plot=ax2)
ax2.set_title('QQ Plot of Weibull Distribution')
ax2.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()