import itertools as it

l = int(input())

def generate(l):
    x = []
    y = []
    for i in range(1, l + 1):
        x = it.chain(x, it.combinations_with_replacement('ATGC', i))
        for j in x:
            y.append(''.join(j))
    return y

print(list(generate(l)))