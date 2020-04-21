import pandas as pd
df = pd.read_csv("data\Automobile_data.csv")
car_Manufacturers = df.groupby('company')
toyotadf = car_Manufacturers.get_group('toyota')
print(toyotadf)

