'''
1) Initial Sample: 
    From population of 1,000,000, you take an initial sample of 10,000 observations.

2) Bootstrap Resampling: 
    You then use these 10,000 observations as your new base for resampling.

3) Creating Bootstrap Samples: 
    You create additional samples by resampling from this initial sample. 
    Each of these new samples, known as bootstrap samples, will also have 10,000 observations.

4) Sampling with Replacement: 
    This resampling is done with replacement, meaning any specific observation from the initial 10,000 
    can be chosen multiple times and appear more than once in each bootstrap sample.

5) Number of Bootstrap Samples: 
    You'll do this resampling process 5 times (or n times as needed), 
    resulting in 5 separate bootstrap samples. Each of these samples is 
    the same size as your initial sample, i.e., 10,000 observations.

6) Result: 
    You end up with 5 bootstrap samples, each containing 10,000 observations drawn from your initial sample of 10,000.

7) Analysis: 
    For each of these 5 bootstrap samples, you can calculate your statistic of interest 
    (like the mean, median, or standard deviation), and then use these calculations 
    to understand the variability or construct confidence intervals for your statistic.

NOTE: Computationally intensive, but can be done in parallel.
'''

import numpy as np

# Function to perform bootstrap resampling and store both samples and their means
def bootstrap_resample_and_store_samples(original_sample, num_bootstrap_samples, sample_size):
    # Arrays to store the bootstrap samples and their means
    bootstrap_samples = np.zeros((num_bootstrap_samples, sample_size))
    bootstrap_sample_means = np.zeros(num_bootstrap_samples)

    for i in range(num_bootstrap_samples):
        # Resample with replacement from the original sample
        bootstrap_sample = np.random.choice(original_sample, size=sample_size, replace=True)
        # Store the bootstrap sample
        bootstrap_samples[i] = bootstrap_sample
        # Calculate and store the mean of the bootstrap sample
        bootstrap_sample_means[i] = np.mean(bootstrap_sample)

    return bootstrap_samples, bootstrap_sample_means

# Example Usage
np.random.seed(0) # For reproducibility

# Parameters
population_mean = 170  # Mean height
population_std = 10    # Standard deviation
sample_size = 1000000     # Size of the initial sample
num_bootstrap_samples = 100  # Number of bootstrap samples to generate for demonstration

# Generate an initial sample
original_sample = np.random.normal(population_mean, population_std, sample_size)

# Perform bootstrap resampling and store the samples and their means
bootstrap_samples, bootstrap_means = bootstrap_resample_and_store_samples(original_sample, num_bootstrap_samples, sample_size)

# Display the first bootstrap sample and its mean for demonstration
bootstrap_samples[:10], bootstrap_means[:10]