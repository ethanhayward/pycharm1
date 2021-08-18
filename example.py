import matplotlib.pyplot as plt
import math
list = [1,2,3,4,5]
empty_list = []
for k in list:
    empty_list.append(math.sin(k))
plt.plot(empty_list,list)
plt.show()