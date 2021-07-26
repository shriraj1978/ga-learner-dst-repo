# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here

# Calculating probability for the event that fico credit score is greater than 700
p_a = len(df[df['fico']>700]) / len(df)

# Calculating probability for the event that purpose == 'debt_consolation'
p_b = len(df[df['purpose']=='debt_consolidation']) / len(df)

df1 = df[df['purpose']=='debt_consolidation']

# Calculating probability for the event that purpose == 'debt_consolation' given 'fico' credit score
p_a_b = len(df1[df1['fico']>700]) / len(df1)

# Checking the independency 
result = p_a_b == p_a
print('Variable Independent : ',result)

# Calculating the probability for the event that paid.back.loan == Yes
prob_lp = len(df[df['paid.back.loan'] == 'Yes'])/len(df)

# Calculating the probability for the event that credit.policy == Yes
prob_cs = len(df[df['credit.policy'] == 'Yes'])/len(df)

new_df = df[df['paid.back.loan']=='Yes']

# Calculating the probability for the event that paid.back.loan == 'Yes' given credit.policy == 'Yes'
prob_pd_cs = len(new_df[new_df['credit.policy'] == 'Yes'])/len(new_df)

# Calculating the conditional probability
bayes = (prob_pd_cs*prob_lp)/prob_cs
print('Probability of Paid Back Loan given Credit Policy: ',round(bayes,4))
print('*'*30)

# Plotting the bar plot for the purpose where paid.back.loan == No
df1 = df[df['paid.back.loan']=='No']
df1.shape

df1['purpose'].value_counts().plot(kind='bar')
plt.show()

# Plotting the histogram for visualization of the continuous variable
inst_median = df['installment'].median()
inst_mean = df['installment'].mean()
df['installment'].value_counts().hist()
df['log.annual.inc'].value_counts().hist()
plt.show()



