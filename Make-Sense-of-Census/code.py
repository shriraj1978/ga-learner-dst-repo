# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

# Adding the new record to data

census = np.concatenate((data,new_record),axis=0)

# Checking shape of the data and census
print(data.shape)
print(census.shape)

# Analysis of Age distribution

age = census[0:,0]
max_age = age.max()     # Finding Maximum Age
min_age = age.min()     # Finding Mininum Age
age_mean = age.mean()   # Finding Mean
age_std = age.std()     # Finding Standard deviation

print("Maximum Age : ",max_age)
print("Manimum Age : ",min_age)
print("Mean Age : {:.2f}".format(age_mean))
print("Standard Deviation : {:.2f}".format(age_std))

# Analysis of Race Distribution

race = census[0:,2]

mask = race == 0
race_0 = race[mask]
len_0 = len(race_0)    # Count of race 0

mask = race == 1
race_1 = race[mask]
len_1 = len(race_1)    # Count of race 1

mask = race == 2
race_2 = race[mask]
len_2 = len(race_2)    # Count of race 2

mask = race == 3
race_3 = race[mask]
len_3 = len(race_3)    # Count of race 3

mask = race == 4
race_4 = race[mask]
len_4 = len(race_4)    # Count of race 4

print("Race Code 0 - Amer-Indian-Eskimo Population : ",len_0)
print("Race Code 1 - Asian-Pac-Islander Population : ",len_1)
print("Race Code 2 - Black Population : ",len_2)
print("Race Code 3 - Other Population : ",len_3)
print("Race Code 4 - White Population : ",len_4)

# Minority Race
populations = [len_0,len_1,len_2,len_3,len_4]
minority_race = populations.index(min(populations))
print("Minority Race Code : ",minority_race)

# Finding Average working hours of Senior Citizens

senior_citizens = census[age>60]

working_hours_sum = np.sum(senior_citizens[:,6])            # Working hours

senior_citizens_len = len(senior_citizens)

avg_working_hours = working_hours_sum / senior_citizens_len # Average Working hours

print("Working Hours of Senior Citizens : ",working_hours_sum)
print("Average Working Hours of Senior Citizens : {:.2f}".format(avg_working_hours))

# Analyzing High Education gets High Pay

high = census[census[:,1]>10]        # Higher Education

low = census[census[:,1]<=10]        # Low Education

avg_pay_high = np.mean(high[:,7])    # Average Pay for High Education

avg_pay_low = np.mean(low[:,7])      # Average Pay for Low Education

print("Average Pay for Higher Education : {:.2f}".format(avg_pay_high))
print("Average Pay for Low Education : {:.2f}".format(avg_pay_low))


