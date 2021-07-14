# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)

#Code starts here

# Checking the Categorical and Numerical variables in Bank Data
categorical_var = bank_data.select_dtypes(include='object')
print(categorical_var)

numerical_var = bank_data.select_dtypes(include='number')
print(numerical_var)

# Checking the missing values in Bank Data and filling with mode
banks = bank_data.drop(['Loan_ID'],axis=1)

banks.isnull().sum()

banks_mode = banks.mode().iloc[0]

banks.fillna(value = banks_mode, inplace=True)

banks.isnull().sum().values.sum()

# Checking the loan amount of an average person
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')

# Checking the percentage of loan approved based on a person's employment type
loan_approved_se = len(banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')])
loan_approved_nse = len(banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')])

percentage_Se = loan_approved_se/614*100
percentage_nSe = loan_approved_nse/614*100

# Checking the applicants with long loan amount term
loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)

big_loan_term = len(loan_term[loan_term >= 25])

# Checking average income of an applicant and the average loan given to a person based on income
loan_groupby = banks.groupby('Loan_Status')

loan_groupby = loan_groupby['ApplicantIncome','Credit_History']

mean_values = loan_groupby.mean()

#Code ends here



