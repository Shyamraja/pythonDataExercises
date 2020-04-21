import pandas as pd
df = pd.read_csv("data/Automobile_data.csv")
companypricedf = df[['company','price']][df.price==df['price'].max()]
print(companypricedf)

