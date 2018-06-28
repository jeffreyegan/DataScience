# Mean

import numpy as np

store_one = np.array([2, 5, 8, 3, 4, 10, 15, 5])
store_two = np.array([3, 17, 18,  9,  2, 14, 10])
store_three = np.array([7, 5, 4, 3, 2, 7, 7])



store_one_avg = np.mean(store_one)
print(store_one_avg)
store_two_avg = np.mean(store_two)
print(store_two_avg)
store_three_avg = np.mean(store_three)
print(store_three_avg)

best_seller = store_two

## Mean as Logical Operator

'''
>>> np.mean(survey_array > 8)
0.2
The logical statement survey_array > 8 evaluates which survey answers were greater than 8, and assigns them a value of 1. 
np.mean adds all of the 1s up and divides them by the length of survey_array. 
The resulting output tells us that 20% of responders purchased more than 8 pounds of produce.
'''

import numpy as np

class_year = np.array([1967, 1949, 2004, 1997, 1953, 1950, 1958, 1974, 1987, 2006, 2013, 1978, 1951, 1998, 1996, 1952, 2005, 2007, 2003, 1955, 1963, 1978, 2001, 2012, 2014, 1948, 1970, 2011, 1962, 1966, 1978, 1988, 2006, 1971, 1994, 1978, 1977, 1960, 2008, 1965, 1990, 2011, 1962, 1995, 2004, 1991, 1952, 2013, 1983, 1955, 1957, 1947, 1994, 1978, 1957, 2016, 1969, 1996, 1958, 1994, 1958, 2008, 1988, 1977, 1991, 1997, 2009, 1976, 1999, 1975, 1949, 1985, 2001, 1952, 1953, 1949, 2015, 2006, 1996, 2015, 2009, 1949, 2004, 2010, 2011, 2001, 1998, 1967, 1994, 1966, 1994, 1986, 1963, 1954, 1963, 1987, 1992, 2008, 1979, 1987])


millennials = np.mean(class_year >= 2005)
print(millennials)


## Mean of 2D Arrays

'''
If we have a two-dimensional array, np.mean can calculate the means of the larger array as well as the interior values.

Let's imagine a game of ring toss at a carnival. In this game, you have three different chances to get all three rings onto a stick. In our ring_toss array, each interior array (the arrays within the larger array) is one try, and each number is one ring toss. 1 represents a successful toss, 0 represents a fail.

First, we can use np.mean to find the mean across all the arrays:

>>> ring_toss = np.array([[1, 0, 0], 
                          [0, 0, 1], 
                          [1, 0, 1]])
>>> np.mean(ring_toss)
0.44444444444444442
To find the means of each interior array, we specify axis 1 (the "rows"):

>>> np.mean(ring_toss, axis=1)
array([ 0.33333333,  0.33333333,  0.66666667])
To find the means of each index position (i.e, mean of all 1st tosses, mean of all 2nd tosses, ...), we specifiy axis 0 (the "columns"):

>>> np.mean(ring_toss, axis=0)
array([ 0.66666667,  0.        ,  0.66666667])
'''

import numpy as np

allergy_trials = np.array([[6, 1, 3, 8, 2],
                           [2, 6, 3, 9, 8],
                           [5, 2, 6, 9, 9]])

total_mean = np.mean(allergy_trials)
print(total_mean)

trial_mean = np.mean(allergy_trials, axis = 1)
patient_mean = np.mean(allergy_trials, axis = 0)
print(trial_mean)
print(patient_mean)


## Outliers

'''
As we can see, the mean is a helpful way to quickly understand different parts of our data. However, the mean is highly influenced by the specific values in our data set. What happens when one of those values is significantly different from the rest?

Values that don’t fit within the majority of a dataset are known as outliers. It’s important to identify outliers because if they go unnoticed, they can skew our data and lead to error in our analysis (like determining the mean). They can also be useful in pointing out errors in our data collection.

When we're able to identify outliers, we can then determine if they were due to an error in sample collection or whether or not they represent a significant but real deviation from the mean.

Suppose we want to determine the average height for 3rd graders. We measure several students at the local school, but accidentally measure one student in centimeters rather than in inches. If we're not paying attention, our dataset could end up looking like this:

[50, 50, 51, 49, 48, 127]
In this case, 127 would be an outlier.

Some outliers aren’t the result of a mistake. For instance, suppose that one of our 3rd graders had skipped a grade and was actually a year younger than everyone else in the class:

[50, 50, 51, 49, 48, 45]
She might be significantly shorter at 45", but her height would still be an outlier.

Suppose that another student was just unusually tall for his age:

[50, 50, 51, 49, 48, 58.5]
His height of 58.5" would also be an outlier.
'''

## Sorting and Outliers

'''
One way to quickly identify outliers is by sorting our data, Once our data is sorted, we can quickly glance at the beginning or end of an array to see if some values lie far beyond the expected range. We can use the NumPy function np.sort to sort our data.

Let’s go back to our 3rd grade height example, and imagine an 8th grader walked into our experiement:

>>> heights = np.array([49.7, 46.9, 62, 47.2, 47, 48.3, 48.7])
If we use np.sort, we can immediately identify the taller student since their height (62") is noticeably outside the range of the dataset:

>>> np.sort(heights)
array([ 46.9,  47. ,  47.2,  48.3,  48.7,  49.7,  62])
'''

import numpy as np

temps = np.array([86, 88, 94, 85, 97, 90, 87, 85, 94, 93, 92, 95, 98, 85, 94, 91, 97, 88, 87, 86, 99, 89, 89, 99, 88, 96, 93, 96, 85, 88, 191, 95, 96, 87, 99, 93, 90, 86, 87, 100, 187, 98, 101, 101, 96, 94, 96, 87, 86, 92, 98,94, 98, 90, 99, 96, 99, 86, 97, 98, 86, 90, 86, 94, 91, 88, 196, 195,93, 97, 199, 87, 87, 90, 90, 98, 88, 92, 97, 88, 85, 94, 88, 93, 198, 90, 91, 90, 92, 92])

sorted_temps = np.sort(temps)
print(sorted_temps)


## Median

'''Another key metric that we can use in data analysis is the median. The median is the middle value of a dataset that’s been ordered in terms of magnitude (from lowest to highest).

Let's look at the following array:

np.array( [1, 1, 2, 3, 4, 5, 5])
In this example, the median would be 3, because it is positioned half-way between the minimum value and the maximum value.

If the length of our dataset was an even number, the median would be the value halfway between the two central values. So in the following example, the median would be 3.5:

np.array( [1, 1, 2, 3, 4, 5, 5, 6])
But what if we had a very large dataset? It would get very tedious to count all of the values. Luckily, NumPy also has a function to calculate the median, np.median:

>>> my_array = np.array([50, 38, 291, 59, 14])
>>> np.median(my_array)
50.0
'''

import numpy as np

large_set = np.genfromtxt('household_income.csv', delimiter=',')



small_set_median = 40500

large_set_median = np.median(large_set)


print(large_set)


print(small_set_median)
print(large_set_median)


## Mean vs Median
'''In a dataset, the median value can provide an important comparison to the mean. 
Unlike a mean, the median is not affected by outliers. 
This becomes important in skewed datasets, datasets whose values are not distributed evenly.
Let's write a program that explores this idea further.
'''

import numpy as np

time_spent = np.genfromtxt('file.csv', delimiter=',')

print(time_spent)

minutes_mean = np.mean(time_spent)
minutes_median = np.median(time_spent)

print(minutes_mean)
print(minutes_median)

best_measure = minutes_median

## Percentiles

'''
As we know, the median is the middle of a dataset: it is the number for which 50% of the samples are below, and 50% of the samples are above. But what if we wanted to find a point at which 40% of the samples are below, and 60% of the samples are above?

This type of point is called a percentile. The Nth percentile is defined as the point N% of samples lie below it. So the point where 40% of samples are below is called the 40th percentile. Percentiles are useful measurements because they can tell us where a particular value is situated within the greater dataset.

Let's look at the following array:

d = [1, 2, 3, 4, 4, 4, 6, 6, 7, 8, 8]
There are 11 numbers in the dataset. The 40th percentile will have 40% of the 10 remaining numbers below it (40% of 10 is 4) and 60% of the numbers above it (60% of 10 is 6). So in this example, the 40th percentile is 4.

percentile

In NumPy, we can calculate percentiles using the function np.percentile, which takes two arguments: the array and the percentile to calculate.

Here's how we would use NumPy to calculate the 40th percentile of array d:

>>> d = np.array([1, 2, 3, 4, 4, 4, 6, 6, 7,  8, 8])
>>> np.percentile(d, 40)
4.00
'''

import numpy as np

patrons = np.array([ 2, 6, 14, 4, 3, 9, 1, 11, 4, 2, 8])

thirtieth_percentile = np.percentile(patrons,30)
print(thirtieth_percentile)

seventieth_percentile = np.percentile(patrons,70)
print(seventieth_percentile)


'''
Some percentiles have specific names:

The 25th percentile is called the first quartile
The 50th percentile is called the median
The 75th percentile is called the third quartile
The minimum, first quartile, median, third quartile, and maximum of a dataset are called a five-number summary. This set of numbers is a great thing to compute when we get a new dataset.

The difference between the first and third quartile is a value called the interquartile range. For example, say we have the following array:

d = [1, 2, 3, 4, 4, 4, 6, 6, 7, 8, 8]
We can calculate the 25th and 75th percentiles using np.percentile:

np.percentile(d, 25)
>>> 3.5
np.percentile(d, 75)
>>> 6.5
Then to find the interquartile range, we subtract the value of the 25th percentile from the value of the 75th:

6.5 - 3.5 = 3
50% of the dataset will lie within the interquartile range. The interquartile range gives us an idea of how spread out our data is. The smaller the interquartile range value, the less variance in our dataset. The greater the value, the larger the variance.
'''

import numpy as np

movies_watched = np.array([2, 3, 8, 0, 2, 4, 3, 1, 1, 0, 5, 1, 1, 7, 2])

first_quarter = np.percentile(movies_watched, 25)
third_quarter = np.percentile(movies_watched, 75)

interquartile_range = third_quarter - first_quarter

print(first_quarter)
print(third_quarter)
print(interquartile_range)


## Standard Deviation std

import numpy as np

pumpkin = np.array([68, 1820, 1420, 2062, 704, 1156, 1857, 1755, 2092, 1384])

acorn_squash = np.array([20, 43, 99, 200, 12, 250, 58, 120, 230, 215])

pumpkin_avg = np.mean(pumpkin)
acorn_squash_avg = np.mean(acorn_squash)

pumpkin_std = np.std(pumpkin)
acorn_squash_std = np.std(acorn_squash)

print(pumpkin_std)
print(acorn_squash_std)
winner = pumpkin

## Review

import numpy as np

rainfall = np.array([5.21, 3.76, 3.27, 2.35, 1.89, 1.55, 0.65, 1.06, 1.72, 3.35, 4.82, 5.11])

rain_mean = np.mean(rainfall)
rain_median = np.median(rainfall)
first_quarter = np.percentile(rainfall, 25)
third_quarter = np.percentile(rainfall, 75)
interquartile_range = third_quarter - first_quarter
rain_std = np.std(rainfall)

print(rain_mean)
print(rain_median)
print(first_quarter)
print(third_quarter)
print(interquartile_range)
print(rain_std)


