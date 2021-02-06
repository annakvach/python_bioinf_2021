import numpy as np
import random
import time
from itertools import accumulate
from operator import mul
import matplotlib.pyplot as plt
import seaborn as sns


# for time
size = 5
progression = list(accumulate([10] * size, mul))
list_random = []
list_np = []

print("------------------------ START random ------------------------ ")
for i in progression:
    print("SIZE: : ", i)
    start_random = time.time_ns()
    for j in range(i):
        random.uniform(0, 1)
    end_random = time.time_ns()

    print("-------------- TIME (sec): ", (end_random - start_random) / 10 ** 9)
    list_random.append((end_random - start_random) / 10 ** 9)

print()

print("------------------------ START np ------------------------ ")

for i in progression:
    print("SIZE: : ", i)
    start_np = time.time_ns()
    np.random.uniform(0, 1, i)
    end_np = time.time_ns()

    print("-------------- TIME (sec): ", (end_np - start_np) / 10 ** 9)
    list_np.append((end_np - start_np) / 10 ** 9)

print()
print("Random: ", list_random)
print("Numpy:  ", list_np)

# for plot
y_ord = range(1, size + 1)


plt.rcParams['figure.figsize'] = [12, 8]
plt.rcParams['font.size'] = 20
plt.rcParams['savefig.bbox'] = 'tight'

plt.plot(y_ord, list_random,  color="cyan", label="Random")
plt.plot(y_ord, list_np, color="darkred", label="Numpy")

plt.title('The relationship between the calculation time of random numbers and their number')
plt.xlabel('Number of random numbers')
plt.ylabel('Time (sec)')
plt.legend()
plt.grid(True)

plt.show()
