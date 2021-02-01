# as examle i use Fasta file of All Wnt genes
# https://era.library.ualberta.ca/items/f1610b9e-6003-42f2-a430-e8c9fddc3483
# Author(s) / Creator(s):
# Sally Leys
# Pamela Windsor-Reid

import sys
import matplotlib.pyplot as plt

# import path to file with sys.argv

len_sys_argv = len(sys.argv[1:])
path_to_file = sys.argv[1]

# path_to_file = "C:\my_mnt_c\Code\my_github\python_bioinf_2021\wnt_fasta_example.fasta"

# data collecting
x = 0
hist_list = []

with open(path_to_file, "r") as file:
    first = file.readline()
    for line in file:
        if str(">") not in line:
            x += len(line.strip())
            print(x)
        else:
            hist_list.append(x)
            x = 0
    hist_list.append(x)


print(hist_list)
print(len(hist_list))


# plot
plt.rcParams['figure.figsize'] = [18, 7]
plt.rcParams['font.size'] = 13
plt.rcParams['savefig.bbox'] = 'tight'


plt.hist(hist_list, bins=50, color="darkcyan", alpha=0.9)
plt.title('Sequence length distribution')
plt.xlabel('Number of elements in sequence (bin size = 50)')
plt.ylabel('Сount')

plt.savefig('Sequence_length_distribution_for_fasta.png')



