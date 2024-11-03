import pandas as pd

df = pd.read_csv('results.csv')

numeric_columns = df.columns[5:]
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce').fillna(0)

stats = lambda data: {
    'Median': data.median(),
    'Mean': data.mean(),
    'Std': data.std()
}

overall_stats = {'Name': 'all', **{stat: stats(df[numeric_columns])[stat] for stat in ['Median', 'Mean', 'Std']}}
team_stats = [{'Name': team, **{stat: stats(df[df['Team'] == team][numeric_columns])[stat] for stat in ['Median', 'Mean', 'Std']}} for team in df['Team'].unique()]

results = [overall_stats] + team_stats
result_df = pd.DataFrame(results)

final_result_df = pd.DataFrame({
    'Index': range(len(result_df)),
    'Name': result_df['Name'],
    **{f'{stat} of {col}': result_df[stat].apply(lambda x: x[col]) for stat in ['Median', 'Mean', 'Std'] for col in numeric_columns}
})

final_result_df.to_csv('results2.csv', index=False)
