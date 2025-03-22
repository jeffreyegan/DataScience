''' recipes.csv =

2,0.75,2,1,0.5
1,0.125,1,1,0.125
2.75,1.5,1,0,1
4,0.5,2,2,0.5

'''


import numpy as np

cupcakes = np.array([2, 0.75, 2, 1, 0.5])

recipes = np.genfromtxt('recipes.csv', delimiter=',')

print(recipes)

eggs = recipes[:, 2]
print(eggs)

print(eggs == 1)

cookies = recipes[2,:]
print(cookies)

double_batch = 2 * cupcakes
print(double_batch)

grocery_list = cookies + double_batch
print(grocery_list)

