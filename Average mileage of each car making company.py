import pandas as pd
df = pd.read_csv("data\Automobile_data.csv")
car_manufacturers = df.groupby('company')
Mileagedf = car_manufacturers['company','average-mileage'].mean()
print(Mileagedf)
