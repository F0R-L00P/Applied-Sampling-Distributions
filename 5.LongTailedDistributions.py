"""
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
"""

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Generate a sample from a Pareto distribution
alpha = 3.0  # Shape parameter
size = 1000  # Sample size
samples = np.random.pareto(alpha, size)

# Create a histogram of the sample
plt.figure(figsize=(10, 6))
count, bins, ignored = plt.hist(samples, 100, density=True, alpha=0.7, color="blue")

# Fit a line to the histogram to show the long tail
fit = alpha * size * (bins ** (alpha - 1)) / (bins**alpha).sum()
plt.plot(bins, max(count) * fit / max(fit), linewidth=2, color="red")

# Annotations
plt.title("Pareto Distribution Histogram (Long-Tailed Distribution)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.text(
    5,
    0.05,
    "Long Tail\nRegion",
    horizontalalignment="center",
    verticalalignment="center",
    bbox=dict(facecolor="red", alpha=0.5),
)
plt.axvline(
    x=1, linestyle="--", color="green", label="x_min (minimum value for Pareto)"
)
plt.legend()
plt.tight_layout()
# Show the plot
plt.show()


"""
* The x-axis represents the values of the distribution.
* The y-axis shows the frequency of these values.
* The red line is a fit to the histogram, highlighting the long-tail characteristic.
* The green dashed line represents the minimum value (x_min) for the Pareto distribution, 
    beyond which the long-tail behavior is observed.
* The area labeled 'Long Tail Region' indicates where the tail of the distribution extends, 
    demonstrating that values far from the mean are more frequent than they would be in a 
    short-tailed distribution (like a normal distribution).
"""


# NOTE QQ-PLOT

# Generate a sample from a Pareto distribution
alpha = 3.0  # Shape parameter
size = 1000  # Sample size
samples = np.random.pareto(alpha, size)

# Generate QQ-plot for the Pareto samples against normal distribution
plt.figure(figsize=(10, 6))
(stats.probplot(samples, dist="norm", plot=plt))

# Updated title and axis labels
plt.title("Modified QQ-plot: Pareto vs. Normal Distribution")
plt.xlabel("Quantiles of Normal Distribution")
plt.ylabel("Z-score (Pareto Samples)")

# Additional annotations or changes
plt.grid(True)  # Keep the grid for better readability
# plt.axhline(y=0, color="r", linestyle="-")  # Add a horizontal line at y=0
plt.axvline(x=0, color="green", linestyle="--")  # Add a vertical line at x=0
plt.text(
    0, 3, "Center Point", horizontalalignment="center", verticalalignment="center"
)  # Add text annotation

# Show the modified plot
plt.show()


"""
for QQ-Plots
If the points are far below the line for low values and far above the line 
for high values, indicating the data are not normally distributed. 

This means that we are much more likely to observe extreme values than would 
be expected if the data had a normal distribution. 

Another common phenomenon: the points are close to the line for the data within 
one standard deviation of the mean. Tukey refers to this phenomenon as 
data being “normal in the middle” but having much longer tails
"""
