import pandas as pd

filename = "../DATA/sc6-61/_CSV/position_1/sc6-61_2024-02-07_ver-99.csv"
df = pd.read_csv(filename, sep=";", decimal=".")

print(f"Number of probe requests: {len(df):,}")

# Print basic information about a DataFrame
print(df.info())

# Print all columns of the first 5 lines of dataframe
pd.set_option('display.max_columns', None)
print(df.head())
