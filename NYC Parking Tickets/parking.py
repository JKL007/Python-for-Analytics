#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 06:59:45 2021

@author: juliannake...kejin
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#step1: Read the file and print out the number of records read.
df = pd.read_csv("nyc_parking_tickets.csv")
print("Step1: Reading file...")
print(len(df), "records were read from file.")


#Step2 Remove any row where Registration_State, Plate_Type, Vehicle_Make, Vehicle_Year, or
#Issuer_Code is invalid. Also only allow rows where Vehicle Year is less than 2018.
"""
df.Vehicle_Make.replace('', np.nan, inplace = True)
df.dropna(subset=['Vehicle_Make'], inplace = True)
print(df)
"""
df = df[
        (df.Vehicle_Year < 2018) &
        (df.Registration_State != 99) &
        (df["Plate_Type"] != 999) &
        (df["Vehicle_Make"] != "") &
        (df["Issuer_Code"] > 99999) &
        (df.Vehicle_Year >= 1900) 
        ]
print("\nStep2: Cleaning up...")
print(len(df), "records left after cleanup.")


#Step 3: Display a graph that shows # of tickets for each vehicle year.
print("\nStep3: # of tickets by vehicle year...")
x, y = [], []
minYear, maxYear = min(df.Vehicle_Year), max(df.Vehicle_Year)
for year in range(minYear, maxYear+1):
    ff = df[df.Vehicle_Year == year]
    x.append(year)
    y.append(ff.count())
    
plt.plot(x, y)
plt.xticks(np.arange(1980, 2018, 5))
plt.show()  


#step4 Display the top 5 vehicle-makes with the most tickets.
print("\nStep4: Top 5 vehicle-makes with most tickets...")
#method1: note ascending must be boolean
print(df.groupby("Vehicle_Make")["Vehicle_Year"].apply(lambda x: x.count()).sort_values(ascending=False).head(5))

"""
#method 2: note must have by=... argument
a = df.groupby("Vehicle_Make").count()
print(a.sort_values(by=["Vehicle_Year"], ascending=0).head(5)) #will print all columns, need to get 2
"""


#Step5 display the street where commercial vehicles got the most ticket.
print("\nStep5: The street where commercial vehicles got the most ticket:")
print(df[df.Plate_Type == "COM"].groupby("Street_Name")["Vehicle_Year"].apply(lambda x: x.count())
      .sort_values(ascending=False).head(1))
      

#Step6.1 display the state whose average vehicle year is the newest.
print("\nStep6.1: The state with newest vehicles:")
print(df.groupby(df.Registration_State)["Vehicle_Year"].apply(lambda x: x.mean()).sort_values(ascending=False).head(1))

#Step6.2 display the state whose average vehicle year is the oldest.
print("\nStep6.2: The state with oldest vehicles:")
print(df.groupby(df.Registration_State)["Vehicle_Year"].apply(lambda x: x.mean()).sort_values().head(1))
