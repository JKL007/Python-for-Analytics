#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 11:32:52 2021

@author: juliannake...kejin
"""
import pandas as pd
import matplotlib.pyplot as plt 

#Step 1 [30]: Read file and display the number of rows in the data.
print("Step 1\n================")
df = pd.read_csv("smokers.csv")
print("# of Surveys:", len(df))


#Step 2 [30]: Find and display the average number of surveys conducted per state.
print("\nStep 2\n================")
statesNum = df.groupby("State").count()
print("# of States: ", len(statesNum))
print("Average # of Surveys per state:", len(df) / len(statesNum))


#Step 3 [30]: Among the surveys in the data-set, display the minimum and maximum smoking rate.
print("\nStep 3\n================")
print("Minimum Recorded Cigarette Use:")
minIdx = df.Value.idxmin()
print(df.loc[minIdx])
print("\nMaximum Recorded Cigarette Use:")
maxIdx = df.Value.idxmax()
print(df.loc[maxIdx])


#Step 4 [30]: Find average smoker rate per state and display the states with minimum and maximum average.
print("\nStep 4\n================")
print("Least Cigarette Use State:")
statesData = df.groupby(df.State).mean().reset_index()
#print(statesData)
leastIdx = statesData.Value.idxmin()
print(statesData.loc[leastIdx].State, statesData.loc[leastIdx].Value)
print("\nMost Cigarette Use State:")
mostIdx = statesData["Value"].idxmax()
print(statesData.loc[mostIdx].State, statesData.loc[mostIdx].Value)


#Step 5 [40]: Same as Step 4 but display the top 10 states instead of min and max.
print("\nStep 5\n================")
top10States= statesData.sort_values(by = ["Value"], ascending = False).head(10)     #cannot use statesData.Value as the argument of by =
print(top10States)


#Step 6 [40]: Get state and year from the user and display the surveys for that state for that year.
print("\nStep 6\n================")
state = input("State: ")
year = int(input("Enter Year: ")) #Note: need to change to Integer!!!
ff = df[(df["State"] == state) & (df["Year"] == year)]
print("Found", len(ff), "surveys:")
print(ff)



#Step 7 [50]: Get state from user as input (using input()) and display the average smoker rate year by year. By
#looking at the most recent 2 years, display if the cigarette use is on decline or rise.
print("\nStep 7\n================")
while True:
    state = input("Enter State: ")
    
    if state == "Exit":
        print("Bye bye!")
        break
    
    if state not in df.State.tolist():
        print("hmmm... cannot find that state.")
    else:
        gf = df[df["State"] == state].groupby("Year").Value.mean() #.Value() can be either before or after.mean()
        
        """
        gf = df[df["State"] == state].groupby("Year").mean()
        x, y = [], []
        yearList = gf.index.tolist() #note: .index refers to the original "Year" column since it was groupby "Year"
        valueList = gf.Value.tolist()
        for i in range(min(gf.index), max(gf.index) + 1, 2):  
            if i in yearList:
                x.append(i)
                yData = gf.loc[i].Value 
                #yData = valueList[yearList.index(i)]
                y.append(yData)
        print(x, y)   
        plt.plot(x, y)
        
        plt.show()
        
        if valueList[-1] > valueList[-2]:
            trend = "rise"
        elif valueList[-1] < valueList[-2]:
            trend = "decline"
        else:
            trend = "not changing"
        print("Cigarette use is on", trend, "in", state)
        """
        
        plt.plot(gf)  #only input y axis is fine for this question!!!!
        plt.show()
      
        if gf.iloc[-1] > gf.iloc[-2]:
            trend = "rise"
        elif gf.iloc[-1] < gf.iloc[-2]:
            trend = "decline"
        else:
            trend = "not changing"
        print("Cigarette use is on", trend, "in", state)
       
    print("Computer for another state or enter 'Exit' to exit.")
    
        
    


    
