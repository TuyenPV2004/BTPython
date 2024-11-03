import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'results.csv')

# Vẽ hàm histogram
for x in df.columns[4:]:
    plt.figure()
    plt.hist(df[x].dropna())
    plt.xlabel(x)
    plt.ylabel("Frequency")
    plt.title(f" Sự phân bố của chỉ số {x} ở cầu thủ ")
    plt.show()
