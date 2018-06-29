'''
Dr. Dirac's Statistics Midterm
Grading a multiple choice exam is easy. But how much do multiple choice exams tell us about what a student really knows? Dr. Dirac is administering a statistics midterm and wants to use Bayes' Theorem to help him understand the following:

How likely is it that a student really understands the material, given that she has answered a particular question correctly?
Dr. Dirac knows the following probabilities based on many years of teaching:

There is a question on the exam that 60% of students know the correct answer to.
Given that a student knows the correct answer, there is still a 15% chance that the student picked the wrong answer.
Given that a student does not know the answer, there is still a 20% chance that the student picks the correct answer by guessing.
Eventually, we will answer the following question:

Given that a student answered a question correctly, what is the probability that she really knows the material?

'''

import numpy as np

# A = knows material
# B = answers question correctly

p_a = 0.6  #p know material

p_b_given_a = 1.0-0.15 # right answer given they know material

p_b = 0.6*(1-.15) + 0.4*.2 # any student ansering correctly


# Bayes: P(A|B) = ( P(B|A) * P(A) ) / P(B)

# P(knows material | answers correctly)
p_a_given_b = (p_b_given_a * p_a) / p_b
print(p_a_given_b)

