# 11. Read CSV
import pandas as pd
df = pd.read_csv("data.csv")

# 12. Read Excel
df = pd.read_excel("file.xlsx")

# 13. Filter rows
df[df['age'] > 30]

# 14. GroupBy
df.groupby('department')['salary'].mean()

# 15. Drop missing values
df.dropna()

# 16. Fill missing values
df.fillna(0)

# 17. Rename columns
df.rename(columns={"old": "new"})

# 18. Export to Excel
df.to_excel("output.xlsx")

# 19. JSON to dict
import json
data = json.loads('{"a":1}')

# 20. Dict to JSON
json.dumps({'a':1})
