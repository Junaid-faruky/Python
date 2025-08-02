import pandas as pd
import sys

df = pd.read_csv(sys.argv[1])
print("Columns:", df.columns.tolist())
print("Basic stats:\n", df.describe())
print("Null counts:\n", df.isnull().sum())
