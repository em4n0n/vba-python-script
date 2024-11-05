import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel("mydata.xlsx")

data.Prices.hist()
plt.show()

grouped_data = data.groupby(by="Categories").mean()
plt.bar(grouped_data.index, grouped_data.Price)
plt.show()