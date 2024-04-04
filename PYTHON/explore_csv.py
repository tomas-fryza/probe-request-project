try:
    import pandas as pd
    import glob  # Filename pattern matching
except ImportError as e:
    print(f"[!] ImportError: {e}")
    raise SystemExit(1)

path = "../DATA/sc6-61/_CSV/position_1/"
dates = "2024-03-"

# Load selected *.csv files into a DataFrame
csv_files = glob.glob(path + "*" + dates + "*.csv")
csv_files = sorted(csv_files)
df = pd.concat(
    (pd.read_csv(filename, sep=";", decimal=".") for filename in csv_files),
    ignore_index=True
)

# Convert timestamp to pandas datetime object
df["datetime"] = pd.to_datetime(df["datetime"])

print(f"Number of files: {len(csv_files)}")
print(f"Number of probe requests: {len(df):,}")

# Print basic information about a DataFrame
print("\nInfo:")
print(df.info())

# Print all columns of the first 5 lines of dataframe
pd.set_option('display.max_columns', None)
print("\nHead:")
print(df.head())
print("\nTail:")
print(df.tail())
