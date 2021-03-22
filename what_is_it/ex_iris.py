import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris, load_boston, load_wine
from sklearn.preprocessing import MinMaxScaler

import plotly.express as px
import plotly.graph_objects as go

%matplotlib inline

iris = load_iris()