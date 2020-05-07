import re
import matplotlib.pyplot as plt
import numpy as np
f = open("d5.txt", "r")
dimm = 20
_x = []
gauss = []
listSieve = []
gdur = 0
ldur = 0
count = 0
for x in f:
    index = x.find("dimm")
    # index = x.find("dimm")
    index2 = x.find("gauss  duration")
    index3 = x.find("list  duration")
    if index != -1:
        _dimm = int(re.search("\d+", x)[0])
        if (dimm != _dimm):
            _x.append(dimm)
            gauss.append(gdur/(count))
            listSieve.append(ldur/(count))
        dimm = _dimm
        gdur = 0
        ldur = 0
        count = 0
        print(dimm)
    elif index2 != -1:
        gdur += int(re.search("\d+", x)[0])
        count+=1
    elif index3 != -1:
        ldur += int(re.search("\d+", x)[0])
_x.append(dimm)
gauss.append(gdur/count)
listSieve.append(ldur/count)
d = []
for i in range(0, len(_x)):
    d.append(listSieve[i]/gauss[i])

# for i in range(1, 5):
#     _x.pop()
#     listSieve.pop()
#     gauss.pop()
print(_x)
print(listSieve)
print(gauss)
plt.plot(_x, d, "o")
# plt.plot(_x, listSieve, 'r--', _x, gauss, 'b--')
# plt.plot(_x, gauss, 'b--')
plt.show()

f.close()
