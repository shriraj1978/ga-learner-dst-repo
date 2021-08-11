# --------------
#Importing header files
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency

import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# Critical Value
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1


#Reading file
data=pd.read_csv(path)

# Code starts here

# Calculating the Confidence Interval

# Creating the sample data from the dataset
data_sample = data.sample(n=sample_size,random_state=0)

# Calculating the mean of installment column of the sample
sample_mean = data_sample['installment'].mean()

# Calculating the standard deviation of installment column of the population
population_std = data['installment'].std()

# Finding the margin of error
margin_of_error = z_critical * (population_std/math.sqrt(sample_size))

# Finding the confidence interval
confidence_interval = []
val_1 = round(sample_mean - margin_of_error,2)
val_2 = round(sample_mean + margin_of_error,2)
confidence_interval.append(val_1)
confidence_interval.append(val_2)

# Finding the true mean of the installment
true_mean = data['installment'].mean()

# Checking the true mean lies in confidence interval
if confidence_interval[0] < true_mean < confidence_interval[1]:
    print('True Mean lies in confidence interval')
else:
    print('True Mean do not lies in confidence interval')
print('True Mean : ',round(true_mean,2))
print('Confidence Interval :',confidence_interval)


# Finding Central Limit Theorem holds for installment column

# Creating an array of sample sizes
sample_sizes = np.array([20, 50, 100])

# Plotting the graph to check if CLT holds for installment column

fig, axes = plt.subplots(nrows=3,ncols=1)

for i in range(len(sample_sizes)):
    m = []
    for j in range(1000):
        sample_data = data.sample(sample_sizes[i])

        sample_mean = sample_data['installment'].mean()

        m.append(sample_mean)
    
    mean_series = pd.Series(m)

    axes[i].hist(mean_series, bins=1000)

plt.show()

# Small Business Interests

# Removing the character % from the values in column int.rate and dividing it by 100
data['int.rate'] = data['int.rate'].str.replace('%','').astype(float)/100

# Applying the z-test with interest rate of small businesses and the mean of interest rate
z_statistic_1, p_value_1 = ztest(data[data['purpose']=='small_business']['int.rate'], x2=None, value=data['int.rate'].mean(), alternative='larger')

print('z-Statistic-1 : ',round(z_statistic_1,2))
print('p-Value-1 : ',p_value_1)

if p_value_1 < 0.05:
    print('Reject the null hypothesis')
else:
    print('Accept the null hypothesis')



# Installment vs Loan Defaulting

# Applying the z-test with interest rate of small businesses and the mean of interest rate
z_statistic_2, p_value_2 = ztest(data[data['paid.back.loan']=='No']['installment'], data[data['paid.back.loan']=='Yes']['installment'])

print('z-Statistic-2 : ',round(z_statistic_2,2))
print('p-Value-2 : ',p_value_2)

if p_value_1 < 0.05:
    print('Reject the null hypothesis')
else:
    print('Accept the null hypothesis')

# Purpose vs Loan Defaulting

# Finding the value counts of different purposes
Ayes = data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
Noes = data[data['paid.back.loan']=='No']['purpose'].value_counts()

# Concatenating the above 2 values in single dataframe
observed = pd.concat([Ayes, Noes], axis=1, keys=['Yes', 'No'])

# Applying the chi2 value to above stored values
chi2, p, dof, ex = chi2_contingency(observed)

print('Chi-squared Statistic : ',round(chi2,2))
print('Critical Value : ',round(critical_value,2))

if chi2 > critical_value:
    print('Reject the null hypothesis')
else:
    print('Accept the null hypothesis')

# Code ends here


