'''

CrunchieMunchies
You work in marketing for a food company YummyCorps, which is developing a new kind of tasty, wholesome cereal called CrunchieMunchies. You want to demonstrate to consumers how healthy your cereal is in comparison to other leading brands, so you've dug up nutritional data on several different competitors.

Your task is to use NumPy statistical calculations to analyze this data and prove that your CrunchieMunchies cereal is the healthiest choice for consumers.
'''

import codecademylib
import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')

print(calorie_stats)

average_calories = np.mean(calorie_stats)
print(average_calories)

calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

median_calories = np.median(calorie_stats)
print(median_calories)

for x in range(0, 10):
    print(x)
    print(np.percentile(calorie_stats, x))

nth_percentile = np.percentile(calorie_stats, 4)

more_calories = np.mean(calorie_stats > 60)
print(more_calories * 100)

calorie_std = np.std(calorie_stats)
print(calorie_std)

'''When looking at the cereal offerings as a whole, Crunchie Munchie offers a low calorie option that has fewer calories than 96% of the competition. The calorie content even falls below the mean less one-sigma limit and has fewer calories than all but three competing cereals.'''