import pandas as pd

df = pd.read_csv("APD_Incident_Extract_2010.csv")
df.columns = ["id", "crime", "date", "time", "ltype", "address", "lng", "lat", "loc"]
df = df[["crime", "time"]]
#print(df)

g = df.groupby("crime").size().to_frame(name='count')
#g = df.groupby("crime").count().to_frame(name='count') #cannot use .count() since AttributeError: 
                                                        #'DataFrame' object has no attribute 'to_frame'
g = g.sort_values(by='count', ascending=0).head(5)
print("Here are top 5 crimes:")
print (g)


while True:
    crime = input("Enter Crime: ")    
    
    if crime == "EXIT":
        break;
        
    xaxis = range(24)
    data = []
    labels = []
    
    hNum = 0
    hTime = 0
    lNum = 99999999
    lTime = 0
    
    for time in xaxis:
        sTime = time * 100
        eTime = sTime + 100
        f = df[((df.crime == crime) | (crime == "ALL")) & (df.time >= sTime) & (df.time < eTime)]
        count = len(f)
        
        if count > hNum:
            hNum = count
            hTime = sTime
        
        if count < lNum:
            lNum = count
            lTime = sTime
        
        data.append(count)
        labels.append(str(sTime) + "-" + str(eTime))
    
    print("Crime Rate Report for " + crime)
    print("Lowest between " + str(lTime) + " and " + str(lTime + 100) + ".")
    print("Highest between " + str(hTime) + " and " + str(hTime + 100) + ".")
    
    import matplotlib.pyplot as plt
    plt.plot(xaxis, data)
    plt.xticks(xaxis, labels, rotation='vertical')
    plt.show()


print("Thank you! Bye Bye!")



