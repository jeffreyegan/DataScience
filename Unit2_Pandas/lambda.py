'''Create a lambda function named contains_a that takes an input word and returns True if the input contains the letter 'a'. Otherwise, return False.'''

#Write your lambda function here
contains_a = lambda word : 'a' in word
print(contains_a("banana"))
print(contains_a("apple"))
print(contains_a("cherry"))


#Write your lambda function here
long_string = lambda str : len(str)>12

print(long_string("short"))
print(long_string("photosynthesis"))

#Write your lambda function here
ends_in_a = lambda str : 'a' == str[-1]

print(ends_in_a("data"))
print(ends_in_a("aardvark"))

#Write your lambda function here
double_or_zero = lambda num : num*2 if num > 10 else 0
print(double_or_zero(15))
print(double_or_zero(5))

#Write your lambda function here
even_or_odd = lambda num : 'even' if num%2 == 0 else 'odd'

print(even_or_odd(10))
print(even_or_odd(5))

#Write your lambda function here
multiple_of_three = lambda num : 'multiple of three' if num%3 == 0 else 'not a multiple'
print(multiple_of_three(9))
print(multiple_of_three(10))

#Write your lambda function here
rate_movie = lambda rating : "I liked this movie" if rating > 8.5 else "This movie was not very good"

print(rate_movie(9.2))
print(rate_movie(7.2))

#Write your lambda function here
ones_place = lambda num : num%10

print(ones_place(123))
print(ones_place(4))


#Write your lambda function here
double_square = lambda num : 2*num**2

print(double_square(5))
print(double_square(3))


import random
#Write your lambda function here
add_random = lambda num : random.randint(1,10)+num

print(add_random(5))
print(add_random(100))


# More Lambda

mylambda = lambda string : string[0]+string[-1]

print(mylambda('This is a string'))
# should print 'Tg'





mylambda = lambda age : "Welcome to BattleCity!" if age > 12 else "You must be over 13"

print(mylambda(11))
print(mylambda(22))


## Pandas with Lambda Functions

import pandas as pd

df = pd.read_csv('employees.csv')

get_last_name = lambda name : name.split(' ')[-1]
# Add columns here
df['last_name'] = df.name.apply(lambda name : name.split(' ')[-1])
print(df)


## Applying Lambda to a Row
import pandas as pd

df = pd.read_csv('employees.csv')


total_earned = lambda row : (row.hours_worked-40)*(1.5*row.hourly_wage) + 40 * row.hourly_wage if row.hours_worked > 40 else row.hours_worked * row.hourly_wage

df['total_earned'] = df.apply(lambda row : (row.hours_worked-40)*(1.5*row.hourly_wage) + 40 * row.hourly_wage if row.hours_worked > 40 else row.hours_worked * row.hourly_wage, axis=1)

print(df.head())


# Review Pandas
import pandas as pd

orders = pd.read_csv('shoefly.csv')


orders['shoe_source'] = orders.shoe_material.apply(lambda shoe_material : 'animal' if shoe_material == 'leather' else 'vegan')

orders['salutation'] = 'Dear '+ orders.gender.apply(lambda gender : 'Mr. ' if gender == 'male' else 'Ms. ') + orders.last_name

print(orders.head(5))