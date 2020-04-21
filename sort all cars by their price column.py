import pandas as pd
df = pd.read_csv("data\Automobile_data.csv")
df = df.sort_values(by=['price'],ascending=True)
print(df)
