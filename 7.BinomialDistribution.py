"""
NOTE: Yes/no (binomial) | buy/don’t buy | click/don’t click | survive/die

distribution that summarizes the likelihood 
that a value will take one of two INDEPENDENT states
The parameters that define a binomial distribution are:

n -> (the number of trials or experiments) 
and 
p -> (the probability of the event occurring in each trial).

Trial
    An event with a discrete outcome (e.g., a coin flip).

Success
    The outcome of interest for a trial.

The binomial distribution is the frequency distribution of 
the number of successes (x) in a given number of trials (n) 
with specified probability (p) of success in each trial. 

Basically Whenever you're looking at events that have two outcomes 
(click or no click, fail or not fail) and these events are INDEPENDENT 
and have the same chance of occurring, you're dealing with a binomial situation.

NOTE: PROBLEM
        assuming I want to see how many times out of 10 I will be successful 
        completing a clime within 5 minutes. 

        number of trils (n) = 10
        probability of success (p) = 0.7
        number of successes (k) = ? -> what we are trying to measure
"""

from scipy.stats import binom
import matplotlib.pyplot as plt

# Define the parameters for the binomial distribution
n = 10  # Number of trials
p = 0.7  # Probability of success on a single trial

# Generate a range of possible number of successes (from 0 to n)
k = range(0, n + 1)

# Calculate the probability for each number of successes
probabilities = binom.pmf(k, n, p)

# Create a bar chart to visualize the probability distribution
plt.bar(k, probabilities, color="teal", alpha=0.7)
plt.title("Binomial Distribution - Probability of Completing a Climb within 5 Minutes")
plt.xlabel("Number of Successful Climbs out of 10 Attempts")
plt.ylabel("Probability")
plt.xticks(k)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

"""
NOTE: the height of the bar over 7 successful climbs is just over 0.25, 
it means that, given your scenario of 10 climbing attempts with a 70% success 
rate for each climb, you have slightly more than a 25% chance 
of completing exactly 7 climbs within 5 minutes.
"""

# Example 2
"""
PROBLEM:
    Suppose you want to calculate the probability 
    of getting a certain 3 heads
    when flipping a fair coin 5 times.
"""
# Define the parameters for the binomial distribution
n = 5  # Number of trials (coin flips)
p = 0.5  # Probability of success on a single trial (getting a head)

# Generate a range of possible number of successes (from 0 to n)
k = range(0, n + 1)

# Calculate the probability for each number of successes
probabilities = binom.pmf(k, n, p)

# Create a bar chart to visualize the probability distribution
plt.bar(k, probabilities, color="skyblue", alpha=0.7)
plt.title("Binomial Distribution - Probability of Getting Heads in 5 Coin Flips")
plt.xlabel("Number of Heads")
plt.ylabel("Probability")
plt.xticks(k)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

"""
NOTE: calculate each probability of getting 0, 1, 2, 3, 4, or 5 heads
        and then visualize the distribution using a bar chart.

        The probability of getting 0 head in 5 coin flips is 0.03125,
        the probability of getting 1 head in 5 coin flips is 0.15625,
        the probability of getting 2 heads (3 tails) in 5 coin flips is 0.3125,
        the probability of getting 3 heads in 5 coin flips is 0.3125,
        the probability of getting 4 heads in 5 coin flips is 0.15625,
        the probability of getting 5 heads in 5 coin flips is 0.03125.
"""