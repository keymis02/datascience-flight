import pandas as pd
from pandas_profiling import ProfileReport

base = pd.read_csv("Clean_Dataset.csv")

print(base)

profile = ProfileReport(base)
profile

profile.to_file("profile.html")
