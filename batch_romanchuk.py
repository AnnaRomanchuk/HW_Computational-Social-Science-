import pandas as pd
df = pd.read_csv("batch - batch.csv")
pd.set_option('display.max_columns', None)
print(df)