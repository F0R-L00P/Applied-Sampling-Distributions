'''
NOTE: Frequency tables, histograms, boxplots, and standard errors 
are all ways to understand the potential error in a sample estimate. 
Confidence intervals are another.

Goal: 
    A confidence interval gives you a range within which you expect the 
    true population parameter (like the mean) to fall.

Confidence Level: 
    This is usually set at a certain percentage, like 95%, indicating how 
    confident you are that the interval contains the true parameter.

Algorithm for a bootstrap confidence interval is as follows:

1) Draw a random sample of size n with replacement from the data (a resample).
2) Record the statistic of interest for the resample.
3) Repeat steps 1-2 many (R) times.
4) For an x% confidence interval, trim [(100-x) / 2]% of the 
    R resample results from either end of the distribution.
5) The trim points are the endpoints of an x% bootstrap confidence interval.
'''
import numpy as np
import matplotlib.pyplot as plt

def bootstrap_confidence_interval(data, statistic_func, R, confidence_level):
    # Initialize an array to store the bootstrap statistics
    bootstrap_statistics = np.zeros(R)

    # Perform R bootstrap resamples using a for loop
    for i in range(R):
        # Resample with replacement from the original data
        resample = np.random.choice(data, size=len(data), replace=True)
        # Calculate and store the statistic for this resample
        bootstrap_statistics[i] = statistic_func(resample)

    # Calculate the confidence interval
    lower_percentile = (100 - confidence_level) / 2
    upper_percentile = 100 - lower_percentile
    confidence_interval = np.percentile(bootstrap_statistics, [lower_percentile, upper_percentile])

    return bootstrap_statistics, confidence_interval

# Example data and usage
data = np.array([85, 90, 78, 92, 88, 75, 84, 82, 89, 91])
bootstrap_stats, confidence_interval = bootstrap_confidence_interval(data, np.mean, R=1000, confidence_level=90)

bootstrap_stats, confidence_interval

# Plotting
plt.hist(bootstrap_stats, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(confidence_interval[0], color='red', linestyle='dashed', linewidth=2, label='90% CI Lower')
plt.axvline(confidence_interval[1], color='green', linestyle='dashed', linewidth=2, label='90% CI Upper')
plt.title('Bootstrap Statistics with 90% Confidence Interval')
plt.xlabel('Mean Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()