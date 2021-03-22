



import sys

path_to_file = sys.argv[1]

with open(path_to_file, "r") as file:
    line = file.readline()
    for line in file:
        if line.find(">") != -1:
            print(line)
        else:
            print(line.upper())