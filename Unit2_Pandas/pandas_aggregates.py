'''
General Caluclations Syntax

df.column_name.command()


Command	Description
mean	Average of all values in column
std	Standard deviation
median	Median
max	Maximum value in column
min	Minimum value in column
count	Number of values in column
nunique	Number of unique values in column
unique	List of unique values in column

'''

## calculating column statistics
import pandas as pd

orders = pd.read_csv('orders.csv')

print(orders.head(10))

most_expensive = orders.price.max()
print(most_expensive)

num_colors = orders.shoe_color.nunique()
print(num_colors)

## Calculating Aggregate Functions I

'''
df.groupby('column1').column2.measurement()

where:

column1 is the column that we want to group by ('student' in our example)
column2 is the column that we want to perform a measurement on (grade in our example)
measurement is the measurement function we want to apply (mean in our example)


Generally, you'll always see a groupby statement followed by reset_index:

df.groupby('column1').column2.measurement()
    .reset_index()

'''

import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders.head(5))

pricey_shoes = orders.groupby('shoe_type').price.max()
print(pricey_shoes)

print(type(pricey_shoes))  # yields a series


## Calculating Aggregate Functions II

import pandas as pd

orders = pd.read_csv('orders.csv')

pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()

print(pricey_shoes)

print(type(pricey_shoes))  # yields a data frame


## Calculating Aggregate Functions III

'''
If we want to calculate the 75th percentile (i.e., the point at which 75% of employees have a lower wage and 25% have a higher wage) for each category, we can use the following combination of apply and a lambda function:

# np.percentile can calculate any percentile over an array of values
high_earners = df.groupby('category').wage
    .apply(lambda x: np.percentile(x, 75))
    .reset_index()
'''

import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')


cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x : np.percentile(x, 25)).reset_index()

print(cheap_shoes)

##  Calculating Aggregate Functions IV

import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')
#print(orders.head(5))
shoe_counts = orders.groupby(['shoe_type', 'shoe_color'])['id'].count().reset_index()

print(shoe_counts)



## Pivot Tables

'''
Reorganizing a table in this way is called pivoting. The new table is called a pivot table.

In Pandas, the command for pivot is:

df.pivot(columns='ColumnToPivot',
         index='ColumnToBeRows',
         values='ColumnToBeValues')
For our specific example, we would write the command like this:

# First use the groupby statement:
unpivoted = df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()
# Now pivot the table
pivoted = unpivoted.pivot(
    columns='Day of Week',
    index='Location',
    values='Total Sales')
Just like with groupby, the output of a pivot command is a new DataFrame, but the indexing tends to be "weird", so we usually follow up with .reset_index().
'''

import numpy as np
import pandas as pd

orders = pd.read_csv('orders.csv')

shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()

print(shoe_counts)

shoe_counts_pivot = shoe_counts.pivot(columns='shoe_color', index = 'shoe_type', values = 'id').reset_index()

print(shoe_counts_pivot)



## Final Review

import pandas as pd

user_visits = pd.read_csv('page_visits.csv')

print(user_visits.head(5))

click_source = user_visits.groupby('utm_source').id.count().reset_index()

print(click_source)

click_source_by_month = user_visits.groupby(['utm_source', 'month'])['id'].count().reset_index()

print(click_source_by_month)

click_source_by_month_pivot = click_source_by_month.pivot(columns = 'month', index = 'utm_source', values = 'id').reset_index()

print(click_source_by_month_pivot)

