## Histograms

'''
We can graph histograms using a Python module known as Matplotlib. We're not going to go into detail about Matplotlib’s plotting functions, but if you're interested in learning more, take our course Introduction to Matplotlib.

For now, familiarize yourself with the following syntax to draw a histogram:

# This imports the plotting package.  We only need to do this once.
from matplotlib import pyplot as plt

# This plots a histogram
plt.hist(data)

# This displays the histogram
plt.show()
When we enter plt.hist with no keyword arguments, matplotlib will automatically make a histogram with 10 bins of equal width that span the entire range of our data.

If you want a different number of bins, use the keyword bins. For instance, the following code would give us 5 bins, instead of 10:

plt.hist(data, bins=5)
If you want a different range, you can pass in the minimum and maximum values that you want to histogram using the keyword range. We pass in a tuple of two numbers. The first number is the minimum value that we want to plot and the second value is the number that we want to plot up to, but not including.

For instance, if our dataset contained values between 0 and 100, but we only wanted to histogram numbers between 20 and 50, we could use this command:

# We pass 51 so that our range includes 50
plt.hist(data, range=(20, 51))
Here’s a complete example:

from matplotlib import pyplot as plt

d = np.array([1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5])

plt.hist(d, bins=5, range=(1, 6))

plt.show()
'''

import numpy as np
# Write matplotlib import here:
from matplotlib import pyplot as plt
commutes = np.genfromtxt('commutes.csv', delimiter=',')

# Plot histogram here:
plt.hist(commutes, bins=6, range=(20,50))
plt.show()


## Normal Distribution

'''
We can generate our own normally distributed datasets using NumPy. Using these datasets can help us better understand the properties and behavior of different distributions. We can also use them to model results, which we can then use as a comparison to real data.

In order to create these datasets, we need to use a random number generator. The NumPy library has several functions for generating random numbers, including one specifically built to generate a set of numbers that fit a normal distribution: np.random.normal. This function takes the following keyword arguments:

loc: the mean for the normal distribution
scale: the standard deviation of the distribution
size: the number of random numbers to generate
a = np.random.normal(0, 1, size=100000)
If we were to plot this set of random numbers as a histogram, it would look like this:
'''
import numpy as np
from matplotlib import pyplot as plt

# Brachiosaurus
b_data = np.random.normal(6.7, 0.7, size=1000)

# Fictionosaurus
f_data = np.random.normal(7.7, 0.3, size=1000)

plt.hist(b_data,
         bins=30, range=(5, 8.5), histtype='step',
         label='Brachiosaurus')
plt.hist(f_data,
         bins=30, range=(5, 8.5), histtype='step',
         label='Fictionosaurus')
plt.xlabel('Femur Length (ft)')
plt.legend(loc=2)
plt.show()

mystery_dino = 'Brachiosaurus'  # for femur w/ length 6.6

answer = False # femur w/ length 7.5 while likely a Fict still could be a Brach, given that probability of being a Brach is not zero


## Standard Deviations and Normal Distribution

'''
We know that the standard deviation affects the "shape" of our normal distribution. The last exercise helps to give us a more quantitative understanding of this.

Suppose that we have a normal distribution with a mean of 50 and a standard deviation of 10. When we say "within one standard deviation of the mean", this is what we are saying mathematically:

lower_bound = mean - std
            = 50 - 10
            = 40

upper_bound = mean + std
            = 50 + 10
            = 60
It turns out that we can expect about 68% of our dataset to be between 40 and 60, for this distribution.

As we saw in the previous exercise, no matter what mean and standard deviation we choose, 68% of our samples will fall between +/- 1 standard deviation of the mean!

In fact, here are a few more helpful rules for normal distributions:

68% of our samples will fall between +/- 1 standard deviation of the mean
95% of our samples will fall between +/- 2 standard deviations of the mean
99.7% of our samples will fall between +/- 3 standard deviations of the mean
'''

## Binomial Distributions

'''
t's known that a certain basketball player makes 30% of his free throws. On Friday night’s game, he had the chance to shoot 10 free throws. How many free throws might you expect him to make? We would expect 0.30 * 10 = 3.

However, he actually made 4 free throws out of 10 or 40%. Is this surprising? Does this mean that he’s actually better than we thought?

The binomial distribution can help us. It tells us how likely it is for a certain number of “successes” to happen, given a probability of success and a number of trials.

In this example:

The probability of success was 30% (he makes 30% of free throws)
The number of trials was 10 (he took 10 shots)
The number of successes was 4 (he made 4 shots)
The binomial distribution is important because it allows us to know how likely a certain outcome is, even when it's not the expected one. From this graph, we can see that it's not that unlikely an outcome for our basketball player to get 4 free throws out of 10. However, it would be pretty unlikely for him to get all 10.
'''

'''
There are some complicated formulas for determining these types of probabilities. Luckily for us, we can use NumPy - specifically, its ability to generate random numbers. We can use these random numbers to model a distribution of numerical data that matches the real-life scenario we're interested in understanding.

For instance, suppose we want to know the different probabilities of our basketball player making 1, 2, 3, etc. out of 10 shots.

NumPy has a function for generating binomial distributions: np.random.binomial, which we can use to determine the probability of different outcomes.

The function will return the number of successes for each "experiment".

It takes the following arguments:

N: The number of samples or trials
P: The probability of success
size: The number of experiments
Let's generate a bunch of "experiments" of our basketball player making 10 shots. We choose a big N to be sure that our probabilities converge on the correct answer.

# Let's generate 10,000 "experiments"
# N = 10 shots
# P = 0.30 (30% he'll get a free throw)

a = np.random.binomial(10, 0.30, size=10000)
Now we have a record of 10,000 experiments. We can use Matplotlib to plot the results of all of these experiments:

plt.hist(a, range=(0, 10), bins=10, normed=True)
plt.xlabel('Number of "Free Throws"')
plt.ylabel('Frequency')
plt.show()
'''

import numpy as np
from matplotlib import pyplot as plt

emails = np.random.binomial(500,0.05, size=10000)

plt.hist(emails)
plt.show()


## Binomial Distributions and Probability
'''
Let's return to our original question:

Our basketball player has a 30% chance of making any individual basket. He took 10 shots and made 4 of them, even though we only expected him to make 3. What percent chance did he have of making those 4 shots?

We can calculate a different probability by counting the percent of experiments with the same outcome, using the np.mean function.

Remember that taking the mean of a logical statement will give us the percent of values that satisfy our logical statement.

Let's calculate the probability that he makes 4 baskets:

a = np.random.binomial(10, 0.30, size=10000)
np.mean(a == 4)
When we plug run this code, we might get:

>> 0.1973
Remember, because we're using a random number generator, we'll get a slightly different result each time. With the large size we chose, the calculated probability should be accurate to about 2 decimal places.

So, our basketball player has a roughly 20% chance of making 4 baskets

This suggests that what we observed wasn't that unlikely. It's quite possible that he hasn't got any better; he just got lucky.
'''

import numpy as np

emails = np.random.binomial(500, 0.05, size=10000)

no_emails = np.mean(np.random.binomial(0, 0.05, size=10000))
#print(np.mean(emails == 0))
print(no_emails)

b_test_emails = np.mean(emails > 500*0.08)
print(b_test_emails)


## Review

import numpy as np
from matplotlib import pyplot as plt

sunflowers = np.genfromtxt('sunflower_heights.csv',
                           delimiter=',')

# Calculate mean and std of sunflowers here:
sunflowers_mean = np.mean(sunflowers)
sunflowers_std = np.std(sunflowers)

# Calculate sunflowers_normal here:
sunflowers_normal = np.random.normal(sunflowers_mean, sunflowers_std, size=5000)

plt.hist(sunflowers,
         range=(11, 15), histtype='step', linewidth=2,
        label='observed', normed=True)
plt.hist(sunflowers_normal,
         range=(11, 15), histtype='step', linewidth=2,
        label='normal', normed=True)
plt.legend()
plt.show()

# Calculate probabilities here:
experiments = np.random.binomial(200, 0.1, size=5000)
prob = np.mean(experiments < 20)
print(prob)








