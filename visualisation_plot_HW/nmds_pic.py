# libraries
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import plotly.express as px
import squarify

path_to_data = "C:/my_mnt_c/Code/my_github/python_bioinf_2021/rd.csv"

# import data.csv
headers = ["Month", "Zooid bud",
      "Feeding zoods","Degenerating zooid",
      "Brown body", "Bb, polypide",
      "Polypide, ovary", "Bb, polypide, ovary",
      "Embryos", "All zoids", "Diameter_age"]
data = pd.read_csv(path_to_data, sep=',', names=headers)


# data cols type
data[["Month", "Zooid bud",
      "Feeding zoods", "Degenerating zooid",
      "Brown body", "Bb, polypide",
      "Polypide, ovary", "Bb, polypide, ovary",
      "Embryos", "All zoids"]] = \
    data[["Month", "Zooid bud", "Feeding zoods", "Degenerating zooid",
          "Brown body", "Bb, polypide",
          "Polypide, ovary", "Bb, polypide, ovary",
          "Embryos", "All zoids"]].astype(int)

data[["Diameter_age"]] = data[["Diameter_age"]].astype(str)

# plot to browser (not very useful plot)
cols = ["Zooid bud",
      "Feeding zoods","Degenerating zooid",
      "Brown body", "Bb, polypide",
      "Polypide, ovary", "Bb, polypide, ovary",
      "Embryos", "All zoids"]


fig = px.parallel_coordinates(data,
                              color="All zoids",
                              dimensions=cols,
                              color_continuous_scale=px.colors.diverging.Tealrose,
                              width=1000,
                              title="Colony size and zooids of different types")

fig.show()


# plot to png

## Parallel plot
plt.figure(figsize=(14, 6), dpi=100)
parallel_coordinates(data, 'Diameter_age',
                     colormap=plt.get_cmap("Set3"),
                     linewidth=1.5,
                     alpha=0.8)
plt.ylabel('Colony size and age $\\rightarrow$', fontsize=12)


plt.savefig("1.png")
plt.close()


# Treemap of colonies of different age
df = data.groupby('Diameter_age').size().reset_index(name='sum') # create dataframe with groups (age) and number of colonies (sum)

labels = df.apply(lambda x: str(x[0]) + "\n [" + str(x[1]) + "]", axis=1) # apply to each row special form

sizes = df['sum'].values # get values from col sum
colors = ['lightseagreen', 'skyblue', 'thistle', 'maroon']


plt.figure(figsize=(14, 6), dpi=100)
plt.axis('off') # delete axis
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.8)
plt.title('Treemap of colonies of different age')



plt.savefig("2.png")
plt.close()
















# ----------------------------------------------------------------------------------------------
"""
a = data[["Month", "Zooid bud", "Feeding zoods", "Degenerating zooid",
          "Brown body", "Bb, polypide",
          "Polypide, ovary", "Bb, polypide, ovary",
          "Embryos", "All zoids"]].astype(int)

b = data[["Diameter_age"]].astype(str).iloc[0]

features = ["Month", "Zooid bud", "Feeding zoods", "Degenerating zooid",
          "Brown body", "Bb, polypide",
          "Polypide, ovary", "Bb, polypide, ovary",
          "Embryos", "All zoids"]

# "< 5 month", "5 month - 1 year", "> 1 year", "2 years"
classes = ["Diameter_age"]

visualizer = parallel_coordinates(a, b, classes=classes, features=features)

"""

# ----------------------------------------------------------------------------------------------









