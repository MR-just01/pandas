import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
n = 500
dates = pd.date_range("2024-01-01", periods=365).to_series().sample(n, replace=True).values
data = pd.DataFrame({
    "order_id": np.arange(1, n+1),
    "date": dates,
    "customer_id": np.random.randint(1, 200, size=n),
    "city": np.random.choice(["Mumbai","Delhi","Bengaluru","Kolkata","Chennai"], size=n),
    "category": np.random.choice(["Electronics","Clothing","Groceries"], size=n),
    "quantity": np.random.randint(1, 5, size=n),
    "unit_price": np.round(np.random.uniform(50, 5000, size=n), 2)
})

data.to_csv("salesdata.csv" , index = False)
print("salesdata.csv is created.")

#Read the csv file 

df = pd.read_csv("salesdata.csv")
