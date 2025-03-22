# Pupulation Mean vs Sample Mean

import numpy as np

population = np.random.normal(loc=65, scale=3.5, size=300)
population_mean = np.mean(population)

print "Population Mean: {}".format(population_mean)

sample_1 = np.random.choice(population, size=30, replace=False)
sample_2 = np.random.choice(population, size=30, replace=False)
sample_3 = np.random.choice(population, size=30, replace=False)
sample_4 = np.random.choice(population, size=30, replace=False)
sample_5 = np.random.choice(population, size=30, replace=False)

sample_1_mean = np.mean(sample_1)
print "Sample 1 Mean: {}".format(sample_1_mean)

sample_2_mean = np.mean(sample_2)
sample_3_mean = np.mean(sample_3)
sample_4_mean = np.mean(sample_4)
sample_5_mean = np.mean(sample_5)

print "Sample 2 Mean: {}".format(sample_2_mean)
print "Sample 3 Mean: {}".format(sample_3_mean)
print "Sample 4 Mean: {}".format(sample_4_mean)
print "Sample 5 Mean: {}".format(sample_5_mean)



## Central Limit Theorem
'''
There is one surefire way to mitigate the risk of having a skewed sample mean — take a larger set of samples. The sample mean of a larger sample set will more closely approximate the population mean. This phenomenon, known as the Central Limit Theorem, states that if we have a large enough sample size, all of our sample means will be sufficiently close to the population mean.

Later, we'll learn how to put numeric values on "large enough" and "sufficiently close".
'''


import numpy as np

# Create population and find population mean
population = np.random.normal(loc=65, scale=100, size=3000)
population_mean = np.mean(population)

# Select increasingly larger samples
extra_small_sample = population[:10]
small_sample = population[:50]
medium_sample = population[:100]
large_sample = population[:500]
extra_large_sample = population[:1000]

# Calculate the mean of those samples
extra_small_sample_mean = np.mean(extra_small_sample)
small_sample_mean = np.mean(small_sample)
medium_sample_mean = np.mean(medium_sample)
large_sample_mean = np.mean(large_sample)
extra_large_sample_mean = np.mean(extra_large_sample)

# Print them all out!
print "Extra Small Sample Mean: {}".format(extra_small_sample_mean)
print "Small Sample Mean: {}".format(small_sample_mean)
print "Medium Sample Mean: {}".format(medium_sample_mean)
print "Large Sample Mean: {}".format(large_sample_mean)
print "Extra Large Sample Mean: {}".format(extra_large_sample_mean)

print "\nPopulation Mean: {}".format(population_mean)


## Hypothesis Tests

'''
When observing differences in data, a data analyst understands the possibility that these differences could be the result of random chance.

Suppose we want to know if men are more likely to sign up for a given programming class than women. We invite 100 men and 100 women to this class. After one week, 34 women sign up, and 39 men sign up. More men than women signed up, but is this a "real" difference?

We have taken sample means from two different populations, men and women. We want to know if the difference that we observe in these sample means reflects a difference in the population means. To formally answer this question, we need to re-frame it in terms of probability:

"What is the probability that men and women have the same level of interest in this class and that the difference we observed is just chance?"

In other words, "If we gave the same invitation to every person in the world, would more men still sign up?"

A more formal version is: "What is the probability that the two population means are the same and that the difference we observed in the sample means is just chance?"

These statements are all ways of expressing a null hypothesis. A null hypothesis is a statement that the observed difference is the result of chance.

Hypothesis testing is a mathematical way of determining whether we can be confident that the null hypothesis is false. Different situations will require different types of hypothesis testing, which we will learn about in the next lesson.
'''

## Type I or Type II

import numpy as np

def intersect(list1, list2):
  return [sample for sample in list1 if sample in list2]

# the true positives and negatives:
actual_positive = [2, 5, 6, 7, 8, 10, 18, 21, 24, 25, 29, 30, 32, 33, 38, 39, 42, 44, 45, 47]
actual_negative = [1, 3, 4, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 22, 23, 26, 27, 28, 31, 34, 35, 36, 37, 40, 41, 43, 46, 48, 49]

# the positives and negatives we determine by running the experiment:
experimental_positive = [2, 4, 5, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 24, 26, 27, 28, 32, 35, 36, 38, 39, 40, 45, 46, 49]
experimental_negative = [1, 3, 6, 12, 14, 23, 25, 29, 30, 31, 33, 34, 37, 41, 42, 43, 44, 47, 48]

#define type_i_errors and type_ii_errors here
'''Type 1 Errors are False Positives where the null-hypothesis is rejected and there really isn't a difference between data sets.

Type II Error is a false negative, where you wrongly rejected the null hypothesis and think there is a statistically significant diference in data when there really isn't'''


type_i_errors = intersect(actual_negative, experimental_positive)

type_ii_errors = intersect(actual_positive, experimental_negative)


# P Values

'''
We have discussed how a hypothesis test is used to determine the validity of a null hypothesis. A hypothesis test provides a numerical answer, called a p-value, that helps us decide how confident we can be in the result. A p-value is the probability that the null hypothesis is true.

A p-value of 0.05 would mean that there is a 5% chance that the null hypothesis is true. This generally means there is a 5% chance that there is no difference between the two population means.

Before conducting a hypothesis test, we determine the necessary threshold we would need before concluding that the results are significant. A higher p-value is more likely to give a false positive so if we want to be very sure that the result is not due to just chance, we will select a very small p-value.

It is important that we choose the p-value before we see the results. If we wait until after we see the results, we might pick our threshold such that we get the result we want to see. For instance, if we're trying to publish our results, we might set a p-value such that our results are significant. Choosing our p-value in advance helps keep us honest.

Generally, we want a p-value of less than 0.05, meaning that there is a less than 5% chance that our results are due to random chance.
'''

def accept_null_hypothesis(p_value):
  """
  Returns the truthiness of the null_hypothesis

  Takes a p-value as its input and assumes p < 0.05 is significant
  """
  if p_value > 0.05:
    null_hypothesis = True
  else:
    null_hypothesis = False
  return null_hypothesis


hypothesis_tests = [0.1, 0.009, 0.051, 0.012, 0.37, 0.6, 0.11, 0.025, 0.0499, 0.0001]

for p_value in hypothesis_tests:
    accept_null_hypothesis(p_value)


## Types of Hypothesis Testing

'''
When we are trying to compare datasets, we often need a way to be confident knowing if datasets are significantly different from each other.
Some situations involve correlating numerical data, such as:

a professor expects an exam average to be roughly 75%, and wants to know if the actual scores line up with this expectation. Was the test actually too easy or too hard?
a manager of a chain of stores wants to know if certain locations have different revenues on different days of the week. Are the revenue differences a result of natural fluctuations or a significant difference between the stores' sales patterns?
a PM for a website wants to compare the time spent on different versions of a homepage. Does one version make users stay on the page significantly longer?
Others involve categorical data, such as:

a pollster wants to know if men and women have significantly different yogurt flavor preferences. Does a result where men more often answer "chocolate" as their favorite reflect a significant difference in the population?
do different age groups have significantly different emotional reactions to different ads?
In this lesson, you will learn how about how we can use hypothesis testing to answer these questions. There are several different types of hypothesis tests for the various scenarios you may encounter. Luckily, SciPy has built-in functions that perform all of these tests for us, normally using just one line of code.

For numerical data, we will cover:

One Sample T-Tests
Two Sample T-Tests
ANOVA
Tukey Tests
For categorical data, we will cover:

Binomial Tests
Chi Square
After this lesson, you will have a wide range of tools in your arsenal to find meaningful correlations in data.

'''

## 1 Sample T-Testing

'''
Let's imagine the fictional business BuyPie, which sends ingredients for pies to your household, so that you can make them from scratch. Suppose that a product manager wants the average age of visitors to BuyPie.com to be 30. In the past hour, the website had 100 visitors and the average age was 31. Are the visitors too old? Or is this just the result of chance and a small sample size?

We can test this using a univariate T-test. A univariate T-test compares a sample mean to a hypothetical population mean. It answers the question "What is the probability that the sample came from a distribution with the desired mean?"

When we conduct a hypothesis test, we want to first create a null hypothesis, which is a prediction that there is no significant difference. The null hypothesis that this test examines can be phrased as such: "The set of samples belongs to a population with the target mean".

The result of the 1 Sample T Test is a p-value, which will tell us whether or not we can reject this null hypothesis. Generally, if we receive a p-value of less than 0.05, we can reject the null hypothesis and state that there is a significant difference.

SciPy has a function called ttest_1samp, which performs a 1 Sample T-Test for you.

ttest_1samp requires two inputs, a distribution of values and an expected mean:

tstat, pval = ttest_1samp(example_distribution, expected_mean)
print pval
It also returns two outputs: the t-statistic (which we won't cover in this course), and the p-value — telling us how confident we can be that the sample of values came from a distribution with the mean specified.
'''

from scipy.stats import ttest_1samp
import numpy as np

ages = np.genfromtxt("ages.csv")
print(ages)

ages_mean = np.mean(ages)
print(ages_mean)  # 31

tstat, pval = ttest_1samp(ages, 30)
print(pval)

'''In the last exercise, we got a p-value that was much higher than 0.05, so we cannot reject the null hypothesis. '''


# One Sample T-Test II

'''In the last exercise, we got a p-value that was much higher than 0.05, so we cannot reject the null hypothesis. Does this mean that if we wait for more visitors to BuyPie, the average age would definitely be 30 and not 31? Not necessarily. In fact, in this case, we know that the mean of our sample was 31.

P-values give us an idea of how confident we can be in a result. Just because we don’t have enough data to detect a difference doesn’t mean that there isn’t one. Generally, the more samples we have, the smaller a difference we’ll be able to detect. You can learn more about the exact relationship between the number of samples and detectable differences in the Sample Size Determination course.

To gain some intuition on how our confidence levels can change, let's explore some distributions with different means and how our p-values from the 1 Sample T-Tests change.
'''

from scipy.stats import ttest_1samp
import numpy as np

correct_results = 0  # Start the counter at 0

daily_visitors = np.genfromtxt("daily_visitors.csv", delimiter=",")

for i in range(1000):  # 1000 experiments
  # your ttest here:
  tstat, pval = ttest_1samp(daily_visitors[i], 30)
  # print the pvalue here:
  print(pval)
  if pval < 0.05:
    correct_results += 1  # Reject the Null Hypothesis

print
"We correctly recognized that the distribution was different in " + str(correct_results) + " out of 1000 experiments."
print
"We correctly recognized that the distribution was different in " + str(correct_results) + " out of 1000 experiments."


## 2 Sample T Test

'''
Suppose that last week, the average amount of time spent per visitor to a website was 25 minutes. This week, the average amount of time spent per visitor to a website was 28 minutes. Did the average time spent per visitor change? Or is this part of natural fluctuations?

One way of testing whether this difference is significant is by using a 2 Sample T-Test. A 2 Sample T-Test compares two sets of data, which are both approximately normally distributed.

The null hypothesis, in this case, is that the two distributions have the same mean.

We can use SciPy's ttest_ind function to perform a 2 Sample T-Test. It takes the two distributions as inputs and returns the t-statistic (which we don't use), and a p-value. If you can't remember what a p-value is, refer to the earlier exercise on univariate t-tests.
'''

from scipy.stats import ttest_ind
import numpy as np

week1 = np.genfromtxt("week1.csv",  delimiter=",")
week2 = np.genfromtxt("week2.csv",  delimiter=",")

week1_mean = np.mean(week1)
week2_mean = np.mean(week2)

print(week1_mean)
print(week2_mean)

week1_std = np.std(week1)
week2_std = np.std(week2)

print(week1_std)
print(week2_std)


tstat, pval = ttest_ind(week1, week2)
print(pval)

''' Console:
25.4480593951
29.0215681077
4.53169338708
5.49796670865
0.000676767690007

Reject Null Hypothesis, They are different
'''

## Dangers of Multiple T Tests

'''
Suppose that we own a chain of stores that sell ants, called VeryAnts. There are three different locations: A, B, and C. We want to know if the average ant sales over the past year are significantly different between the three locations.

At first, it seems that we could perform T-tests between each pair of stores.

We know that the p-value is the probability that we incorrectly reject the null hypothesis on each t-test. The more t-tests we perform, the more likely that we are to get a false positive, a Type I error.

For a p-value of 0.05, if the null hypothesis is true then the probability of obtaining a significant result is 1 – 0.05 = 0.95. When we run another t-test, the probability of still getting a correct result is 0.95 * 0.95, or 0.9025. That means our probability of making an error is now close to 10%! This error probability only gets bigger with the more t-tests we do.
'''

from scipy.stats import ttest_ind
import numpy as np

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")

a_mean = np.mean(a)
b_mean = np.mean(b)
c_mean = np.mean(c)

a_std = np.std(a)
b_std = np.std(b)
c_std = np.std(c)

print(a_mean)
print(a_std)
print(b_mean)
print(b_std)
print(c_mean)
print(c_std)

'''
console:
58.349636084
14.7537040523
65.6262871356
14.7465644902
62.3611731859
15.0924585109
'''

tstat, a_b_pval = ttest_ind(a, b)
tstat, a_c_pval = ttest_ind(a, c)
tstat, b_c_pval = ttest_ind(b, c)
print(a_b_pval)
print(a_c_pval)
print(b_c_pval)
'''
2.76676293987e-05
0.0210120516986
0.0598856352397
'''

error_prob = 1 - 0.95**3
print(error_prob)
''' 0.142625 '''


## ANOVA - Analysis of Variance

'''
In the last exercise, we saw that the probability of making a Type I error got dangerously high as we performed more t-tests.

When comparing more than two numerical datasets, the best way to preserve a Type I error probability of 0.05 is to use ANOVA. ANOVA (Analysis of Variance) tests the null hypothesis that all of the datasets have the same mean. If we reject the null hypothesis with ANOVA, we're saying that at least one of the sets has a different mean; however, it does not tell us which datasets are different.

We can use the SciPy function f_oneway to perform ANOVA on multiple datasets. It takes in each dataset as a different input and returns the t-statistic and the p-value. For example, if we were comparing scores on a videogame between math majors, writing majors, and psychology majors, we could run an ANOVA test with this line:

fstat, pval = f_oneway(scores_mathematicians, scores_writers, scores_psychologists)
The null hypothesis, in this case, is that all three populations have the same mean score on this videogame. If we reject this null hypothesis (if we get a p-value less than 0.05), we can say that we are reasonably confident that a pair of datasets is significantly different. After using only ANOVA, we can't make any conclusions on which two populations have a significant difference.

Let's look at an example of ANOVA in action.
'''
from scipy.stats import ttest_ind
from scipy.stats import f_oneway
import numpy as np

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")

fstat, pval = f_oneway(a, b, c)
print(pval)  # 0.000153411660078

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b_new.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")

fstat, pval = f_oneway(a, b, c)
print(pval)  # 8.49989098083e-215


## Assumptions of Numerical Hypothesis Tests

'''
Before we use numerical hypothesis tests, we need to be sure that the following things are true:

1. The samples should each be normally distributed...ish
Data analysts in the real world often still perform hypothesis on sets that aren't exactly normally distributed. What is more important is to recognize if there is some reason to believe that a normal distribution is especially unlikely. If your dataset is definitively not normal, the numerical hypothesis tests won't work as intended.

For example, imagine we have three datasets, each representing a day of traffic data in three different cities. Each dataset is independent, as traffic in one city should not impact traffic in another city. However, it is unlikely that each dataset is normally distributed. In fact, each dataset probably has two distinct peaks, one at the morning rush hour and one during the evening rush hour. The histogram of a day of traffic data might look something like this:

histogram

In this scenario, using a numerical hypothesis test would be inappropriate.

2. The population standard deviations of the groups should be equal
For ANOVA and 2-Sample T-Tests, using datasets with standard deviations that are significantly different from each other will often obscure the differences in group means.

To check for similarity between the standard deviations, it is normally sufficient to divide the two standard deviations and see if the ratio is "close enough" to 1. "Close enough" may differ in different contexts but generally staying within 10% should suffice.

3. The samples must be independent
When comparing two or more datasets, the values in one distribution should not affect the values in another distribution. In other words, knowing more about one distribution should not give you any information about any other distribution.

Here are some examples where it would seem the samples are not independent:

the number of goals scored per soccer player before, during, and after undergoing a rigorous training regimen
a group of patients' blood pressure levels before, during, and after the administration of a drug
It is important to understand your datasets before you begin conducting hypothesis tests on it so that you know you are choosing the right test.
'''

import codecademylib
import numpy as np
import matplotlib.pyplot as plt

dist_1 = np.genfromtxt("1.csv",  delimiter=",")
dist_2 = np.genfromtxt("2.csv",  delimiter=",")
dist_3 = np.genfromtxt("3.csv",  delimiter=",")
dist_4 = np.genfromtxt("4.csv",  delimiter=",")

#plot your histogram here
plt.figure()
plt.hist(dist_1)
plt.show()
plt.figure()
plt.hist(dist_2)
plt.show()
plt.figure()
plt.hist(dist_3)
plt.show()
plt.figure()
plt.hist(dist_4)
plt.show()

not_normal = 4

ratio = np.std(dist_2) / np.std(dist_3)
print(ratio)  # =0.58   not close enough for hypothesis testing


## Tukey's Range Test

'''
Let's say that we have performed ANOVA to compare three sets of data from the three VeryAnts stores. We received the result that there is some significant difference between datasets.

Now, we have to find out which datasets are different.

We can perform a Tukey's Range Test to determine the difference between datasets.

If we feed in three datasets, such as the sales at the VeryAnts store locations A, B, and C, Tukey's Test can tell us which pairs of locations are distinguishable from each other.

The function to perform Tukey's Range Test is pairwise_tukeyhsd, which is found in statsmodel, not scipy. We have to provide the function with one list of all of the data and a list of labels that tell the function which elements of the list are from which set. We also provide the significance level we want, which is usually 0.05.

For example, if we were looking to compare mean scores of movies that are dramas, comedies, or documentaries, we would make a call to pairwise_tukeyhsd like this:

movie_scores = np.concatenate([drama_scores, comedy_scores, documentary_scores])
labels = ['drama'] * len(drama_scores) + ['comedy'] * len(comedy_scores) + ['documentary'] * len(documentary_scores)

tukey_results = pairwise_tukeyhsd(movie_scores, labels, 0.05)
It will return a table of information, telling you whether or not to reject the null hypothesis for each pair of datasets.
'''

from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import f_oneway
import numpy as np

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")

stat, pval = f_oneway(a, b, c)
print pval

# Using our data from ANOVA, we create v and l
v = np.concatenate([a, b, c])
labels = ['a'] * len(a) + ['b'] * len(b) + ['c'] * len(c)

tukey_results = pairwise_tukeyhsd(v, labels, 0.05)
print(tukey_results)

'''
0.000153411660078
Multiple Comparison of Means - Tukey HSD,FWER=0.05
=============================================
group1 group2 meandiff  lower   upper  reject
---------------------------------------------
  a      b     7.2767   3.2266 11.3267  True 
  a      c     4.0115  -0.0385  8.0616 False 
  b      c    -3.2651  -7.3152  0.7849 False 
---------------------------------------------
'''

## Binomial Test

'''
Let's imagine that we are analyzing the percentage of customers who make a purchase after visiting a website. We have a set of 1000 customers from this month, 58 of whom made a purchase. Over the past year, the number of visitors per every 1000 who make a purchase hovers consistently at around 72. Thus, our marketing department has set our target number of purchases per 1000 visits to be 72. We would like to know if this month's number, 58, is a significant difference from that target or a result of natural fluctuations.

How do we begin comparing this, if there's no mean or standard deviation that we can use? The data is divided into two discrete categories, "made a purchase" and "did not make a purchase".

So far, we have been working with numerical datasets. The tests we have looked at, the 1- and 2-Sample T-Tests, ANOVA, and Tukey's Range test, will not work if we can't find the means of our distributions and compare them.

If we have a dataset where the entries are not numbers, but categories instead, we have to use different methods.

To analyze a dataset like this, with two different possibilities for entries, we can use a Binomial Test. A Binomial Test compares a categorical dataset to some expectation.

Examples include:

Comparing the actual percent of emails that were opened to the quarterly goals
Comparing the actual percentage of respondents who gave a certain survey response to the expected survey response
Comparing the actual number of heads from 1000 coin flips of a weighted coin to the expected number of heads
The null hypothesis, in this case, would be that there is no difference between the observed behavior and the expected behavior. If we get a p-value of less than 0.05, we can reject that hypothesis and determine that there is a difference between the observation and expectation.

SciPy has a function called binom_test, which performs a Binomial Test for you.

binom_test requires three inputs, the number of observed successes, the number of total trials, and an expected probability of success. For example, with 1000 coin flips of a fair coin, we would expect a "success rate" (the rate of getting heads), to be 0.5, and the number of trials to be 1000. Let's imagine we get 525 heads. Is the coin weighted? This function call would look like:

pval = binom_test(525, n=1000, p=0.5)
It returns a p-value, telling us how confident we can be that the sample of values was likely to occur with the specified probability. If we get a p-value less than 0.05, we can reject the null hypothesis and say that it is likely the coin is actually weighted, and that the probability of getting heads is statistically different than 0.5.
'''
from scipy.stats import binom_test


'''
Suppose the goal of VeryAnts's marketing team this quarter was to have 6% of customers click a link that was emailed to them. They sent out a link to 10,000 customers and 510 clicked the link, which comes out to 5.1% instead of 6%. Did they do significantly worse than the target? Let's use a binomial test to answer this question.

Use SciPy's binom_test function to calculate the p-value the experiment returns for this distribution, where we wanted the mean to be 6% of emails opened, or p=0.06, but only saw 5.1% of emails opened.

Store the p-value in a variable called pval and print it out.'''
pval = binom_test(510, n= 10000, p=0.06)
print(pval)

'''For the next quarter, marketing has tried out a new email tactic, including puns in every line of every email. As a result, 590 people out of 10000 opened the link in the newest email.

If we still wanted the mean to be 6% of emails opened, but now have 5.9% of emails opened, what is the new p-value. Save your results to the variable pval2

Does this new p-value make sense?'''
pval2 = binom_test(590, n= 10000, p=0.06)
print(pval2)

## Chi-Square Test

'''In the last exercise, we looked at data where customers visited a website and either made a purchase or did not make a purchase. What if we also wanted to track if visitors added any items to their shopping cart? With three discrete categories of data per dataset, we can no longer use a Binomial Test. If we have two or more categorical datasets that we want to compare, we should use a Chi Square test. It is useful in situations like:

An A/B test where half of users were shown a green submit button and the other half were shown a purple submit button. Was one group more likely to click the submit button?
Men and women were both given a survey asking "Which of the following three products is your favorite?" Did the men and women have significantly different preferences?
In SciPy, you can use the function chi2_contingency to perform a Chi Square test.

The input to chi2_contingency is a contingency table where:

The columns are each a different condition, such as men vs. women or Interface A vs. Interface B
The rows represent different outcomes, like "Survey Response A" vs. "Survey Response B" or "Clicked a Link" vs. "Didn't Click"
This table can have as many rows and columns as you need.

In this case, the null hypothesis is that there's no significant difference between the datasets. We reject that hypothesis, and state that there is a significant difference between two of the datasets if we get a p-value less than 0.05.
'''

from scipy.stats import chi2_contingency

# Contingency table
#         harvester |  leaf cutter
# ----+------------------+------------
# 1st gr | 30       |  10
# 2nd gr | 35       |  5
# 3rd gr | 28       |  12

'''The management at the VeryAnts ant store wants to know if their two most popular species of ants, the Leaf Cutter and the Harvester, vary in popularity between 1st, 2nd, and 3rd graders.

We have created a table representing the different ants bought by the children in grades 1, 2, and 3 after the last big field trip to VeryAnts. Run the code to see what happens when we enter this table into SciPy's chi-square test.

Does the resulting p-value mean that we should reject or accept the null hypothesis?'''
X = [[30, 10],
     [35, 5],
     [28, 12],
    [20, 20]]
chi2, pval, dof, expected = chi2_contingency(X)
print pval  # 0.155082308077  , accept null hypothesis

'''A class of 40 4th graders comes into VeryAnts in the next week and buys 20 sets of Leaf Cutter ants and 20 sets of Harvester ants.

Add this data to the contingency table, rerun the chi-square test, and see if there is now a low enough value to reject the null hypothesis.'''

# 0.00281283455955  reject null hypothesis

