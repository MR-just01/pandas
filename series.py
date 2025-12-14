import pandas as pd

a = [1,2,3,42,1]

#series is the like column in the dataframe 
myvar = pd.Series(a)
print(myvar)

#LABLES 

ar = [1,2,3]
myvari = pd.Series(ar,index = ["a","b" ,"c"])
print(myvari)


#creatin the simple series from dict

week = {"mon " : 1,
        "tue"  : 2,
        "wed" : 3, 
        "thu" : 4}

myweek = pd.Series(week)
print(myweek)