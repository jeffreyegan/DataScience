## Load Tables

import pandas as pd

orders = pd.read_csv('orders.csv')

products = pd.read_csv('products.csv')

customers = pd.read_csv('customers.csv')

print(orders)
print(products)
print(customers)


## Inner Merge

'''
The .merge method looks for columns that are common between two DataFrames and then looks for rows where those column's values are the same. 
It then combines the matching rows into a single row in a new table.
'''

import pandas as pd

sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

sales_vs_targets = pd.merge(sales, targets)
print(sales_vs_targets)

crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]
print(crushing_it)

'''
In addition to using pd.merge, each DataFrame has its own merge method. For instance, if you wanted to merge orders with customers, you could use:

new_df = orders.merge(customers)
This produces the same DataFrame as if we had called pd.merge(orders, customers).

We generally use this when we are joining more than two DataFrames together because we can "chain" the commands. The following command would merge orders to customers, and then the resulting DataFrame to products:

big_df = orders.merge(customers)\
    .merge(products)
'''

import pandas as pd

sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

men_women = pd.read_csv('men_women_sales.csv')
print(men_women.head(5))

all_data = targets.merge(sales).merge(men_women)

print(all_data)

results = all_data[(all_data.target < all_data.revenue) & (all_data.women > all_data.men)]
print(results)


## Merge on Specific Columns

'''
In the previous example, the merge function "knew" how to combine tables based on the columns that were the same between two tables. For instance, products and orders both had a column called product_id. This won't always be true when we want to perform a merge.

Generally, the products and customers DataFrames would not have the columns product_id or customer_id. Instead, they would both be called id and it would be implied that the id was the product_id for the products table and customer_id for the customers table.

How would this affect our merges?

Because the id columns would mean something different in each table, our default merges would be wrong.

One way that we could address this problem is to use .rename to rename the columns for our merges. In the example below, we will rename the column id to customer_id, so that orders and customers have a common column for the merge.

pd.merge(
    orders,
    customers.rename(columns={'id': 'customer_id'}))

'''

import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)

orders_products = pd.merge(orders,products.rename(columns={'id': 'product_id'}))

print(orders_products)


'''
In the previous exercise, we learned how to use rename to merge two DataFrames whose columns don't match.

If we don't want to do that, we have another option. We could use the keywords left_on and right_on to specify which columns we want to perform the merge on. In the example below, the "left" table is the one that comes first (orders), and the "right" table is the one that comes second (customers). This syntax says that we should match the customer_id from orders to the id in customers.

pd.merge(
    orders,
    customers,
    left_on='customer_id',
    right_on='id')
If we use this syntax, we'll end up with two columns called id, one from the first table and one from the second. Pandas won't let you have two columns with the same name, so it will change them to id_x and id_y.

The new column names id_x and id_y aren't very helpful for us when we read the table. We can help make them more useful by using the keyword suffixes. We can provide a list of suffixes to use instead of "_x" and "_y".

For example, we could use the following code to make the suffixes reflect the table names:

pd.merge(
    orders,
    customers,
    left_on='customer_id',
    right_on='id',
    suffixes=['_order', '_customer']
)

'''

import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)

orders_products = pd.merge(orders,products,left_on='product_id',right_on='id',suffixes=['_orders', '_products'])

print(orders_products)


## Mismatched Merges

import pandas as pd

orders = pd.read_csv('orders.csv')
products = pd.read_csv('products.csv')
print(orders)
print(products)

merged_df = pd.merge(orders, products)
print(merged_df)

# Order without accompanying product data gets dropped from merge


## Outer Merge

'''
In the previous exercise, we saw that when we merge two DataFrames whose rows don't match perfectly, we lose the unmatched rows.

This type of merge (where we only include matching rows) is called an inner merge. There are other types of merges that we can use when we want to keep information from the unmatched rows.

pd.merge(company_a, company_b, how='outer')

'''

import pandas as pd

store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)

store_a_b_outer = pd.merge(store_a, store_b, how='outer')
print(store_a_b_outer)


## Left and Right Merge

'''
A Left Merge includes all rows from the first (left) table, but only rows from the second (right) table that match the first table.

or this command, the order of the arguments matters. If the first DataFrame is company_a and we do a left join, we'll only end up with rows that appear in company_a.

By listing company_a first, we get all customers from Company A, and only customers from Company B who are also customers of Company A.

pd.merge(company_a, company_b, how='left')


Right merge is the exact opposite of left merge. Here, the merged table will include all rows from the second (right) table, but only rows from the first (left) table that match the second table.

By listing company_a first and company_b second, we get all customers from Company B, and only customers from Company A who are also customers of Company B.

pd.merge(company_a, company_b, how="right")

'''

import pandas as pd

store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)

store_a_b_left = pd.merge(store_a, store_b, how='left')
print(store_a_b_left)


store_b_a_left = pd.merge(store_b, store_a, how='left')
print(store_b_a_left)

# Store B carries rakes, shovels, and wooden dowels while A does not

# Store A carries screws, screwdrivers, and wrenches while B does not.

# The rest of their inventory is common



## Concatenate Data Frames

'''
Sometimes, a dataset is broken into multiple tables. For instance, data is often split into multiple CSV files so that each download is smaller.

When we need to reconstruct a single DataFrame from multiple smaller DataFrames, we can use the method pd.concat([df1, df2, df2, ...]). 

This method only works if all of the columns are the same in all of the DataFrames.
'''

import pandas as pd

bakery = pd.read_csv('bakery.csv')
print(bakery)
ice_cream = pd.read_csv('ice_cream.csv')
print(ice_cream)

menu = pd.concat([bakery, ice_cream])
print(menu)



## Review


'''
This lesson introduced some methods for combining multiple DataFrames:

Creating a DataFrame made by matching the common columns of two DataFrames is called a merge
We can specify which columns should be matches by using the keyword arguments left_on and right_on
We can combine DataFrames whose rows don't all match using left, right, and outer merges and the how keyword argument
We can stack or concatenate DataFrames with the same columns using pd.concat

'''

import pandas as pd

visits = pd.read_csv('visits.csv',
                        parse_dates=[1])
checkouts = pd.read_csv('checkouts.csv',
                        parse_dates=[1])

print(visits.head(10))
print(checkouts.head(10))

v_to_c = pd.merge(visits,checkouts)


v_to_c['time'] = v_to_c.checkout_time - v_to_c.visit_time
print(v_to_c.head(10))

# Mean Time Between Visiting Landing page and checking out
print('Mean time to checkout: '+ str(v_to_c.time.mean()))