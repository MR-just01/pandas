import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "name " : ["Ava", "Emma" , "cam"],
    "age" : [21, 34, 12],
    "score" : [99 , 79 , 90]


})

ages = df["age"]  ##selecting a single column
multiple = df[["age" ,"score"]]
print(multiple)
print("ages : ")
print(ages)

print(df)