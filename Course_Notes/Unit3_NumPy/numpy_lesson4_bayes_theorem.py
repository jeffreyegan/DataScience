## Independent Events

## Conditional Probability
'''
Conditional probability is the probability that two events happen. It's easiest to calculate conditional probability when the two events are independent.

Note: For the rest of this lesson, we'll be using the statistical convention that the probability of an event is written as P(event).

If the probability of Event A is P(A) and the probability of Event B is P(B) and the two events are independent, then the probability of both events occurring is the product of the probabilities:

P(A ∩ B) = P(A) × P(B)
(The symbol ∩ just means "and", so P(A ∩ B) means probability that both A and B happen)

For instance, suppose we are rolling a pair of dice, and want to know the probability of rolling two sixes. Each die has six sides, so the probability of rolling a six is 1/6. Each die is independent (i.e., rolling one six does not increase or decrease our chance of rolling a second six), so

P(6 ∩ 6) = P(6) × P(6) = 1/6 × 1/6 = 1/36
'''

import numpy as np

p_disease_and_correct = 0.99 * 1.0/100000
print(p_disease_and_correct)

p_no_disease_and_incorrect = 0.01 * (100000.0-1.0)/100000.0
print(p_no_disease_and_incorrect)


## Bayes' Theorem

'''
In the previous exercise, we determined two probabilities:

The patient had the disease, and the test correctly diagnosed the disease ≈ 0.00001
The patient didn't have the disease and the test incorrectly diagnosed that they had the disease ≈ 0.01
Both events are rare, but we can see that it was about 1,000 times more likely than the test was incorrect than that the patient had this rare disease.

We're able to come to this conclusion because we had more information than just the accuracy of the test; we also knew the prevalence of this disease. That extra information about how we expect the world to work is called a prior.

When we only use the first piece of information (the result of the test), it's called a Frequentist Approach to statistics. When we incorporate our prior, it's called a Bayesian Approach.

In statistics, if we have two events (A and B), we write the probability that event A will happen, given that event B already happened as P(A|B). In our example, we want to find P(rare disease | positive result).

We can calculate P(A|B) using Bayes' Theorem, which states:

P(A|B) = ( P(B|A) * P(A) ) / P(B)

'''

'''
Calculate P(positive result | rare disease), or the probability of a positive test result, given that a patient really has this rare disease. Save your answer (as a decimal) to p_positive_given_disease.
'''


'''
Calculate P(positive result | rare disease), or the probability of a positive test result, given that a patient really has this rare disease. Save your answer (as a decimal) to p_positive_given_disease.

The test is 99% accurate.

2.
What is P(rare disease), the probability that a randomly selected patient has the rare disease? Save your answer to p_disease.


3.
As we discussed previously, there are two ways to get a positive result:

The patient had the disease, and the test correctly diagnosed the disease
The patient didn't have the disease and the test incorrectly diagnosed that they had the disease.
Using these two probabilities, calculate the total probability that a randomly selected patient receives a positive test result, P(positive result). Save your answer to the variable p_positive.


4.
Substitute all three of these values into Bayes' Theorem and calculate P(rare disease | positive result). Save your result as p_disease_given_positive.

5.
Print p_disease_given_positive.

Is it likely that your patient has this disease?
'''

import numpy as np

p_positive_given_disease = (0.99 * (.00001))/ (1./100000.)
print(p_positive_given_disease)

p_disease = 1./100000.
print(p_disease)

p_positive = (0.00001) + (0.01)
print(p_positive)

p_disease_given_positive = (p_positive_given_disease) * (p_disease) / (p_positive)

print(p_disease_given_positive)


# Spam Filters - Bayes in Action

'''
Let's explore a different example. Email Spam filters use Bayes Theorem to determine if certain words indicate that an email is spam.

Let's a take word that often appears in spam: "enhancement". With just 3 facts, we can make some preliminary steps towards a good spam filter:

"enhancement" appears in just 0.1% of non-spam emails
"enhancement" appears in 5% of spam emails
Spam emails make up about 20% of total emails
Given that an email contains "enhancement", what is the probability that the email is spam?
'''

import numpy as np

a = 'spam'
b = 'enhancement'

p_spam = 0.2
p_enhancement_given_spam = 0.05
p_enhancement = 0.05 * 0.2 + 0.001 * (1 - 0.2)
p_spam_enhancement = p_enhancement_given_spam * p_spam / p_enhancement

print(p_spam_enhancement)

## Review

'''
In this course, we learned several new definitions:

Two events are independent if the occurrence of one event does not affect the probability of the second event
If two events are independent then, 
P(A ∩ B) = P(A) × P(B)
A prior is an additional piece of information that tells us how likely an event is
A frequentist approach to statistics does not incorporate a prior
A Bayesian approach to statistics incorporates prior knowledge
Bayes' Theorem is

'''