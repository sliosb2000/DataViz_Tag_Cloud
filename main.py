import csv
from distutils.command.install import key

with open('input.txt', 'r') as info_file:
    dic = dict()

    for line in info_file:
        line = line.strip()
        line = line.upper()
        word = line.split()

        for w in dic:
            dic[w] = dic[w] + 1
        else:
            dic[word] = 1

    for word in list(dic.keys()):
        print(key, " ", dic[key])