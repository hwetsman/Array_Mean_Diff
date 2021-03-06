# Array_Mean_Diff
Graphical easy to understand presentation of confidence intervals

## Background:
Most people who want to compare two things have data, but no way to quickly understand the comparison. Statistical packages often have a high learning curve. Also, most people are visual and can see a difference better than they can understand numerical comparisons.

It is common when dealing with a sample from a population to calculate the mean. It is also common to use bootstrapping to calculate the confidence intervals of that sample mean. Given two different samples, one could calculate the means and confidence intervals. Then using numeric principles, one could calculate the odds that the means might be different given the measurements that we have.

The present project aims to provide a quick, easy to use visual identifier for overlap of confidence intervals.

## Use
To use this app, clone the repo. Then insert the csv of your choice (with headers on first line) in the Data directory and remove the Sample.csv. Run `pip install -r requirements.txt` from the directory containing the app. Then from the terminal, cd to the app directory and run `streamlit run Mean_Diff.py`.

From the sliders on the sidebar, select the confidence interval you want to use and the columns of your dataframe that you wish to compare. The output is a pyplot graphic showing the min, max, mean, and required confidence intervals. If these confidence intervals overlap, the two means cannot be said to be different enough to reject the null hypothesis that the means are the same. If the confidence intervals do not overlap, the means are sufficiently different to show that the null can be rejected.

## To Do
I want to pretty up the graph using seaborn and perhaps improve the shape of the graphic. 
