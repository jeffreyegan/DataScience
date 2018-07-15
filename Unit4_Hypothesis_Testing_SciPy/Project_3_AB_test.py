'''
A/B Testing at Nosh Mish Mosh
The Nosh Mish Mosh is a recipe and ingredient meal delivery service. We ship the raw materials and you get to cook it at your home!
We've decided to hire a data analyst to help them make product and interface decisions.
Get started and we'll be able to judge the amount of data we'll need for these differences to be meaningful.

Nosh Mish Mosh: An Assortment of Edible Aliments
1.
We've collected customer data for the past week and exposed it through a Python library, so first import noshmishmosh.


2.
Next, we'll need to do a little bit of data analysis — let's use numpy to help. Import numpy into your workspace.


A/B Testing at Nosh Mish Mosh
3.
Nosh Mish Mosh wants to run an experiment to see if we can convince more people to purchase meal plans if we use a more artisanal-looking vegetable selection. We've photographed these modern meals with blush tomatoes and graffiti eggplants, but aren't sure if this strategy will sell enough units to benefit from establishing a business relationship with a new provider.

Before running this experiment, of course, we need to know how many people have to see the new assets. We don't want customers seeing food that we won't end up offering. Of course, there are three things we need to know before we determine that number.

the Baseline
the Minimum Detectable Effect
and the Statistical Significance
4.
Let's get the ball rolling on finding those numbers! In order to get our baseline, we need to first know how many users visited the site. Let's grab that logged information, which is stored in noshmishmosh.customer_visits. Assign that to a new variable called all_visitors.

5.
Next we need to know how many visitors to the site ultimately end up buying a meal or set of meals from Nosh Mish Mosh. We have that information saved into purchasing_customers field on noshmishmosh. Save that information into a variable called paying_visitors.

6.
Calculate the lengths of the two lists, saving the results into variables called total_visitor_count and paying_visitor_count, respectively.


7.
Now to get the baseline: since we want a percentage as our answer, multiply the number of purchasing visitors by 100.0. Then divide that by the number of total visitors. Save the result in a variable called baseline_percent.

8.
Print out the baseline_percent so we know what to use for our baseline percentage in the A/B Sample Size Calculator.

Mish Mosh B'Gosh: the Minimum Detectable Effect
9.
These rainbow fingerling potatoes don't come cheap. We'd like to know for sure that we'll be pulling in at least $1240 more every week. In order to figure out how many more customers we need we'll have to investigate the average revenue generated from a given sale. Luckily we have a list of the money spent by each customer in noshmishmosh.money_spent. Save that list into a variable called payment_history.

10.
We need to find how many typical purchases it would take to reach $1240 in additional revenue using our historical data.

Let's start with computing the average payment per paying customer using np.mean, saving it as average_payment.


11.
We want to know how many of these "usual" payments it would take to clear our $1240 mark. Round the number up using np.ceil (because that's how many new customers it takes to bring in more than $1240). Save that value into a new_customers_needed variable.


12.
Now find the percent lift required by multiplying the number of customers by 100.0 and dividing the result by the total visitor count ascertained earlier. Save the result in a variable called percentage_point_increase. Print percentage_point_increase to see what it is.

percentage_point_increase = (new_customers_needed * 100.0) / total_visitor_count
13.
In order to find our minimum detectable effect, we need to express percentage_point_increase as a percent of baseline_percent. You can do this by dividing percentage_point_increase by baseline_percent and multiplying by 100.0.

Store the results in a variable called minimum_detectable_effect.


14.
Print out the result minimum_detectable_effect.

Nosh Mish Mosh: Tying It All Together
15.
The last thing we need to calculate the sample size for Nosh Mish Mosh's artisanal rebranding is our statistical significance. We'd like to be fairly certain, but this isn't going to be a million dollar decision, so let's go with 90%.

16.
Now put it all together! Puch the baseline, the minimum detectable effect, and the statistical significance into the calculator and evaluate how many people need to be shown the new assets before we can check if the results are a significant improvement. Save the results in a variable called ab_sample_size.


'''

import noshmishmosh
import numpy as np

all_visitors = noshmishmosh.customer_visits
paying_customers = noshmishmosh.purchasing_customers
total_visitor_count = np.size(all_visitors)
paying_visitor_count = np.size(paying_customers)

baseline_percent = 100.0*paying_visitor_count / total_visitor_count
print(baseline_percent)  # 18.6%

payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)
print(average_payment)  # $26.54
new_customers_needed = np.ceil(1240.0 / average_payment)
print(new_customers_needed)  # 47 new customers

percentage_point_increase  = 100.0 * new_customers_needed / total_visitor_count
print(percentage_point_increase)  # 9.4%


minimum_detectable_effect = 100.0 * percentage_point_increase / baseline_percent
print(minimum_detectable_effect)  # 50.53

ab_sample_size = 290  #90% confident at https://s3.amazonaws.com/codecademy-content/courses/learn-hypothesis-testing/a_b_sample_size/index.html


