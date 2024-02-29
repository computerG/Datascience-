

## Import libraries
import os
import pandas as pd
import numpy as np
import statistics
# read the csv file

current_file = os.path.abspath(os.path.dirname(__file__))

print("The current file",current_file)
csv_filename = os.path.join(current_file, './Inc_Exp_Data.csv')
#read the dataset
household_df = pd.read_csv(csv_filename)
##get the first 5 data



household_df_numeric = household_df[['Mthly_HH_Income','Mthly_HH_Expense',
                   'No_of_Fly_Members','Emi_or_Rent_Amt',
                   'Annual_HH_Income',                   
                   'No_of_Earning_Members']]


print("===VARIANCE===")
print(household_df_numeric.var(axis=0).round(2))
print("===STANDARD DEVIATION===")
print(household_df_numeric.std(axis=0).round(2))

print("===MEAN===")
print(household_df_numeric.mean().round(2))
print("===MEDIAN===")
print(household_df_numeric.median().round(2))
print("===MODE===")
print(household_df_numeric.mode().round(2))



#get summary statistics for Mthly_HH_Income,Mthly_HH_Expense,
#No_of_Fly_Members,Emi_or_Rent_Amt,Annual_HH_Income,
#Highest_Qualified_Member,No_of_Earning_Members

descriptive_statistics_df = household_df[['Mthly_HH_Income','Mthly_HH_Expense',
                   'No_of_Fly_Members','Emi_or_Rent_Amt',
                   'Annual_HH_Income',
                   
                   'No_of_Earning_Members']].describe().round(2)
descriptive_statistics_df.to_csv("descriptive_statistics_df.xls")


# get multiple mode

multiple_mode = household_df['Mthly_HH_Income'].value_counts()
res = multiple_mode.head(1)


print("Mode CALC " , res)

##get multimode using statistics module
multumode = statistics.multimode(household_df['No_of_Fly_Members'
                  ])
print(multumode)

level_education = household_df.groupby('Highest_Qualified_Member')['Highest_Qualified_Member']
print (level_education.count())