'''
Page Visits Funnel
In this project, you’ll be analyzing data for Cool T-Shirts Inc. Your job is to build a funnel, which is a description of how many people continue to the next step of a multi-step process.
This funnel will describe how users move through their website and eventually purchase a t-shirt. You’ll use merges in Pandas to create this funnel from multiple tables.



Cool T-Shirts Inc. has asked you to analyze data on visits to their website. Your job is to build a funnel, which is a description of how many people continue to the next step of a multi-step process.

In this case, our funnel is going to describe the following process:

A user visits CoolTShirts.com
A user adds a t-shirt to their cart
A user clicks "checkout"
A user actually purchases a t-shirt
'''

import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head(2))
print(cart.head(2))
print(checkout.head(2))
print(purchase.head(2))

v_to_c = pd.merge(visits,cart,how='left')
print(v_to_c.head(2))
print(len(v_to_c))  # num visits
print(len(v_to_c[v_to_c.cart_time.isnull()]))  # visits w/o cart

perc_v_to_c = str(float(len(v_to_c[v_to_c.cart_time.isnull()])) / float(len(v_to_c))*100)
print(perc_v_to_c+'% of Visitors Did Not Put Items in their Cart')

c_to_x = pd.merge(cart,checkout,how='left')
print(len(c_to_x))  # num put in cart
print(len(c_to_x[c_to_x.checkout_time.isnull()]))  # cart w/o checkout
perc_c_to_x = str(float(len(c_to_x[c_to_x.checkout_time.isnull()])) / float(len(c_to_x))*100)
print(perc_c_to_x+'% of Visitors With Items in their Cart Did Not Checkout')


all_data = visits.merge(cart,how='left').merge(checkout,how='left').merge(purchase,how='left')
print(all_data.head(2))

# What % of users proceeded to checkout but did not purchase a shirt?

# Number of Checkouts without Purchases
n1 = all_data[(~all_data.checkout_time.isnull()) & (all_data.purchase_time.isnull())].count()

#Number of Checkouts with Purchases
n2 = all_data[(~all_data.checkout_time.isnull()) & (~all_data.purchase_time.isnull())].count()

#Number of Checkouts with & without Purchases
n3 = all_data[(~all_data.checkout_time.isnull())].count()

fail_x_to_p = float(n1.checkout_time)/float(n3.checkout_time)*100

print(str(fail_x_to_p)+'% of users proceeded to checkout but failed to purchase.')


conversion = all_data[(~all_data.visit_time.isnull())].count().reset_index()
conversion.rename(columns={0:'num_users'}, inplace = True)

conversion['delta'] = conversion.num_users.diff()

conversion['percent_converted'] = conversion.num_users / (conversion.num_users - conversion.delta)*100


print(conversion)

print('The weakest step of the funnel is clearly the disconnection where visitors to the site do not put something in their cart. Work must be done to motivate people to put things in their cart.')

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

#print(all_data.time_to_purchase)

print('Average time to purchase: ' + str(all_data.time_to_purchase.mean()))