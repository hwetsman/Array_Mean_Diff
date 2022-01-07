"""
Author: Howard Wetsman MD
Purpose: To give users a quick, intuitive view of a comparison of two, possibly
overlapping, samples' data.
Inputs: Two arrays of numbers
Output: Image of the overlap or lack of overlap of the 95% confidence levels
from those arrays
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import streamlit as st


def Means_of_Boots(array):
    """
    Function to bootstrap an array 10K times and return an array of the mean of
    each of those bootstraps
    Input: np.array - an array of sample data
    Output: np.array - an array of 10000 means of bootstrapped samples
    """
    boot = []
    for _ in range(10000):
        bootsample = np.random.choice(array, array.size, replace=True)
        boot.append(bootsample.mean())
    boot = np.array(boot)
    return boot


def Confid_Levels(array, confidence):
    """
    This will take the confidence levels calculated from user input alpha and the bootstrap
    array and return the desired confidence levels upper and lower for plotting
    Input: np.array and float - Takes the float of 1-alpha and the array of bootstrapped
    means of the input array
    Output: float, float - The upper and lower confidence levels for the
    plot of the bootstraps
    """
    boot = Means_of_Boots(array)
    boot_lower = np.percentile(boot, confidence*100/2)
    boot_upper = np.percentile(boot, 100-confidence*100/2)
    return boot_lower, boot_upper


# Refactor to Streamlit
# create better sample data with multiple cols - done
# read sample data to csv
df = pd.read_csv('Data/Sample.csv')
cols = df.columns.tolist()
print(cols)
# choose cols to be displayed
array1_name = st.sidebar.select_slider('Select for first array', cols)
array2_name = st.sidebar.select_slider('Select for first array', cols)
# set up user choice of cols
# display results on streamlit


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
# fill rectangle
height = boot1_upper-boot1_lower
width = 2*array1.size/total
origin = (1-(array1.size/total), boot1_lower)
rect1 = patches.Rectangle(origin, width, height, linewidth=1, edgecolor='b', facecolor='lightblue')
ax.add_patch(rect1)

if array1.mean() > array2.mean():
    ax.hlines(boot1_lower, 1, 2, color='b', linestyles='dotted')
else:
    ax.hlines(boot1_upper, 1, 2, color='b', linestyles='dotted')

# array2
ax.vlines(2, array2.min(), array2.max(), color='y', alpha=.2)
ax.hlines(array2.mean(), 2-(array2.size/total), 2+(array2.size/total), color='y')
ax.hlines(boot2_lower, 2-(array2.size/total), 2+(array2.size/total), color='y')
ax.hlines(boot2_upper, 2-(array2.size/total), 2+(array2.size/total), color='y')
# fill rectangle
height = boot2_upper-boot2_lower
width = 2*array2.size/total
origin = (2-(array2.size/total), boot2_lower)
rect2 = patches.Rectangle(origin, width, height, linewidth=1,
                          edgecolor='y', facecolor='lightyellow')
ax.add_patch(rect2)
if array2.mean() > array1.mean():
    ax.hlines(boot2_lower, 1, 2, color='y', linestyles='dotted')
else:
    ax.hlines(boot2_upper, 1, 2, color='y', linestyles='dotted')
plt.show()
