import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('results.csv')
features = ['Age', 'Matches played', 'Minutes', 'Assists', 'non-Penalty Goals', 'Yellow Cards', 'Red Cards']

data_scaled = StandardScaler().fit_transform(data[features])
kmeans = KMeans(n_clusters=5, random_state=0).fit(data_scaled)
data['Cluster'] = kmeans.labels_
pca = PCA(n_components=2)
data[['PCA1', 'PCA2']] = pca.fit_transform(data_scaled)

x_min, x_max = data['PCA1'].min() - 1, data['PCA1'].max() + 1
y_min, y_max = data['PCA2'].min() - 1, data['PCA2'].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))
Z = kmeans.predict(pca.inverse_transform(np.c_[xx.ravel(), yy.ravel()])).reshape(xx.shape)

plt.figure(figsize=(12, 8))
plt.contourf(xx, yy, Z, alpha=0.5, cmap='viridis')
sns.scatterplot(x='PCA1', y='PCA2', hue='Cluster', data=data, palette='viridis', s=100, edgecolor='k')
plt.title('K-means Clustering of Football Players')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.legend(title='Cluster')
plt.show()
