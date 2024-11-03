import pandas as pd

df = pd.read_csv(r'results.csv')
columns_to_sum = df.columns[5:]
df[columns_to_sum] = df[columns_to_sum].apply(pd.to_numeric, errors='coerce')
highest_team_stats = df.groupby('Team')[columns_to_sum].sum().idxmax()

for key, value in highest_team_stats.items():
    print(f"{key}: {value}")