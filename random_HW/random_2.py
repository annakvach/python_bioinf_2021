import numpy as np
import time
import matplotlib.pyplot as plt


# function to test is the list sort or not

def SORT_OR_NOT(my_random_list):
    l = my_random_list[0]
    for r in my_random_list:
        if l > r:
            return False  # not sorted
        l = r
    return True  # sorted

# generate experiment design list
samples = 10
repetitions = 15
arith = []  # experiment design list

for j in range(1, samples + 1):
    for _ in range(1, repetitions + 1):
        arith.append(j)


# experiment
cycle_timer = 0
time_list = []

for i in arith:
    my_random_list = np.random.randint(1, i + 1, i)
    print(my_random_list)
    otvet = SORT_OR_NOT(my_random_list)
    cycle_timer += 1

    print("=============================================== CYCLE:", cycle_timer, "  REP:", i)

    start_monkey = time.time_ns()
    while otvet == False:
        s = np.random.permutation(my_random_list)
        otvet = SORT_OR_NOT(s)

    end_monkey = time.time_ns()

    time_list.append((end_monkey - start_monkey) / 10 ** 9)
    print("TIME (sec): ", (end_monkey - start_monkey) / 10 ** 9)

# statistics calculate
temp_list = []
mean_list = []
std_list = []
temp = 0

for j in [i for i in range(0, samples * repetitions, repetitions)]:
    temp_list = [time_list[j], time_list[j + 1], time_list[j + 2]]
    mean_list.append(np.mean(temp_list))
    std_list.append(np.std(temp_list))
    temp_list = []

numbers = [i for i in range(1, samples + 1)]

# PLOT

plt.rcParams['figure.figsize'] = [12, 8]
plt.rcParams['font.size'] = 20
plt.rcParams['savefig.bbox'] = 'tight'

x_pos = np.arange(len(numbers))

fig, ax = plt.subplots()
ax.bar(x_pos, mean_list, yerr=std_list, color='darkred', align='center', alpha=0.7, ecolor='black', capsize=10)
ax.set_ylabel('Time (sec)')
ax.set_xlabel('Number of items in the random list (n)')

ax.set_xticks(x_pos)
ax.set_xticklabels(numbers)
ax.set_title('Sorting time of the random list vs their number of items')
ax.yaxis.grid(True)

plt.savefig('Random_task_2_pic.png')