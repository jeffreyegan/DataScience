'''
LEARN PANDAS: AGGREGATES
A/B Testing for ShoeFly.com
Our favorite online shoe store, ShoeFly.com is performing an A/B Test. They have two different versions of an ad, which they have placed in emails, as well as in banner ads on Facebook, Twitter, and Google. They want to know how the two ads are performing on each of the different platforms on each day of the week. Help them analyze the data using aggregate measures.

Mark the tasks as complete by checking them off
Analyzing Ad Sources
1.
Examine the first few rows of ad_clicks.


2.
Your manager wants to know which ad platform is getting you the most views.

How many views (i.e., rows of the table) came from each utm_source?


3.
If the column ad_click_timestamp is not null, then someone actually clicked on the ad that was displayed.

Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise.

Try using the following code:

ad_clicks['is_click'] = ~ad_clicks\
   .ad_click_timestamp.isnull()
The ~ is a NOT operator, and isnull() tests whether or not the value of ad_click_timestamp is null.

4.
We want to know the percent of people who clicked on ads from each utm_source.

Start by grouping by utm_source and is_click and counting the number of user_id's in each of those groups. Save your answer to the variable clicks_by_source.


5.
Now let's pivot the data so that the columns are is_click (either True or False), the index is utm_source, and the values are user_id.

Save your results to the variable clicks_pivot.


6.
Create a new column in clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source.

Was there a difference in click rates for each source?

Try the following code:

clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] +
    clicks_pivot[False])
clicks_pivot[True] is the number of people who clicked (because is_click was True for those users)

clicks_pivot[False] is the number of people who did not click (because is_click was False for those users)

So, the percent of people who clicked would be (Total Who Clicked) / (Total Who Clicked + Total Who Did Not Click)

Analyzing an A/B Test
7.
The column experimental_group tells us whether the user was shown Ad A or Ad B.

Were approximately the same number of people shown both adds?

We can group by experimental_group and count the number of users.

8.
Using the column is_click that we defined earlier, check to see if a greater percentage of users clicked on Ad A or Ad B.

Group by both experimental_group and is_click and count the number of user_id's.

You might want to use a pivot table like we did for the utm_source exercises.

9.
The Product Manager for the A/B test thinks that the clicks might have changed by day of the week.

Start by creating two DataFrames: a_clicks and b_clicks, which contain only the results for A group and B group, respectively.


10.
For each group (a_clicks and b_clicks), calculate the percent of users who clicked on the ad by day.

First, group by is_click and day. Next, pivot the data so that the columns are based on is_click. Finally, calculate the percent of people who clicked on the ad.

11.
Compare the results for A and B. What happened over the course of the week?

Do you recommend that your company use Ad A or Ad B?

'''

import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head(10))

# How Many Views from Each UTM Source?
views = ad_clicks.groupby('utm_source').count().reset_index()
print(views)

# New Column, True if ad_click time not null
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
#print(ad_clicks.head(10))

# Percent of People that Clicked on Ads from Each Source
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

# Pivot Data: cols = is_click, rows/index = utm src
clicks_pivot = clicks_by_source.pivot(columns='is_click', index = 'utm_source', values = 'user_id').reset_index()

'''
The solution calls for the Column headers in this case True/False to remain as is, and not encapsulated within quotation marks:
'''

# This Works
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])*100

#This Does Not
'''
clicks_pivot['percent_clicked'] = clicks_pivot['True'] / (clicks_pivot['True'] + clicks_pivot['False'])*100

Why is this the case in this example where the prevailing syntax elsewhere (even the assignment of the new column created in this line of code) has the column name in quotes? In this case I would also expect the True and False headers to be strings, not booleans. If they are Booleans, how does that make sense?
'''
print(clicks_pivot)


# Following Shows that Ad A and Ad B each were presented 827 times
experimental = ad_clicks.groupby('experimental_group').count().reset_index()
print(experimental)

experimental_clicks = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
print(experimental_clicks)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
#print(a_clicks.head(10))

a_clicks_by_day = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
b_clicks_by_day = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
#print(a_clicks_by_day)

a_clicks_by_day_p = a_clicks_by_day.pivot(columns = 'is_click', index = 'day', values = 'user_id').reset_index()
b_clicks_by_day_p = b_clicks_by_day.pivot(columns = 'is_click', index = 'day', values = 'user_id').reset_index()

a_clicks_by_day_p['percent_clicked'] = a_clicks_by_day_p[True] / (a_clicks_by_day_p[True] + a_clicks_by_day_p[False])*100
b_clicks_by_day_p['percent_clicked'] = b_clicks_by_day_p[True] / (b_clicks_by_day_p[True] + b_clicks_by_day_p[False])*100

print(a_clicks_by_day_p)
print(b_clicks_by_day_p)

# Advertisement B has slightly more success on Tuesdays than Advert A but in general, Advert A has the better conversion rate.
