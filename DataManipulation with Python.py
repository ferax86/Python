# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 15:33:47 2021

@author: XRFRBL
"""
###1.Introducing a dataframe
#Exploring a Dataframe

import pandas as pd
dogs = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\2.Data Manipulation with pandas\Pandas DataFrame.csv",sep=";")
print(dogs)
dogs.dtypes

dogs["DateofBirth"]=pd.to_datetime(dogs["DateofBirth"])
dogs.dtypes

dir=r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\2.Data Manipulation with pandas\Pandas DataFrame.csv"
dogs_new=pd.read_csv(dir,sep=";")
print(dogs_new)

dogs.head()
dogs.head(3)
dogs.dtypes
dogs.info()
dogs.shape
dogs.describe()
dogs.values
dogs.columns
dogs.columns[-1]
dogs.columns[1]
dogs.index
dogs.index[1]

#%%
#Sorting 

dogs.sort_values("Weight(kg)")
dogs.sort_values("Weight(kg)",ascending=False) #descending order
dogs.sort_values(["Weight(kg)","Height(cm)"]) #multiple variable
dogs.sort_values(["Weight(kg)","Height(cm)"],ascending=[True, False])

#Subsetting
dogs["Name"] #single column
dogs[["Breed", "Height(cm)"]] #multiple columns(1st method)
cols_to_subset = ["Breed", "Height(cm)"]
dogs[cols_to_subset] #multiple columns(2nd method)

dogs["Height(cm)"] > 50 #subsetting rows
dogs[dogs["Height(cm)"] > 50]


dogs[dogs["Breed"] == "Labrador"] #subset based on text data
dogs[dogs["DateofBirth"] > "01/01/2015"]  #subset based on DATES
type(dogs["DateofBirth"] )
dogs[ (dogs["Breed"] == "Labrador") & (dogs["Color"] == "Brown") ] #subset based on multiple conditions 
is_black_or_brown = dogs["Color"].isin(["Black", "Brown"])
dogs[is_black_or_brown]
subset= [50,18,59]
dogs[dogs["Height(cm)"].isin(subset)]
#%%


#New Columns

dogs["Height(m)"] = dogs["Height(cm)"] / 100
print(dogs)

dogs["bmi"] = dogs["Weight(kg)"] / dogs["Height(m)"] ** 2 #** is the exp operator
print(dogs.head()) #mass index formula

bmi_lt_100 = dogs[dogs["bmi"] < 100]
print(bmi_lt_100) 
bmi_lt_100_height = bmi_lt_100.sort_values("Height(m)", ascending=False)
print(bmi_lt_100_height)
bmi_lt_100_height[["Name", "Height(m)", "bmi"]] #Multiple Manipulations






#%%


###2.Summary statistics

#Numerical data
dogs["Height(cm)"].mean()
dogs["Height(cm)"].median()
dogs["Height(cm)"].mode()
dogs["Height(cm)"].min()
dogs["Height(cm)"].max()
dogs["Height(cm)"].var()
dogs["Height(cm)"].std()
dogs["Height(cm)"].sum()
dogs["Height(cm)"].quantile()

#Dates
dogs["DateofBirth"].min()
dogs["DateofBirth"].max()

#the .agg() method

def pct30(column):
    return column.quantile(0.3)

dogs["Weight(kg)"].agg(pct30)
dogs["Weight(kg)"].quantile(0.3) 


dogs[["Weight(kg)", "Height(cm)"]].agg(pct30) #Multiple columns


def pct40(column):
    return column.quantile(0.4)

def mediana(column):
    return column.median()

dogs["Weight(kg)"].agg([pct30,pct40,mediana]) #multiple summaries (30 , 40th percentile and median)

#Multiple summaries on multiple columns
import numpy as np
dogs[["Weight(kg)", "Height(cm)"]].agg([pct30,mediana])


#Cumulative statistics
dogs["Weight(kg)"]
dogs["Weight(kg)"].cumsum()
dogs["Weight(kg)"].cummax()
dogs["Weight(kg)"].cummin()
dogs["Weight(kg)"].cumprod()
#%%


###3.Counting

dogs.drop_duplicates(subset="Name") #dropping duplicates name
unique_dogs=dogs.drop_duplicates(subset=["Name","Breed"]) #dropping duplicates pairs
dogs["Breed"].value_counts()
dogs["Breed"].value_counts(sort=True)
dogs["Breed"].value_counts(normalize=True) #byproportion

#%%

###4.Grouped summary statistics

dogs[dogs["Color"] == "Black"]["Weight(kg)"].mean()
dogs[dogs["Color"] == "Brown"]["Weight(kg)"].mean()

dogs.groupby("Color")["Weight(kg)"].mean()
dogs.groupby("Color")["Weight(kg)"].agg([min, max, sum])
dogs.groupby("Color")["Weight(kg)"].agg([np.min, np.max, np.sum,np.mean, np.median]) #when use mean or median need to specify np 

#%%


dogs.groupby(["Color","Breed"])["Weight(kg)"].mean() #groupipng by multiple variables
dogs.groupby(["Color","Breed"])[["Weight(kg)","Height(cm)"]].mean() 


###5. Pivot tables
#In pandas, pivot tables are essentially just another way of performing grouped calculations. 
#That is, the .pivot_table() method is just an alternative to .groupby().

#Pivot on one variable
dogs.groupby("Color")["Weight(kg)"].mean()
dogs.pivot_table(values="Weight(kg)",index="Color") #the same as previous line 
dogs.pivot_table(values="Weight(kg)", index="Color", aggfunc=np.median) #Different statistics(median)
dogs.pivot_table(values="Weight(kg)", index="Color", aggfunc=[np.mean, np.median]) #Multiple statistics

#Pivot on two variables

dogs.groupby(["Color", "Breed"])["Weight(kg)"].mean()
dogs.pivot_table(values="Weight(kg)", index="Color", columns="Breed")
dogs.pivot_table(values="Weight(kg)", index="Color", columns="Breed", fill_value=0) #Fill NA 
dogs.pivot_table(values="Weight(kg)", index="Color", columns="Breed", fill_value=0,margins=True) #summing with Pivot Tables

#%%
###6. Explicit indexes

dogs.columns
dogs.index
print(dogs)
dogs_ind = dogs.set_index("Name")#Setting a column as the index
print(dogs_ind)
dogs_ind.reset_index() #Removing/Resetting an index
dogs_ind.reset_index(drop=True) #Dropping an index ( in this case the Name)

dogs[dogs["Name"].isin(["Bella", "Stella"])] 
dogs_ind.loc[["Bella", "Stella"]] #Indexes make subsetting simpler

dogs_ind2 = dogs.set_index("Breed") #Index values don't need to be unique
print(dogs_ind2) 

dogs_ind2.loc["Labrador"] #Subsetting on duplicated index values

dogs_ind3 = dogs.set_index(["Breed", "Color"]) #Multi-level indexes a.k.a. hierarchical indexes
print(dogs_ind3)

dogs_ind3.loc[["Labrador", "Chihuahua"]] #Subset the outer level with a list

dogs_ind3.loc[[("Labrador", "Brown"), ("Chihuahua", "Tan")]] #Subset inner levels with a list of tuples

dogs_ind3.sort_index() #Sorting by index values(from outer to inner in descening order)
dogs_ind3.sort_index(level=["Color", "Breed"], ascending=[True, False]) #Controlling sort_index


breeds = ["Labrador", "Poodle","Chow Chow", "Schnauzer","Labrador", "Chihuahua", "St. Bernard"]
breeds[2:5] #slicing lists

#%%

###6.Slicing and subsetting with .loc and .iloc


breeds[:3]
breeds[:]

dogs_srt = dogs.set_index(["Breed", "Color"]).sort_index() #Sort the index before you slice
print(dogs_srt)

dogs_srt.loc["Chow Chow":"Poodle"] #Slicing the outer index level
dogs_srt.loc[("Labrador", "Brown"):("Schnauzer", "Grey")] #Slicing the inner index levels correctly


dogs_srt.loc[:, "Name":"Height(cm)"]  #Slicing columns

dogs_srt.loc[("Labrador", "Brown"):("Schnauzer", "Grey"),"Name":"Height(cm)"] #Slicing on both columns and rows

dogs = dogs.set_index("DateofBirth").sort_index()
print(dogs)

dogs.loc["2013-07-01":"2017-01-20"] #Slicing by dates

dogs.loc["2011":"2015"] #Slicing by Partial dates

print(dogs.iloc[2:5, 1:4]) #Subsetting by row/column number
print(dogs.iloc[:5, 1:4])
print(dogs.iloc[:5, :4])

#%%

###7.Working with Pivot tables

dogs_height_by_breed_vs_color = dogs.pivot_table("Height(cm)", 
                                index="Breed", columns="Color") 
print(dogs_height_by_breed_vs_color) #the standadard aggregation number is mean()

dogs_height_by_breed_vs_color_1 = dogs.pivot_table("Height(cm)", 
                                index=["Breed","Name"], columns="Color") 

print(dogs_height_by_breed_vs_color_1 )


dogs_height_by_breed_vs_color.loc["Chow Chow":"Poodle"] #.loc[] + slicing is a power combo


print(dogs)


dogs_height_by_breed_vs_color.mean(axis="index") #The axis argument
dogs_height_by_breed_vs_color.mean(axis="columns") #Calculating summary stats across columns

dogs["year"]=pd.DatetimeIndex(dogs["DateofBirth"]).year
dogs_weight_by_year_mean=  dogs.groupby(["year"])["Weight(kg)"].mean()
print(dogs_weight_by_year_mean[dogs_weight_by_year_mean==dogs_weight_by_year_mean.max()])

#%%
###8.Data Visualization


#Histogram
import matplotlib.pyplot as plt

dogs["Height(cm)"].hist()
plt.show()#in order to call the plot we need this line of code


dogs["Height(cm)"].hist(bins=20)
plt.show()
dogs["Height(cm)"].hist(bins=5)
plt.show()
#%%
#Bar plots

avg_weight_by_breed = dogs.groupby("Breed")["Weight(kg)"].mean()
print(avg_weight_by_breed)

avg_weight_by_breed.plot(kind="bar",title="Mean Weight by Dog Breed")
plt.show()


sully = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\2.Data Manipulation with pandas\Sully.csv",sep=";")
print(sully)
sully.head()
sully.plot(x="Date",y="Weight",kind="line")
plt.show()

sully.plot(x="Date", y="Weight", kind="line", rot=45) #Rotating axis labels
plt.show()
#%%

#Scatter plots
dogs.plot(x="Height(cm)", y="Weight(kg)", kind="scatter")
plt.show()


dogs[dogs["sexes"]=="F"]["Height(cm)"].hist() #Layering plots
dogs[dogs["sexes"]=="M"]["Height(cm)"].hist()
plt.legend(["F", "M"]) #add the legend (otherwise not possible to know in advance)
plt.show()

dogs[dogs["sexes"]=="F"]["Height(cm)"].hist(alpha=0.7) #Layering plots(with transparency)
dogs[dogs["sexes"]=="M"]["Height(cm)"].hist(alpha=0.7)
plt.legend(["F", "M"]) #add the legend (otherwise not possible to know in advance)
plt.show()
#%%

#Missing Values

dogs.isna() #Detecting missing values

dogs.isna().any() #here we see if there is at least one NA in each column
dogs.isna().sum() #counting missing values

import matplotlib.pyplot as plt
dogs.isna().sum().plot(kind="bar")
plt.show()

dogs.dropna() #Removing missing values
dogs.fillna(0) #Replacing missing values

#%%
#Creating DataFrames

#Dictionary is a way of storing data in Python; it holds a set of Key-Value pairs

my_dict = {"title": "Charlotte's Web",
           "author": "E.B. White",
           "published": 1952
           }

my_dict["title"]



#%%

#List of dictionaries - by row
list_of_dicts = [ {"name": "Ginger", 
                   "breed": "Dachshund", 
                   "height_cm": 22,
                   "weight_kg": 10, 
                   "date_of_birth": "2019-03-14"}, #HERE ENDS THE FIRST ROW
                 
                    {"name": "Scout", 
                      "breed": "Dalmatian", 
                      "height_cm": 59,
                      "weight_kg": 25, 
                      "date_of_birth": "2019-05-09"}
]

new_dogs=pd.DataFrame(list_of_dicts) #from dictionary to dataframe
print(new_dogs)
#%%

#Dictionary of lists - by column


dict_of_lists = { 
                    "Name": ["Ginger", "Scout"],
                    "Breed": ["Dachshund", "Dalmatian"],
                    "Color": ["Black", "Brown"] ,
                    "Height(cm)": [22, 59],
                    "Weight(kg)": [10, 25],
                    "DateofBirth": ["2019-03-14","2019-05-09"],
                    "sexes": ["M","F"],
} #here Key = column name and Value = list of column values

new_dogs=pd.DataFrame(dict_of_lists) #from dictionary to dataframe
print(new_dogs)

#Adding New rows to the dogs Dateframe
dogs_update= dogs.append(new_dogs, ignore_index=True)

#%%
#Reading and writing CSVs

import pandas as pd
dir="\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\Data Manipulation with pandas\Pandas DataFrame.csv"
dogs = pd.read_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\Data Manipulation with pandas\Pandas DataFrame.csv",sep=";")
#dogs_1=pd.read_csv(dir,sep=";")
print(dogs)  #CSV to a DataFrame

dogs["bmi"] = dogs["Weight(kg)"] / (dogs["Height(cm)"] / 100) ** 2
print(dogs) #DataFrame manipulation

dogs.to_csv(r"\\WWG00M.ROOTDOM.NET\BFS-HOME\XRFRBL-R0266830\Personal Doc\Python\Data Manipulation with pandas\new_dogs_with_bmi.csv",sep=";") #DataFrame to CSV 

