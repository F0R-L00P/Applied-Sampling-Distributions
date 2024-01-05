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
'''
import numpy as np

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
bootstrap_stats, confidence_interval = bootstrap_confidence_interval(data, np.mean, R=10, confidence_level=95)

bootstrap_stats, confidence_interval



