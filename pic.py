import matplotlib.pyplot as plt
import pandas as pd

# line plot for small data

# import data.csv
headers = ["bud", "f", "Degenerating", "Brown body", "br", "op", "pbo", "emb", "sum"]
data = pd.read_csv('data.csv', sep=';', names=headers)
data = data.astype(int)

# sorting
data.set_index("sum", inplace=True)  # replace index col
data_sort = data.sort_values(by=["sum"], ascending=[True])


data_degener = data_sort[["Brown body", "Degenerating"]]

data_degener.plot()

plt.title('Number of "degenerate/ing" modules vs colony size')
plt.xlabel('Colony size')
plt.ylabel('Degenerate/ing zooids')
plt.grid()

plt.show()


