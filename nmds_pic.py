# libraries
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import plotly.express as px

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

# ["< 5 month", "5 month - 1 year", "> 1 year", "> 2 years"


# plot

# print(data)


parallel_coordinates(data, 'Diameter_age',
                     colormap=plt.get_cmap("Set3"),
                     linewidth=1.5,
                     alpha=0.8)
plt.ylabel('Colony size and age $\\rightarrow$', fontsize=12)

plt.show()
