import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('results.csv').iloc[:, 5:8] \
            .replace('N/a', pd.NA) \
            .apply(pd.to_numeric, errors='coerce') \
            .dropna()
data_scaled = StandardScaler().fit_transform(data)

df = pd.read_csv('results.csv')
df['Cluster'] = KMeans(n_clusters=5, random_state=42).fit_predict(data_scaled)

for i in range(5):
    print(f"\n--- Cluster {i} ---\n{df[df['Cluster'] == i][['Name', 'Team', 'Cluster']].head()}\n{'-' * 40}")

plt.figure(figsize=(10, 6))
plt.scatter(data_scaled[:, 0], data_scaled[:, 1], c=df['Cluster'], cmap='viridis')
plt.title('K-means Clustering of Players')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Cluster')
plt.grid()
plt.show()
