

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def Means_of_Boots(array):
    boot = []
    for _ in range(10000):
        bootsample = np.random.choice(array, array.size, replace=True)
        boot.append(bootsample.mean())
    boot = np.array(boot)
    return boot


def Confid_Levels(array, confidence):
    boot = Means_of_Boots(array)
    boot_lower = np.percentile(boot, confidence*100/2)
    boot_upper = np.percentile(boot, 100-confidence*100/2)
    return boot_lower, boot_upper


# define 2 arrays
# these will in the future be supplied by users
array1 = np.random.randint(6, 18, 120)
array1_name = 'Array 1'
array2 = np.random.randint(8, 22, 150)
array2_name = 'Array 2'
confidence_input = .95  # this is the alpha you wish to test
confidence = round(1-confidence_input, 2)
total = array1.size + array2.size

# define means
mean1 = array1.mean()
mean2 = array2.mean()

# create bootstraps and confidence levels
boot1_lower, boot1_upper = Confid_Levels(array1, confidence)
boot2_lower, boot2_upper = Confid_Levels(array2, confidence)
print(boot1_lower, boot1_upper)
print(boot2_lower, boot2_upper)

# plot these
fig, ax = plt.subplots()
ax.set_title(f'{confidence_input} Confidence Limits on Means of {array1_name} and {array2_name}')
ax.set_ylabel('Mean')
x = [1, 2]
my_xticks = [array1_name, array2_name]
plt.xticks(x, my_xticks)

# array1
ax.vlines(1, array1.min(), array1.max(), color='b', alpha=.2)
ax.hlines(array1.mean(), 1-(array1.size/total), 1+(array1.size/total), color='b')
ax.hlines(boot1_lower, 1-(array1.size/total), 1+(array1.size/total), color='b')
ax.hlines(boot1_upper, 1-(array1.size/total), 1+(array1.size/total), color='b')
if array1.mean() > array2.mean():
    ax.hlines(boot1_lower, 1, 2, color='b', linestyles='dotted')
else:
    ax.hlines(boot1_upper, 1, 2, color='b', linestyles='dotted')

# array2
ax.vlines(2, array2.min(), array2.max(), color='y', alpha=.2)
ax.hlines(array2.mean(), 2-(array2.size/total), 2+(array2.size/total), color='y')
ax.hlines(boot2_lower, 2-(array2.size/total), 2+(array2.size/total), color='y')
ax.hlines(boot2_upper, 2-(array2.size/total), 2+(array2.size/total), color='y')
if array2.mean() > array1.mean():
    ax.hlines(boot2_lower, 1, 2, color='y', linestyles='dotted')
else:
    ax.hlines(boot2_upper, 1, 2, color='y', linestyles='dotted')
plt.show()
