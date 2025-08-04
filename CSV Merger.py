import pandas as pd
import glob

files = glob.glob("*.csv")
df_list = [pd.read_csv(f) for f in files]
combined = pd.concat(df_list, ignore_index=True)
combined.to_csv("merged.csv", index=False)
print("Merged", len(files), "CSV files into merged.csv")
