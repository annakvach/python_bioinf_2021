import matplotlib.pyplot as plt
import pandas as pd

# line plot for small data

# import data.csv
headers = ["Zooid bud", "f", "Degenerating zooid", "Brown body", "br", "op", "pbo", "emb", "sum"]
data = pd.read_csv('data.csv', sep=';', names=headers)
data = data.astype(int)

# sorting
data.set_index("sum", inplace=True)  # replace index col
data_sort = data.sort_values(by=["sum"], ascending=[True])
data_degener = data_sort[["Brown body", "Degenerating zooid", "Zooid bud"]]

# rcParams

plt.rcParams['figure.figsize'] = [18, 9]
plt.rcParams['font.size'] = 15
plt.rcParams['savefig.bbox'] = 'tight'

data_degener.plot(color=["darkred", "red", "cyan"])

plt.title('Number of "degenerate/ing" zooids vs colony size')
plt.xlabel('All zooids in the colony')
plt.ylabel('Number of the degenerate/ing zooids')
plt.grid()

plt.show()

