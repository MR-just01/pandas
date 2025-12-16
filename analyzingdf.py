#head() : this function is returns the header and a specified number of rows , starting form the top
import pandas as pd 
df= pd.read_json("data.json")
print(df.head(10)) #prints first 10 rows of the dataframe


#tail() is the function that returns specifies number of rows starting from the bottom 

print("*******using the trail function********")
print(df.tail()) #prints the last 5 rows of the df
print(df.tail(3)) #prints the last 3 rows
print()

#informationn about the dataframe
print(df.info())