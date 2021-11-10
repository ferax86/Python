# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:12:08 2021

@author: XRFRBL
"""
####1.Data Type Constraints


import pandas as pd
sales = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\3.Cleaning Data with Python\sales.csv",sep=";")
sales.head(2)

#When working with new data, you should always check the data types 
#of your columns using the .dtypes attribute or the .info() method 

sales.dtypes # Get data types of columns
sales["Revenue_text"]=sales["Revenu"].astype("str") #Integers to String
sales.info()
sales["Time of purchase"]=sales["Time of purchase"].str.strip("min") #remove min 
sales.info()
sales['Revenue_text'].sum() #since the variable is a string the sum concatenate the values
sales["Revenue_text"]=sales["Revenu"].astype("int") # String to Integers
sales['Revenue_text'].sum()
sales['Revenue_text'].describe()

assert sales['Revenue_text'].dtype == 'int' ## Verify that Revenue_text is now an integer
assert 1+1 == 3 # This will not pass


movies = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\3.Cleaning Data with Python\movies.csv",sep=";")
movies.head()
import matplotlib.pyplot as plt
plt.hist(movies["Average Rating "])
plt.title('Average rating of movies (1-5)') #we have one outlier (6 as average rating)


###How to deal with out of range data?

# Output Movies with rating > 5
movies[movies["Average Rating "] > 5]

# Drop values using filtering
movies = movies[movies["Average Rating "] <= 5]

# Drop values using .drop()
movies.drop(movies[movies["Average Rating "] > 5].index, inplace = True)

# Convert avg_rating > 5 to 5
movies.loc[movies["Average Rating "] > 5, "Average Rating "] = 5

# Assert results
assert movies["Average Rating "].max() <= 5


###Date range example

import datetime as dt
user_signups = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\3.Cleaning Data with Python\user_signups.csv",sep=";")
user_signups.head()

# Output data types
user_signups['subscription_date'].dtypes

# Convert to DateTime
user_signups['subscription_date'] = pd.to_datetime(user_signups['subscription_date'])
user_signups.dtypes
print(user_signups['subscription_date'] )


# Assert that conversion happened
assert user_signups['subscription_date'].dtype == 'datetime64[ns]'


today_date = dt.date.today()
type(today_date)
print(today_date)

today_date =pd.to_datetime(today_date)
type(today_date)
print(today_date)
##First scenario in fixing date outlier: DROP THE DATATA

# Drop values using filtering
user_signups = user_signups[user_signups['subscription_date'] < today_date]
# Drop values using .drop()
user_signups.drop(user_signups[user_signups['subscription_date'] > today_date].index, inplace = True)


##Second scenario in fixing date outlier: HARDCORE DATES WITH UPPER LIMIT

# Drop values using filtering
user_signups.loc[user_signups['subscription_date'] > today_date, 'subscription_date'] = today_date
# Assert is true
assert user_signups.subscription_date.max().date() <= today_date

####Uniqueness of constraints


height_weight = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\3.Cleaning Data with Python\height_weight.csv",sep=";")
height_weight.head()

duplicates = height_weight.duplicated() # Get duplicates across all columns
print(duplicates)

height_weight[duplicates] # Get duplicate rows


column_names_subset_1 = ['Name','Surname','Address']
column_names_subset_2 = ['Name','Surname',]
column_names_subset_3 = ['Name','Address']

## Get duplicates across a subset of columns 
duplicates_subset_1=height_weight.duplicated(subset = column_names_subset_1, keep = False)
duplicates_subset_2=height_weight.duplicated(subset = column_names_subset_2, keep = False)
duplicates_subset_3=height_weight.duplicated(subset = column_names_subset_3, keep = False)
duplicates_subset_4=height_weight.duplicated(subset = column_names_subset_3, keep = 'first') #keep first duplicate value
duplicates_subset_5=height_weight.duplicated(subset = column_names_subset_3, keep = 'last')  #keep last duplicate value


# Output duplicate values
height_weight[duplicates_subset_1]
height_weight[duplicates_subset_2]
height_weight[duplicates_subset_3]
height_weight[duplicates_subset_1].sort_values(by ='Name')


##How to treat duplicate values?

# Drop duplicates
height_weight.drop_duplicates(inplace = True) 


# Group by column names and produce statistical summaries

column_names = ['Name','Surname','Address']
summaries = {'Height': 'max', 'Weight': 'mean'}
height_weight = height_weight.groupby(by = column_names).agg(summaries).reset_index() 
print(height_weight)

# Make sure aggregation is done
duplicates = height_weight.duplicated(subset = column_names, keep = False)
height_weight[duplicates].sort_values(by = 'Name')  #NO DUPLICATE ANYMORE



####2.Membership Constraints

study_data = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\3.Cleaning Data with Python\study_data.csv",sep=";")
study_data

categories = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\3.Cleaning Data with Python\categories.csv",sep=";")
categories


# Print unique values of blood_type columns in study_data

print('Blood type: ', study_data['blood_type'].unique(), "\n")


#Finding inconsistent categories
inconsistent_categories = set(study_data['blood_type']).difference(categories['blood_type'])
print(inconsistent_categories)

# Get and print rows with inconsistent categories

inconsistent_rows = study_data['blood_type'].isin(inconsistent_categories)
study_data[inconsistent_rows]


#Dropping inconsistent categories and get consistent data only

consistent_data = study_data[~inconsistent_rows]


#Value Consistency

demographics = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\3.Cleaning Data with Python\demographics.csv",sep=";")
demographics

# Get marriage status column
marriage_status = demographics['marriage_status']
marriage_status.value_counts()

# Get value counts on DataFrame
demographics.groupby('marriage_status').count()

# Capitalize

demographics['marriage_status'] = demographics['marriage_status'].str.upper()
demographics['marriage_status'].value_counts()


# Lowercase

demographics['marriage_status'] = demographics['marriage_status'].str.lower()
demographics['marriage_status'].value_counts()



#Trailing spaces

demographics_1 = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\3.Cleaning Data with Python\demographics_1.csv",sep=";")
marriage_status = demographics_1['marriage_status']
marriage_status.value_counts()

# Strip all spaces
demographics_1['marriage_status_nospace'] = demographics_1['marriage_status'].str.strip()
demographics_1['marriage_status_nospace'] .value_counts()


#Collapsing data into categories
#a) Create categories out of data
import pandas as pd
import numpy as np

# Using qcut()
group_names = ['0-200K', '200K-500K', '500K+']
demographics['income_group'] = pd.qcut(demographics['household_income'], q = 3,labels = group_names)
demographics[['income_group', 'household_income']]

# Using cut() - create category ranges and names
ranges = [0,200000,500000,np.inf]
group_names = ['0-200K', '200K-500K', '500K+']
demographics['income_group'] = pd.cut(demographics['household_income'], bins=ranges,labels=group_names)
demographics[['income_group', 'household_income']]





#b) Map categories to fewer ones:

devices = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\3.Cleaning Data with Python\Operating Systems.csv",sep=";")
devices

# Create mapping dictionary and replace
mapping = {'Microsoft':'DesktopOS', 'MacOS':'DesktopOS', 'Linux':'DesktopOS','IOS':'MobileOS', 'Android':'MobileOS'}
devices['operating_system'] = devices['operating_system'].replace(mapping)
devices['operating_system'].unique()




####Cleaning Text Data

phones = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\3.Cleaning Data with Python\phones.csv",sep=";")
print(phones)



# Replace "?" with "00"
phones["Phone number"] = phones["Phone number"].str.replace("?","00") 
phones

# Replace "-" with nothing

phones["Phone number"] = phones["Phone number"].str.replace("-","") 
phones


# Replace phone numbers with lower than 10 digits to NaN

digits = phones['Phone number'].str.len() 
print(digits)
phones.loc[digits <10,"Phone number"] = np.nan 
phones

# Find length of each row in Phone number column
sanity_check = phones['Phone number'].str.len()

# Assert minmum phone number length is 10
assert phones['Phone number'].str.len().min() >= 10
#ou
assert sanity_check.min() >= 10

# Assert all numbers do not have "+" or "-"
assert phones['Phone number'].str.contains("+|-").any() == False


#More Complicated example 

phones_1 = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\3.Cleaning Data with Python\phones_1.csv",sep=";")
print(phones_1)

# Replace letters with nothing(Regular expressions in action)

phones_1['Phone number'] = phones_1['Phone number'].str.replace(r'\D+', '')#
phones_1.head()



####3. Uniformity

temperatures = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\3.Cleaning Data with Python\temperature.csv",sep=";")
print(temperatures) # probably the last value(50) is in fahreneit and not in celsius

# Import matplotlib
import matplotlib.pyplot as plt
# Create scatter plot
plt.scatter(x = 'Date', y = 'Temperature', data = temperatures)
# Create title, xlabel and ylabel
plt.title('Temperature in Celsius March 2019 - NYC')
plt.xlabel('Dates')
plt.ylabel('Temperature in Celsius')
# Show plot
plt.show()

# Treating temperature data
temp_fah = temperatures.loc[temperatures['Temperature'] > 40, 'Temperature'] #the.loc method gives the specific temperature values greater than 40 not eh whole rows of data(as in the next row)
print(temp_fah)
temp_fah_1=temperatures[temperatures['Temperature'] > 40]
print(temp_fah_1)

temp_cels = (temp_fah - 32) * (5/9)
temp_cels


temperatures.loc[temperatures['Temperature'] > 40, 'Temperature'] = temp_cels
print(temperatures)


# Treating date data

birthdays = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\3.Cleaning Data with Python\birthdays.csv",sep=";")
print(birthdays)
birthdays.dtypes

# Converts to datetime - but won't work!
birthdays['Birthday'] = pd.to_datetime(birthdays['Birthday'])

# Will work!
birthdays['Birthday'] = pd.to_datetime(birthdays['Birthday'],infer_datetime_format=True, # Attempt to infer format of each date
errors = 'coerce')                                                                       # Return NA for rows where conversion failed

print(birthdays)
birthdays.dtypes

birthdays['Birthday'] = birthdays['Birthday'].dt.strftime("%d-%m-%Y")
birthdays.head()


### Cross field validation

flights = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\3.Cleaning Data with Python\flights.csv",sep=";")
print(flights)

sum_classes = flights[['economy_class', 'business_class', 'first_class']].sum(axis = 1) #axis=1 -->sum by row
print(sum_classes)

passenger_equ = sum_classes == flights['total_passengers']
print(passenger_equ)

# Find and filter out rows with inconsistent passenger totals
inconsistent_pass = flights[~passenger_equ]
consistent_pass = flights[passenger_equ]

users = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\3.Cleaning Data with Python\users.csv",sep=";")
print(users)

import datetime as dt

# Convert to datetime and get today's date
users['Birthday'] = pd.to_datetime(users['Birthday'])
print(users['Birthday'] )
today = dt.date.today()
type(today)
print(today)

# For each row in the Birthday column, calculate year difference
age_manual = today.year - users['Birthday'].dt.year
print(age_manual)

# Find instances where ages match
age_equ = age_manual == users['Age']
print(age_equ)
# Find and filter out rows with inconsistent age
inconsistent_age = users[~age_equ]
consistent_age = users[age_equ]




### Completeness

airquality = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\3.Cleaning Data with Python\airquality.csv",sep=";")
print(airquality)

# Return missing values
airquality.isna()

# Get summary of missingness
airquality.isna().sum()

import missingno as msno
import matplotlib.pyplot as plt
# Visualize missingness
msno.matrix(airquality)
plt.show()



# Isolate missing and complete values aside
missing = airquality[airquality['CO2'].isna()]
complete = airquality[~airquality['CO2'].isna()]


# Describe complete DataFramee
complete.describe()
# Describe missing DataFramee
missing.describe()

##How to deal with missing value 
# 1.Drop missing values
airquality_dropped = airquality.dropna(subset = ['CO2'])
airquality_dropped.head(10)

#2.Replacing with statistical measures
co2_mean = airquality['CO2'].mean()
airquality_imputed = airquality.fillna({'CO2': co2_mean})
airquality_imputed.head()



####4. Comparing Strings-->TO DO BUT SEEMS NOT NECESSARY

from fuzzywuzzy import fuzz

fuzz.WRatio('Reeding', 'Reading')


