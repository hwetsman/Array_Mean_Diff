# Array_Mean_Diff
Graphical easy to understand presentation of confidence intervals

## Background: 
Most people who want to compare two things have data, but no way to quickly understand the comparison. Statistical packages often have a high learning curve. Also, most people are visual and can see a difference better than they can understand numerical comparisons. 

It is common when dealing with a sample from a population to calculate the mean. It is also common to use bootstrapping to calculate the confidence intervals of that sample mean. Given two different samples, one could calculate the means and confidence intervals. Then using numeric principles, one could calculate the odds that the means might be different given the measurements that we have.

The present project aims to provide a quick, easy to use visual identifier for overlap of confidence intervals.

## Use
One would input their own arrays, the confidence interval they want to use, and then run the script. The output is a pyplot graphic showing the min, max, mean, and required confidence intervals. If these intervals overlap, the two means cannot be said to be different enough to meet the confidence intervals wished for. If the confidence intervals do not overlap, the means are sufficiently different to show that the null can be rejected.

## To Do
I want to pretty up the graph using seaborn and perhaps improve the shape of the graphic. Also inputs for the user's arrays and confidence intervals would be good.
