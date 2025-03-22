## Petal Power Project
import pandas as pd

# Import CSV
inventory = pd.read_csv('inventory.csv')

# Inspect first 10 rows of Inventory
print(inventory.head(10))

# Select Staten Island Rows
staten_island = inventory[inventory.location == 'Staten Island']
#print(staten_island)


# Product Request at Staten Island Location
product_request = staten_island.product_description
#print(product_request)


# Customer wants seeds in Brooklyn
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
#print(seed_request)


# Add In_Stock Bool for Inventory Items with Qty > 0
inventory['in_stock'] = inventory.quantity.apply(lambda quantity : True if quantity > 0 else False)


# Value of Inventory
inventory['total_value'] = inventory['price'] * inventory['quantity']


# Uncluse this lambda function
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)


# Create new column in inventory called full_description with above lambda function
inventory['full_description'] = inventory.apply(lambda row : '{} - {}'.format(row.product_type, row.product_description), axis =1)

print(inventory.head(10))

