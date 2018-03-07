import cython
import cython
import random
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing
import timeit
class BreakIt(Exception): pass
data_in = []
probability_normal = []
probability_harmonic = []
probability_geo = []
for i in range(101):
    if i > 0:
        if i < 100:
            probability_geo.append((1 / (2 ** i)))
        else:
            probability_geo.append((1 / (2 ** 99)))
for i in range(101):
    if (i > 0):
        probability_harmonic.append((1 / (i * 5.187377517639621)))
for i in range(101):
    if (i > 0):
        data_in.append(i)
        probability_normal.append(0.01)


def normal_list(p, data, n):
    cost = 0
    cost_list = []
    list = [np.random.choice(data, p=p)]
    listappend = list.append


    for i in range(1,n):
        x = np.random.choice(data, p=p)
        try:
            for j in list:
                if j == x:
                    cost+=1
                    raise BreakIt
                elif j == list[-1]:
                    listappend(x)
                cost += 1
        except BreakIt:
            pass
        yield cost
        cost = 0

def move_to_front_list(p, data, n):
    cost = 0
    list = [np.random.choice(data, p=p)]
    listappend = list.append

    for i in range(1,n):
        x = np.random.choice(data, p=p)
        try:
            for j in list:
                if j == x:
                    cost+=1
                    list.remove(j)
                    list.insert(0,j)
                    raise BreakIt
                elif j == list[-1]:
                    listappend(x)
                cost += 1
        except BreakIt:
            pass
        yield cost
        cost = 0


cost_list = 0
cost_list_tf = 0
cost_list_mf = 0
cost_list_count = 0
list_to_front = []
list_mv_forward = []
list_count = []
n_list = [100, 500, 1000, 5000, 10000, 50000, 100000]
mean_list = []
list=[]
for i in n_list:
    for value in normal_list(probability_normal,data_in,i):
        list.append(value)
    mean_list.append(np.mean(list))
    list.clear()

print(mean_list)
plt.plot(n_list, mean_list)
plt.show()
# list.sort()

