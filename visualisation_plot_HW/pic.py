import matplotlib.pyplot as plt
import pandas as pd

# line plot for small data

# import data.csv
headers = ["Zooid bud", "Feeding zoods", "Degenerating zooid", "Brown body", "br", "op", "pbo", "emb", "sum"]
data = pd.read_csv('data.csv', sep=';', names=headers)
data = data.astype(int)

# sorting
data.set_index("sum", inplace=True)  # replace index col
data_sort = data.sort_values(by=["sum"], ascending=[True])

data_degener = data_sort[["Brown body", "Degenerating zooid", "Zooid bud"]]
data_feed = data_sort["Feeding zoods"]

# Plots
plt.rcParams['figure.figsize'] = [18, 7]
plt.rcParams['font.size'] = 13
plt.rcParams['savefig.bbox'] = 'tight'

# several plots
figure, axes = plt.subplots(nrows=2, ncols=1)

# color
data_degener.plot(color=["darkred", "red", "cyan"], ax=axes[0])
data_feed.plot(color=["purple"], ax=axes[1])

# labels
plt.suptitle('Number of zooid of different types vs colony size')

axes[0].set_ylabel("'Young' and 'old' zooids")
axes[1].set_ylabel("Feeding zooids")

axes[0].set_xlabel("")
axes[1].set_xlabel("Colony size (number of zooids)")

plt.show()



