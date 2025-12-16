import pandas as pd 
df = pd.read_csv("data.csv")

# dropna() function is used to remove the missing values fromt the dataframe 
#this function will not change the original dataframe until inplace  = True is specified 
# new_df = df.dropna()
# print(new_df.to_string())

df.dropna(inplace = True)
print(df.to_string())
print(df.info())



#REPLACE EMPTY VALUES 

#fillna() function is used tp replace empty cells with a value
#in this example we will replace empty cells with 120

df.fillna(120 , inplace = True)

print(df.to_string())


##REPLACE VALUES FOR THE SPECIFIC COLUMNS
df.fillna({"calories": "A"} , inplace = True)

print(df.to_string())
print("\n")

#REPLACE USING THE MEAN , MEDIAN OR MODE 

x = df["calories"].mean()
df.fillna({"calories":x}, inplace = True)
print(df.to_string())