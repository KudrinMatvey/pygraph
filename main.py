import re
import matplotlib.pyplot as plt

f = open("d6.txt", "r")
dimm = 20
_x = []
gauss = []
gauss40 = []
gauss60 = []
listSieve = []
listSieve40 = []
listSieve60 = []
gdur = 0
ldur = 0
count = 0
for x in f:
    index = x.find("diff: 20")
    index2 = x.find("gauss  duration")
    index3 = x.find("list  duration")
    if index != -1:
        _dimm = int(re.search("\d+", x)[0])
        if (dimm != _dimm):
            _x.append(dimm)
            gauss.append(gdur / (count))
            listSieve.append(ldur / (count))
        dimm = _dimm
        gdur = 0
        ldur = 0
        count = 0
        print(dimm)
    elif index2 != -1:
        gdur += int(re.search("\d+", x)[0])
        count += 1
    elif index3 != -1:
        ldur += int(re.search("\d+", x)[0])
_x.append(dimm)
gauss.append(gdur / count)
listSieve.append(ldur / count)
d = []
dimm = 20
f.close()
f = open("d5.txt", "r")

for i in range(0, len(_x)):
    d.append(listSieve[i] / gauss[i])
for x in f:
    index = x.find("diff: 40")
    index2 = x.find("gauss  duration")
    index3 = x.find("list  duration")
    if index != -1:
        _dimm = int(re.search("\d+", x)[0])
        if (dimm != _dimm):
            gauss40.append(gdur / (count))
            listSieve40.append(ldur / (count))
        dimm = _dimm
        gdur = 0
        ldur = 0
        count = 0
        print(dimm)
    elif index2 != -1:
        gdur += int(re.search("\d+", x)[0])
        count += 1
    elif index3 != -1:
        ldur += int(re.search("\d+", x)[0])
gauss40.append(gdur / count)
listSieve40.append(ldur / count)
d40 = []
dimm = 20


f.close()
f = open("d5.txt", "r")

for x in f:
    index = x.find("diff: 60")
    index2 = x.find("gauss  duration")
    index3 = x.find("list  duration")
    if index != -1:
        _dimm = int(re.search("\d+", x)[0])
        if (dimm != _dimm):
            gauss60.append(gdur / (count))
            listSieve60.append(ldur / (count))
        dimm = _dimm
        gdur = 0
        ldur = 0
        count = 0
        print(dimm)
    elif index2 != -1:
        gdur += int(re.search("\d+", x)[0])
        count += 1
    elif index3 != -1:
        ldur += int(re.search("\d+", x)[0])
gauss60.append(gdur / count)
listSieve60.append(ldur / count)
d60 = []
for i in range(0, len(_x) -1):
    d60.append(listSieve60[i] / gauss60[i])
    d40.append(listSieve40[i] / gauss40[i])


print(_x)
print(listSieve)
print(gauss)

_x.pop()
_x.pop()
listSieve.pop()
listSieve.pop()
gauss.pop()
gauss.pop()
d.pop()
d.pop()
listSieve40.pop()
listSieve60.pop()
gauss40.pop()
gauss60.pop()
d40.pop()
d60.pop()


fig, axes = plt.subplots(nrows=3, ncols=1)
fig.tight_layout()
a = []
a1 = []
b = []
b1 = []
for i in range(0, len(_x) ):
    a.append(listSieve60[i]/listSieve[i])
    a1.append(listSieve40[i]/listSieve[i])
    b.append(gauss60[i]/gauss[i])
    b1.append(gauss40[i]/gauss[i])
fig, ax = plt.subplots()
plt.xlabel('размерность', fontsize=10)
plt.ylabel('отношение среднего времени выполнения, раз', fontsize=10)
ax.plot(_x,a, label="list 3/1")
ax.plot(_x,a1, label="list 2/1")
ax.plot(_x,b, label="gauss 3/1")
ax.plot(_x,b1, label="gauss 2/1")
legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')


# plt.subplot(3,1,1)
# plt.yscale('log')
# plt.title(r"$\forall b \in B : b = [0,400] $", fontsize=10)
# plt.plot(_x, listSieve, 'r--', _x, gauss, 'b--')
# plt.xlabel('размерность', fontsize=10)
# plt.ylabel('время, миллисекунды', fontsize=10)
#
# plt.subplot(3, 1, 2)
# plt.yscale('log')
# plt.title(r"$\forall b \in B : b = [0,800] $", fontsize=10)
# plt.plot(_x, listSieve40, 'r-.', _x, gauss40, 'b-.')
# plt.xlabel('размерность', fontsize=10)
# plt.ylabel('время, миллисекунды', fontsize=10)
#
# plt.subplot(3, 1, 3)
# plt.yscale('log')
# plt.title(r"$\forall b \in B : b = [0,1200] $", fontsize=10)
# plt.plot(_x, listSieve60, _x, gauss60,)
# plt.xlabel('размерность', fontsize=10)
# plt.ylabel('время, миллисекунды', fontsize=10)
#

# plt.subplot(6, 1, 4)
# plt.plot(_x, d)
# plt.subplot(6, 1, 5)
# plt.plot(_x, d40)
# plt.subplot(6, 1, 6)
# plt.plot(_x, d60)

# plt.plot(_x, gauss, 'b--')
plt.show()

f.close()
