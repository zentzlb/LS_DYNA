import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

speed = 35  # mph
c = 0.44704  # mph to mm/ms

file_path = fr'C:\Users\Logan.Zentz\Documents\Coupling\Coupling_FoamStudy\i\Boundary_{speed}mph_001.k'
new_file_path = fr'C:\Users\Logan.Zentz\Documents\Coupling\Coupling_FoamStudy\i\Boundary_{speed}mph_002.k'

with open(file_path, 'r') as file:
    text = file.read()

v = [speed * c]
t = [0]

a = -9.8 * 0.18 * 1e-3  # mm/ms/ms
dt = 1  # ms
tf = 2500  # ms

mystr = '$:             xvals               yvals\n'
ind = text.find(mystr) + len(mystr)

temp = text[:ind]

while t[-1] < tf:
    t.append(t[-1] + dt)
    v .append(v[-1] + a * dt)

for i in range(len(t)):
    temp += f'{t[i]:20.5f}{v[i] / v[0]:20.5f} \n'

temp += '*END\n'

with open(new_file_path, 'w') as new_file:
    new_file.write(temp)


print(temp)







# T = np.array(t)
# V = np.array(v)
#
# T.reshape((len(T), 1))
# V.reshape((len(V),1))
#
# plt.plot(t,v)
# plt.show()