#!/usr/bin/env python
# coding: utf-8

# # question 01
Q1. Pearson correlation coefficient is a measure of the linear relationship between two variables. Suppose
you have collected data on the amount of time students spend studying for an exam and their final exam
scores. Calculate the Pearson correlation coefficient between these two variables and interpret the result.
To calculate the Pearson correlation coefficient between the amount of time students spend studying for an exam and their final exam scores, you need to first calculate the covariance and standard deviations of the two variables.

Assuming you have n pairs of observations (x1,y1), (x2,y2),..., (xn,yn) for the two variables, the Pearson correlation coefficient r is calculated as:

r = cov(x, y) / (sd(x) * sd(y))

where cov(x, y) is the covariance between x and y, and sd(x) and sd(y) are the standard deviations of x and y, respectively.

Once you calculate the covariance and standard deviations, you can plug them into the formula to get the Pearson correlation coefficient.

The interpretation of the Pearson correlation coefficient is as follows:

If r is close to 1, it indicates a strong positive linear relationship between the two variables, meaning that as one variable increases, the other variable also increases.
If r is close to -1, it indicates a strong negative linear relationship between the two variables, meaning that as one variable increases, the other variable decreases.
If r is close to 0, it indicates a weak or no linear relationship between the two variables.
Note that the Pearson correlation coefficient only measures the strength of a linear relationship between the two variables, and does not imply causality. Other factors could be influencing the relationship between the two variables.
# # question 02
Q2. Spearman's rank correlation is a measure of the monotonic relationship between two variables.
Suppose you have collected data on the amount of sleep individuals get each night and their overall job
satisfaction level on a scale of 1 to 10. Calculate the Spearman's rank correlation between these two
variables and interpret the result.
To calculate the Spearman's rank correlation between the amount of sleep individuals get each night and their overall job satisfaction level on a scale of 1 to 10, you need to first rank the observations for each variable. Then, you can calculate the Spearman's rank correlation coefficient, denoted by rs, using the following formula:

rs = 1 - (6 * sum(d^2) / (n*(n^2 - 1)))

where d is the difference between the ranks of the corresponding pairs of observations, and n is the number of observations.

Once you calculate the Spearman's rank correlation coefficient, you can interpret the result as follows:

If rs is close to 1, it indicates a strong positive monotonic relationship between the two variables, meaning that as one variable increases, the other variable also tends to increase (or vice versa).
If rs is close to -1, it indicates a strong negative monotonic relationship between the two variables, meaning that as one variable increases, the other variable tends to decrease (or vice versa).
If rs is close to 0, it indicates a weak or no monotonic relationship between the two variables.
Note that the Spearman's rank correlation coefficient only measures the strength of a monotonic relationship between the two variables, and not necessarily a linear relationship. This means that the relationship between the two variables could be non-linear, but still exhibit a monotonic trend. Also, as with the Pearson correlation coefficient, the Spearman's rank correlation coefficient does not imply causality. Other factors could be influencing the relationship between the two variables.
# # question 03
Q3. Suppose you are conducting a study to examine the relationship between the number of hours of
exercise per week and body mass index (BMI) in a sample of adults. You collected data on both variables
for 50 participants. Calculate the Pearson correlation coefficient and the Spearman's rank correlation
between these two variables and compare the results.
To calculate the Pearson correlation coefficient and the Spearman's rank correlation coefficient between the number of hours of exercise per week and body mass index (BMI) in a sample of 50 adults, you need to first calculate the covariance, standard deviations, and ranks of the two variables.

Assuming you have n=50 pairs of observations (x1,y1), (x2,y2),..., (xn,yn) for the two variables, you can calculate the Pearson correlation coefficient r as:

r = cov(x, y) / (sd(x) * sd(y))

where cov(x, y) is the covariance between x and y, and sd(x) and sd(y) are the standard deviations of x and y, respectively.

To calculate the Spearman's rank correlation coefficient rs, you need to rank the observations for each variable, and then calculate the correlation coefficient using the following formula:

rs = 1 - (6 * sum(d^2) / (n*(n^2 - 1)))

where d is the difference between the ranks of the corresponding pairs of observations, and n is the number of observations.

Once you calculate both correlation coefficients, you can compare the results.

If the relationship between the two variables is linear, then the Pearson correlation coefficient r will be a more appropriate measure of the strength of the relationship. On the other hand, if the relationship is monotonic but not necessarily linear, then the Spearman's rank correlation coefficient rs will be a better measure.

If the relationship is strictly linear, then the Pearson correlation coefficient and the Spearman's rank correlation coefficient will be identical. However, if the relationship is non-linear, then the Pearson correlation coefficient may not capture the full strength of the relationship.

In general, if there is a monotonic relationship between the two variables, then the Spearman's rank correlation coefficient will be a more appropriate measure than the Pearson correlation coefficient. However, if the relationship is linear, then the Pearson correlation coefficient will provide a more accurate measure of the strength of the relationship.

Therefore, in this case, it would be appropriate to calculate both correlation coefficients and compare the results to determine which measure is more appropriate for describing the relationship between the number of hours of exercise per week and body mass index (BMI) in the sample of adults.
# # question 04
# Q4. A researcher is interested in examining the relationship between the number of hours individuals
spend watching television per day and their level of physical activity. The researcher collected data on
both variables from a sample of 50 participants. Calculate the Pearson correlation coefficient between
these two variables.
To calculate the Pearson correlation coefficient between the number of hours individuals spend watching television per day and their level of physical activity in a sample of 50 participants, you need to first calculate the covariance, standard deviations, and means of the two variables.

Assuming you have n=50 pairs of observations (x1,y1), (x2,y2),..., (xn,yn) for the two variables, you can calculate the Pearson correlation coefficient r as:

r = cov(x, y) / (sd(x) * sd(y))

where cov(x, y) is the covariance between x and y, and sd(x) and sd(y) are the standard deviations of x and y, respectively.

To calculate the covariance, you can use the following formula:

cov(x, y) = (1/n) * sum((xi - x_mean) * (yi - y_mean))

where xi and yi are the ith observations of x and y, respectively, x_mean and y_mean are the means of x and y, respectively, and n is the number of observations.

To calculate the standard deviations, you can use the following formula:

sd(x) = sqrt((1/n) * sum((xi - x_mean)^2))

sd(y) = sqrt((1/n) * sum((yi - y_mean)^2))

where xi and yi are the ith observations of x and y, respectively, x_mean and y_mean are the means of x and y, respectively, and n is the number of observations.

Once you calculate the covariance and standard deviations, you can plug them into the formula for r to obtain the Pearson correlation coefficient.

Interpreting the Pearson correlation coefficient will depend on the value obtained. If r is close to 1, it indicates a strong positive linear relationship between the two variables, meaning that as one variable increases, the other variable also tends to increase (or vice versa). If r is close to -1, it indicates a strong negative linear relationship between the two variables, meaning that as one variable increases, the other variable tends to decrease (or vice versa). If r is close to 0, it indicates a weak or no linear relationship between the two variables.

In this case, it is not possible to determine the strength or direction of the relationship without actually calculating the correlation coefficient. Therefore, you need to collect the data and use the above formulas to calculate the Pearson correlation coefficient between the number of hours individuals spend watching television per day and their level of physical activity.
# # question 05
# 
It appears that there is some missing data in the survey results provided, as there is no corresponding soft drink preference for the ages of 37 and 19. Therefore, it is not possible to analyze the relationship between age and preference for a particular brand of soft drink based on the data provided.

In general, to examine the relationship between two categorical variables like age and soft drink preference, you can use a chi-square test of independence. This test evaluates whether there is a statistically significant association between the two variables. If the test result is statistically significant, it suggests that the two variables are not independent and that there is a relationship between them. However, this analysis requires complete data for both variables, and the data provided in the question is incomplete.
# # question 06
Q6. A company is interested in examining the relationship between the number of sales calls made per day
and the number of sales made per week. The company collected data on both variables from a sample of
30 sales representatives. Calculate the Pearson correlation coefficient between these two variables.
To calculate the Pearson correlation coefficient between the number of sales calls made per day and the number of sales made per week in a sample of 30 sales representatives, you need to first calculate the covariance, standard deviations, and means of the two variables.

Assuming you have n=30 pairs of observations (x1,y1), (x2,y2),..., (xn,yn) for the two variables, you can calculate the Pearson correlation coefficient r as:

r = cov(x, y) / (sd(x) * sd(y))

where cov(x, y) is the covariance between x and y, and sd(x) and sd(y) are the standard deviations of x and y, respectively.

To calculate the covariance, you can use the following formula:

cov(x, y) = (1/n) * sum((xi - x_mean) * (yi - y_mean))

where xi and yi are the ith observations of x and y, respectively, x_mean and y_mean are the means of x and y, respectively, and n is the number of observations.

To calculate the standard deviations, you can use the following formula:

sd(x) = sqrt((1/n) * sum((xi - x_mean)^2))

sd(y) = sqrt((1/n) * sum((yi - y_mean)^2))

where xi and yi are the ith observations of x and y, respectively, x_mean and y_mean are the means of x and y, respectively, and n is the number of observations.

Once you calculate the covariance and standard deviations, you can plug them into the formula for r to obtain the Pearson correlation coefficient.

For example, suppose the data for the number of sales calls made per day and the number of sales made per week are as follows:

Sales Calls (x): 10, 12, 8, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66
Sales Made (y): 2, 3, 1, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50

Using the formulas outlined above, you can calculate the Pearson correlation coefficient r to be approximately 0.986.

Interpreting the Pearson correlation coefficient will depend on the value obtained. In this case, the value of r is close to 1, which indicates a strong positive linear relationship between the two variables. This suggests that as the number of sales calls made per day increases, the number of sales made per week also tends to increase, and vice versa.