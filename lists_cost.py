
import numpy as np
import matplotlib.pyplot as plt
import val_cout_object
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

def transpose_list(p, data, n):
    cost = 0
    list = [np.random.choice(data, p=p)]
    listappend = list.append

    for i in range(1,n):
        x = np.random.choice(data, p=p)
        try:
            for j in range(len(list)):
                if list[j] == x:
                    cost+=1
                    temp=list[j]
                    del list[j]
                    list.insert(j,temp)
                    raise BreakIt
                elif list[j] == list[-1]:
                    listappend(x)
                cost += 1
        except BreakIt:
            pass
        yield cost
        cost = 0


def count_list(p, data, n):
    cost = 0
    list = [val_cout_object.Val_cout(np.random.choice(data, p=p),1)]
    listappend = list.append

    for i in range(1,n):
        x = np.random.choice(data, p=p)
        try:
            for j in range(len(list)):
                if list[j].value == x:
                    cost+=1
                    list[j].count+=1
                    list.sort(key=lambda x: x.count, reverse=True)
                    print(list)
                    raise BreakIt
                elif list[j].value == list[-1].value:
                    listappend(val_cout_object.Val_cout(x,1))
                cost += 1
        except BreakIt:
            pass
        yield cost
        cost = 0

cost_list = []
cost_list_tf = []
cost_list_mf = []
cost_list_count = []
cost_list_geo = []
cost_list_tf_geo = []
cost_list_mf_geo = []
cost_list_count_geo = []
cost_list_h = []
cost_list_tf_h = []
cost_list_mf_h = []
cost_list_count_h = []

n_list = [100, 500, 1000, 5000, 10000, 50000, 100000]
mean_list = []
list=[]

    #Normal Normal list
for i in n_list:
    for value in normal_list(probability_normal,data_in,i):
        list.append(value)
    cost_list.append(np.mean(list))
    list.clear()

    #geo normal list
for i in n_list:
    for value in normal_list(probability_geo,data_in,i):
        list.append(value)
    cost_list_geo.append(np.mean(list))
    list.clear()

    #harmonic normal list
for i in n_list:
    for value in normal_list(probability_harmonic, data_in, i):
        list.append(value)
    cost_list_h.append(np.mean(list))
    list.clear()


for i in n_list:
    for value in count_list(probability_normal,data_in,i):
        list.append(value)
    cost_list_count.append(np.mean(list))
    list.clear()

    #geo normal list
for i in n_list:
    for value in count_list(probability_geo,data_in,i):
        list.append(value)
    cost_list_count_geo.append(np.mean(list))
    list.clear()

    #harmonic normal list
for i in n_list:
    for value in count_list(probability_harmonic, data_in, i):
        list.append(value)
    cost_list_count_h.append(np.mean(list))
    list.clear()



for i in n_list:
    for value in move_to_front_list(probability_normal,data_in,i):
        list.append(value)
    cost_list_mf.append(np.mean(list))
    list.clear()

    #geo normal list
for i in n_list:
    for value in move_to_front_list(probability_geo,data_in,i):
        list.append(value)
    cost_list_mf_geo.append(np.mean(list))
    list.clear()

    #harmonic normal list
for i in n_list:
    for value in move_to_front_list(probability_harmonic, data_in, i):
        list.append(value)
    cost_list_mf_h.append(np.mean(list))
    list.clear()


for i in n_list:
    for value in transpose_list(probability_normal,data_in,i):
        list.append(value)
    cost_list_tf.append(np.mean(list))
    list.clear()

    #geo normal list
for i in n_list:
    for value in transpose_list(probability_geo,data_in,i):
        list.append(value)
    cost_list_tf_geo.append(np.mean(list))
    list.clear()

    #harmonic normal list
for i in n_list:
    for value in transpose_list(probability_harmonic, data_in, i):
        list.append(value)
    cost_list_tf_h.append(np.mean(list))
    list.clear()



plt.figure(1)
plt.plot(n_list, cost_list)
plt.semilogx()
plt.xlabel('n')
plt.title("Normal List Normal Probability")
plt.grid()
plt.figure(2)
plt.plot(n_list, cost_list_geo)
plt.semilogx()
plt.xlabel('n')
plt.title("Normal List Geo Probability")
plt.grid()
plt.figure(3)
plt.plot(n_list, cost_list_h)
plt.semilogx()
plt.xlabel('n')
plt.title("Normal List Harmonic Probability")
plt.grid()
plt.figure(4)
plt.plot(n_list, cost_list_tf)
plt.semilogx()
plt.xlabel('n')
plt.title("TRANSPOSE List Normal Probability")
plt.grid()
plt.figure(5)
plt.plot(n_list, cost_list_tf_geo)
plt.semilogx()
plt.xlabel('n')
plt.title("TRANSPOSE List Geo Probability")
plt.grid()
plt.figure(6)
plt.plot(n_list, cost_list_tf_h)
plt.semilogx()
plt.xlabel('n')
plt.title("TRANSPOSE List Harmonic Probability")
plt.grid()
plt.figure(7)
plt.plot(n_list, cost_list_mf)
plt.semilogx()
plt.xlabel('n')
plt.title("MTF List Normal Probability")
plt.grid()
plt.figure(8)
plt.plot(n_list, cost_list_mf_geo)
plt.semilogx()
plt.xlabel('n')
plt.title("MTF List Geo Probability")
plt.grid()
plt.figure(9)
plt.plot(n_list, cost_list_mf_h)
plt.semilogx()
plt.xlabel('n')
plt.title("MTF List Harmonic Probability")
plt.grid()
plt.figure(10)
plt.plot(n_list, cost_list_count)
plt.semilogx()
plt.xlabel('n')
plt.title("COUNT List Normal Probability")
plt.grid()
plt.figure(11)
plt.plot(n_list, cost_list_count_geo)
plt.semilogx()
plt.xlabel('n')
plt.title("COUNT List Geo Probability")
plt.grid()
plt.figure(12)
plt.plot(n_list, cost_list_count_h)
plt.semilogx()
plt.xlabel('n')
plt.title("COUNT List Harmonic Probability")
plt.grid()
plt.show()
# list.sort()

