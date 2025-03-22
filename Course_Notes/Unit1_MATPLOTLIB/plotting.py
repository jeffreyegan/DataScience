from matplotlib import pyplot as plt


## Advanced Subplots

x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]
plt.subplot(2,1,1)
plt.plot(x, straight_line)
plt.subplot(2,2,3)
plt.plot(x,parabola)
plt.subplot(2,2,4)
plt.plot(x,cubic)

plt.subplots_adjust(wspace=0.35,bottom=0.2)
plt.show()


## Legends

months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)

#create your legend here
legend_labels = ['Hyrule','Kakariko','Gerudo Valley']
plt.legend(legend_labels, loc=8)
plt.show()

## Modify Ticks

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

plt.xlabel("Months")
plt.ylabel("Conversion")

plt.plot(months, conversion)

# Your work here
ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
ax.set_yticks([0.10,0.25,0.5,0.75])
ax.set_yticklabels(['10%','25%','50%','75%'])

plt.show()

## Figures

word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

plt.close('all')

plt.figure()
plt.plot(years,word_length)
plt.show()
plt.savefig('winning_word_lengths.png')

plt.figure(figsize=(7,3))
plt.plot(years,power_generated)
plt.show()
plt.savefig('power_generated.png')

## More Plotting

x = [0, 1, 2, 3, 4, 7, 8, 22, 35]
y1 = [128+14.2, 128+11.9, 128+10, 128+10, 128+9, 128+12, 128+12,128+20.5, 128+35.5]
y2 = [1,1,1,2,2,2,3,3,3]

plt.plot(x,y1,color='pink',marker='o')
plt.plot(x,y2,color='gray',marker='o')
plt.title('Two Lines on One Graph')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')
plt.legend(['Baby Weight','Nothing'],loc=9)
plt.show()


## Sublime Limes Project

from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# create your figure here
plt.figure(figsize=(12,8))
ax1 = plt.subplot(1,2,1)
plt.plot(range(len(months)),visits_per_month,marker='o')
plt.xlabel('Month')
plt.ylabel('Visits')
plt.title('Visits per Month')
ax1.set_xticks(range(len(months)))
ax1.set_xticklabels(months)

ax2 = plt.subplot(1,2,2)
ax2.set_xticks(range(len(months)))
ax2.set_xticklabels(months)
plt.xlabel('Month')
plt.ylabel('Limes Sold')
plt.title('Limes Sold per Month')

plt.plot(range(len(months)),key_limes_per_month,color='green',marker='o')
plt.plot(range(len(months)),persian_limes_per_month,color='yellow',marker='o')
plt.plot(range(len(months)),blood_limes_per_month,color='red',marker='o')
legend=['Key Limes', 'Persian Limes', 'Blood Limes']
plt.legend(legend)

plt.savefig('lime_data.png')
plt.show()


## Simple Bar Chart
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)

#create your ax object here
ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)
plt.ylabel('Sales')
plt.xlabel('Drink Type')
plt.show()



## Side by Side Bars

from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

#Paste the x_values code here
n = 1
t = 2
d = len(drinks)
w = 0.8
store1_x = [t*element + w*n for element in range(d)]
n = 2
t = 2
d = len(drinks)
w = 0.8
store2_x = [t*element + w*n for element in range(d)]

plt.bar(store1_x,sales1)
plt.bar(store2_x,sales2)
plt.legend(['Store 1', 'Store 2'])
plt.ylabel('Sales')
ax = plt.subplot()
ax.set_xticks(store1_x)
ax.set_xticklabels(drinks)

plt.show()


## Stacked Bars
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

x_values=range(len(drinks))

plt.bar(x_values,sales1)
plt.bar(x_values,sales2,bottom=sales1)
plt.legend(['Location 1', 'Location 2'])

plt.show()

## Error Bars
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

# Plot the bar graph here

plt.bar(range(len(drinks)),ounces_of_milk,yerr=error,capsize=5)
ax = plt.subplot()
plt.ylabel('Ounces of Milk +/- Barista Error')
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)
plt.title('Milk Per Drink - Accounting for Error')
plt.show()



## Fill Between
from matplotlib import pyplot as plt

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]


y_lower = []
y_upper = []
for val in revenue:
  y_lower.append(val*0.9)
  y_upper.append(val*1.1)

plt.fill_between(months,y_lower, y_upper, alpha=0.2)

plt.plot(months,revenue)
ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)

plt.xlabel('Month')
plt.ylabel('Predicted Revenue +/- 10%')
plt.title('Monthly Revenue Predictions')


plt.show()

## Pie Chart
from matplotlib import pyplot as plt
import numpy as np

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

#make your pie chart here
plt.pie(payment_method_freqs)
plt.axis('equal')
plt.legend(payment_method_names)
plt.show()


payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.pie(payment_method_freqs, labels=payment_method_names, autopct='%0.1f%%')
plt.axis('equal')
plt.title('Payment Methods')
plt.show()

## Bar Chart 1
from matplotlib import pyplot as plt

past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

# Make your chart here
plt.figure(figsize=(10,8))
plt.bar(range(len(years)),past_years_averages,yerr=error,capsize=5)
plt.axis([-0.5,6.5,70,95])
ax = plt.subplot()
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)
plt.title('Final Exam Averages')
plt.xlabel('Year')
plt.ylabel('Test Average')
plt.savefig('my_bar_chart.png')
plt.show()

## Bar Chart 2 - Side by Side
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]


def create_x(t, w, n, d):
    return [t * x + w * n for x in range(d)]


school_a_x = [0.8, 2.8, 4.8, 6.8, 8.8]
school_b_x = [1.6, 3.6, 5.6, 7.6, 9.6]

middle_x = []
for idx in range(len(school_a_x)):
    middle_x.append((school_a_x[idx] + school_b_x[idx]) / 2)

# Make your chart here
plt.figure(figsize=(10, 8))
plt.bar(school_a_x, middle_school_a)
plt.bar(school_b_x, middle_school_b)
ax = plt.subplot()
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)

plt.legend(['Middle School A', 'Middle School B'])
plt.title('Test Averages on Different Units')
plt.xlabel('Unit')
plt.ylabel('Test Average')

plt.savefig('my_side_by_side.png')
plt.show()



## Stacked Bar Chart
from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs)
#create d_bottom and f_bottom here
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)
#create your plot here
plt.figure(figsize=(10,8))
ax = plt.subplot()
ax.set_xticks(x)
ax.set_xticklabels(unit_topics)
plt.bar(x,As)
plt.bar(x,Bs,bottom=As)
plt.bar(x,Cs,bottom=c_bottom)
plt.bar(x,Ds,bottom=d_bottom)
plt.bar(x,Fs,bottom=f_bottom)
plt.title('Grade distribution')
plt.ylabel('Number of Students')
plt.xlabel('Unit')
plt.savefig('my_stacked_bar.png')
leg = ['A','B','C','D','F']
plt.legend(leg)
plt.show()

## Histograms
from matplotlib import pyplot as plt

exam_scores1 = [62.58, 67.63, 81.37, 52.53, 62.98, 72.15, 59.05, 73.85, 97.24, 76.81, 89.34, 74.44, 68.52, 85.13, 90.75, 70.29, 75.62, 85.38, 77.82, 98.31, 79.08, 61.72, 71.33, 80.77, 80.31, 78.16, 61.15, 64.99, 72.67, 78.94]
exam_scores2 = [72.38, 71.28, 79.24, 83.86, 84.42, 79.38, 75.51, 76.63, 81.48,78.81,79.23,74.38,79.27,81.07,75.42,90.35,82.93,86.74,81.33,95.1,86.57,83.66,85.58,81.87,92.14,72.15,91.64,74.21,89.04,76.54,81.9,96.5,80.05,74.77,72.26,73.23,92.6,66.22,70.09,77.2]

# Make your plot here
plt.figure(figsize=(10,8))
plt.hist(exam_scores1, normed=True, bins=12, histtype='step', linewidth=2)
plt.hist(exam_scores2, normed=True, bins=12, histtype='step', linewidth=2)
plt.legend(['1st Yr Teaching','2nd Yr Teaching'])
plt.xlabel('Percentage')
plt.ylabel('Frequency')
plt.title('Final Exam Score Distribution')
plt.savefig('my_histogram.png')
plt.show()


## Pie Chart
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]

#Make your plot here
plt.figure(figsize=(10,8))
plt.pie(num_hardest_reported, labels=unit_topics, autopct='%d%%')
plt.axis('equal')
plt.title('Hardest Topics')
plt.savefig('my_pie_chart.png')


plt.show()

## Line Plot with Shaded Error
from matplotlib import pyplot as plt

hours_reported = [3, 2.5, 2.75, 2.5, 2.75, 3.0, 3.5, 3.25, 3.25, 3.5, 3.5, 3.75, 3.75, 4, 4.0, 3.75, 4.0, 4.25, 4.25,
                  4.5, 4.5, 5.0, 5.25, 5, 5.25, 5.5, 5.5, 5.75, 5.25, 4.75]
exam_scores = [52.53, 59.05, 61.15, 61.72, 62.58, 62.98, 64.99, 67.63, 68.52, 70.29, 71.33, 72.15, 72.67, 73.85, 74.44,
               75.62, 76.81, 77.82, 78.16, 78.94, 79.08, 80.31, 80.77, 81.37, 85.13, 85.38, 89.34, 90.75, 97.24, 98.31]

plt.figure(figsize=(10, 8))

# Create your hours_lower_bound and hours_upper_bound lists here
'''hours_lower_bound = []
hours_upper_bound = []
for val in hours_reported:
  hours_lower_bound.append(val*0.8)
  hours_upper_bound.append(val*1.2)'''

hours_lower_bound = [hours * 0.8 for hours in hours_reported]
hours_upper_bound = [hours * 1.2 for hours in hours_reported]

# Make your graph here
plt.figure(figsize=(10, 8))
plt.fill_between(exam_scores, hours_lower_bound, hours_upper_bound, alpha=0.2)
plt.plot(exam_scores, hours_reported, linewidth=2)
plt.title('Time spent studying vs final exam scores')
plt.xlabel('Score')
plt.ylabel('Hours studying (self-reported)')
plt.savefig('my_line_graph.png')
plt.show()