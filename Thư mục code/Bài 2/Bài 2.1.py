import pandas as pd

df = pd.read_csv('results.csv')
df.iloc[:, 5:] = df.iloc[:, 5:].replace(',', '', regex=True).apply(pd.to_numeric, errors='coerce')

for x in df.columns[4:]:
    tmp = df[['Name', x]].sort_values(x).dropna()
    
    top_3_highest = tmp.tail(3)[::-1]
    top_3_lowest = tmp.head(3)
    
    print(f'Top 3 cầu thủ có chỉ số {x} cao nhất:')
    for _, row in top_3_highest.iterrows():
        print(f"{row['Name']:^20} | {row[x]:<5}")
    print()
    
    print(f'Top 3 cầu thủ có chỉ số {x} thấp nhất:')
    for _, row in top_3_lowest.iterrows():
        print(f"{row['Name']:^20} | {row[x]:<5}")
    print()
