import numpy as np
import scipy
import matplotlib.pyplot as plt
import csv
import pandas as pd

from sklearn.metrics import pairwise_distances #jaccard diss.
from sklearn import manifold  # multidimensional scaling

# import data.csv
path_to_raw_data = "C:/my_mnt_c/Code/my_github/python_bioinf_2021/rd.csv"
headers = ["<5 m", "5m-1y", "1y+", "2y+"]
data = pd.read_csv(path_to_raw_data, sep=',', names=headers)
data = data.astype(int)

data = data.to_numpy()

dis_matrix = pairwise_distances(data, metric = 'jaccard')
print(dis_matrix.shape)

mds_model = manifold.MDS(n_components=2, random_state=123,
                         dissimilarity='precomputed')
mds_fit = mds_model.fit(dis_matrix)
mds_coords = mds_model.fit_transform(dis_matrix)


plt.figure()
plt.scatter(mds_coords[:, 0], mds_coords[:, 1],
            facecolors='none', edgecolors='none')  # points in white (invisible)
labels = headers
for label, x, y in zip(labels, mds_coords[:, 0], mds_coords[:, 1]):
    plt.annotate(label, (x, y), xycoords='data')
plt.xlabel('First Dimension')
plt.ylabel('Second Dimension')
plt.title('Dissimilarity among food items')
plt.show()

"""


foods_binary = np.random.randint(2, size=(100, 10)) #initial dataset
print(foods_binary.shape)

dis_matrix = pairwise_distances(foods_binary, metric = 'jaccard')
print(dis_matrix.shape)

mds_model = manifold.MDS(n_components=2, random_state=123,
                         dissimilarity='precomputed')
mds_fit = mds_model.fit(dis_matrix)
mds_coords = mds_model.fit_transform(dis_matrix)

food_names = ['pasta', 'pizza', 'meat', 'eggs', 'cheese', 'ananas', 'pear', 'bread', 'nuts', 'milk']
plt.figure()
plt.scatter(mds_coords[:, 0], mds_coords[:, 1],
            facecolors='none', edgecolors='none')  # points in white (invisible)
labels = food_names
for label, x, y in zip(labels, mds_coords[:, 0], mds_coords[:, 1]):
    plt.annotate(label, (x, y), xycoords='data')
plt.xlabel('First Dimension')
plt.ylabel('Second Dimension')
plt.title('Dissimilarity among food items')
plt.show()
"""