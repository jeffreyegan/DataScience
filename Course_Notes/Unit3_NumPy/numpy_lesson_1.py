## NumPy Arrays

import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])

test_2 = np.genfromtxt('test_2.csv', delimiter=',')

## Operations with Arrays


import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

# Giving students 2 extra points for erroroneous Q on test
test_3_fixed = test_3 + 2
# Quicker than list operations with for loops


total_grade = test_1 + test_2 + test_3_fixed

final_grade = total_grade / 3

print(final_grade)

## 2-D Arrays

import numpy as np

coin_toss = np.array([1,0,0,1,0])

coin_toss_again = np.array([[1,0,0,1,0],[0,0,1,1,1]])



import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

jeremy_test_2 = test_2[3]
print(jeremy_test_2)

manual_adwoa_test_1 = np.array([test_1[1], test_1[2]])
print(manual_adwoa_test_1)


## Selecting a value from a 2-D Array

#Axis 0 = column, Axis 1 = row

import numpy as np

student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])

tanya_test_3 = student_scores[2,0]
print(tanya_test_3)

cody_test_scores = student_scores[0:,4]
print(cody_test_scores)

## Logical Operations with Arrays

'''
Logical Operations with Arrays
Another useful thing that arrays can do is perform element-wise logical operations. For instance, suppose we want to know how many elements in an array are greater than 5. We can easily write some code that checks to see whether this statement evaluates to True for each item in the array, without having to use a for loop :

>>> a = np.array([10, 2, 2, 4, 5, 3, 9, 8, 9, 7])
>>> a > 5
array([True, False, False, False, False, False, True, True, True, True], dtype=bool)
We can then use logical operators to evaluate and select items based on certain criteria. To select all elements from the previous array that are greater than 5, we'd write the following:

>>> a[a > 5]
array([10, 9, 8, 9, 7])
We can also combine logical statements to further specify our criteria. To do so, we place each statement in parentheses and use boolean operators like & (and) and | (or).

In our example, we can use combined statements to find the elements that are greater than five or less than two:

>>> a[(a > 5) | (a < 2)]
array([10, 9, 8, 9, 7])
'''

import numpy as np

porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

cold = porridge[porridge<60]
print(cold)

hot = porridge[porridge>80]
print(hot)

just_right = porridge[(porridge > 60) & (porridge < 80)]
print(just_right)


## Review

'''
Let's take a second and review. In this lesson, you learned the basics of the NumPy package. Here are some key points:

Arrays are a special type of list that allows us to store values in an organized manner.
An array can be created by either defining it directly using np.array() or by importing a CSV using np.genfromtxt('file.csv', delimiter=',').
An operation (such as addition) can be performed on every element in an array by simply performing it on the array itself.
Elements can be selected from arrays using their index and array locations, both of which start at 0.
Logical operations can be used to create new, more focused arrays out of larger arrays.
The next lesson will explore how to analyze these arrays and use means, medians, and standard deviations to tell a story. But first, practice what you've learned by working through the following checkpoints.
'''


import numpy as np

temperatures = np.genfromtxt('temperature_data.csv', delimiter=',')

print(temperatures)

temperatures_fixed = temperatures + 3
print(temperatures_fixed)

monday_temperatures = temperatures_fixed[0,:]
print(monday_temperatures)

thursday_friday_morning = np.array([temperatures_fixed[3,1], temperatures_fixed[4,1]])
print(thursday_friday_morning)

temperature_extremes = temperatures_fixed[(temperatures_fixed<50)|(temperatures_fixed>60)]
print(temperature_extremes)

