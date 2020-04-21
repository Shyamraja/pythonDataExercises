import pandas as pd
df = pd.read_csv("data\Automobile_data.csv")
car_manufacturers = df.groupby('company')
Pricedf = car_manufacturers['company','price'].max()
print(Pricedf)

