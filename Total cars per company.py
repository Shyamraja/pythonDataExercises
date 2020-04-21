import pandas as pd
df = pd.read_csv("data\Automobile_data.csv")
countdf=df['company'].value_counts()
print(countdf)
