import pandas as pd
import sys

a = pd.read_csv(sys.argv[1])
b = pd.read_csv(sys.argv[2])

diff = pd.concat([a, b]).drop_duplicates(keep=False)
print("Differences:\n", diff)
