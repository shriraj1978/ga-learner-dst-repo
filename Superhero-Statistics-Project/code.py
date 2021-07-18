# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

# Code starts here

# Replacing the '-' with 'Agender' in gender column
data['Gender'].replace('-','Agender',inplace=True)

# Plotting the Distribution of Gender
gender = data['Gender'].value_counts()

gender.plot(kind='bar')
plt.title('Distribution of Gender')
plt.xlabel('Gender')
plt.ylabel('Counts')
plt.show()

# Does good overpower evil or does evil overwhelm good?
# Plotting the Distribution of Alignment
alignment = data['Alignment'].value_counts()

plt.pie(alignment,labels=['Good','Bad','Neutral'],startangle=90,explode=(0.05,0.05,0.05))
plt.show()

# Checking out if combat relate to persons strength or intelligence

# Calculating the covariance of Intelligence and Combat
intelligence_combat = data[['Intelligence','Combat']]

cov_intelligence_combat = intelligence_combat['Intelligence'].cov(intelligence_combat['Combat'])

# Calculating the standard deviation of Intelligence and Combat
std_intelligence = intelligence_combat['Intelligence'].std()
std_combat = intelligence_combat['Combat'].std()

# Calculating the coefficient for Intelligence and Combat
coefficient_intelligence_combat = cov_intelligence_combat / (std_intelligence * std_combat)
print('Coefficient for Intelligence and Combat:',np.round(coefficient_intelligence_combat,2))

# Calculating the covariance of Strength and Combat
strength_combat = data[['Strength','Combat']]

cov_strength_combat = strength_combat['Strength'].cov(strength_combat['Combat'])

# Calculating the standard deviation of Intelligence and Combat
std_strength = strength_combat['Strength'].std()
std_combat = strength_combat['Combat'].std()

# Calculating the coefficient for Intelligence and Combat
coefficient_strength_combat = cov_strength_combat / (std_strength * std_combat)
print('Coefficient for Strength and Combat:',np.round(coefficient_strength_combat,2))

# Plotting the histogram of Combat, Intelligence, Strength
plt.figure(figsize = (10,6))

plt.subplot(1,3,1)
plt.hist(data['Combat'],bins=20)
plt.title('Combat')

plt.subplot(1,3,2)
plt.hist(data['Intelligence'],bins=20)
plt.title('Intelligence')

plt.subplot(1,3,3)
plt.hist(data['Strength'],bins=20)
plt.title('Strength')

plt.show()

# Finding out the best in the best superhero universe

quantile_total = data['Total'].quantile(0.99)
super_best = data[data['Total']>quantile_total]
super_best_names = list(super_best['Name'])
print('Best Super Hero: ',super_best_names)




