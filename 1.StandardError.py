import numpy as np

'''
1) Sampling the Population: 
    you first take samples from the population. For instance, from a population of 1,000,000, 
    you might take 5 samples, each consisting of 1,000 individuals.

2) Calculate the Mean of Each Sample: 
    calculate the mean for each of the 5 samples. Each sample will have its own mean.

3) Calculate the Standard Deviation of the Sample Means, Not Individual Samples: 
    don't calculate and average the standard deviations of the 5 samples. 
    calculate the standard deviation of the 5 sample means you found in step 2. 
    This is a crucial step as it measures the variability of these sample means.

4) Calculate the Standard Error: 
    Finally, calculate the standard error, which is the standard deviation of the sample means (from step 3) 
    divided by the square root of the sample size (which is 1,000 in your example).

The formula for standard error is:
SE= s/√n
    where s is the standard deviation of the sample means, and 
    n is the size of each sample.

This process estimates how much variability you can expect in the sample means compared to the true population mean.'''

# Function to simulate sampling and calculate standard error
def simulate_sampling(population_mean, population_std, sample_size, num_samples):
    # Generate random samples
    samples = np.random.normal(population_mean, population_std, (num_samples, sample_size))
    
    # Calculate sample means
    sample_means = np.mean(samples, axis=1)
    
    # Calculate standard deviation of the sample means
    sample_means_std = np.std(sample_means)
    
    # Calculate standard error
    standard_error = sample_means_std / np.sqrt(sample_size)
    
    return sample_means, standard_error

# Parameters
population_mean = 175  # Population mean (e.g., average height in cm)
population_std = 10   # Estimated population standard deviation
sample_size = 10      # Number of individuals in each sample
num_samples = 5       # Number of samples

# Simulate sampling and calculate standard error
sample_means, standard_error = simulate_sampling(population_mean, population_std, sample_size, num_samples)

sample_means, standard_error