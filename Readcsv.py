import pandas as pd

df = pd.read_csv("data.csv")
# print(df.to_string())
#to_String() is used to print the entire dataframe in the table


# print(pd.options.display.max_rows) #to check the maximum number of rows with this


pd.options.display.max_rows = 3
print(df)