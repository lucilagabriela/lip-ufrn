# cmd: pip install matplotlib

import matplotlib.pyplot as plt
import numpy as np

#plt.plot([1, 2, 3, 4], [10, 15, 25, 50])

dic = {
    'a': 10,
    'b': 15,
    'c': 25,
    'd': 50,
}

plt.figure(' ')
plt.bar(dic.keys(), dic.values())
plt.xlabel('x numbers')
plt.ylabel('y numbers')
plt.draw()
plt.show()