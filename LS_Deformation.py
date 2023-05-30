# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 14:07:51 2022

@author: Logan.Zentz
"""

from lasso.dyna import D3plot, ArrayType
from finder import find
import numpy as np
import os

# file_path = r"C:\Users\Logan.Zentz\Documents\Coupling\Coupling_FoamStudy\test_results\AM50_G50_ON90_P0_35mph_FC1500_SF0,500\d3plot"


def MaxDeformation(dir):

    file_path = os.path.join(dir, 'd3plot')
    d3plot = D3plot(file_path, state_array_filter=[ArrayType.node_displacement])

    E = d3plot.arrays['node_displacement']
    n = d3plot.arrays['node_ids']

    # X = []
    # index = [] MPH TO MPS: 0.44704
    # dx = 78.2227
    fts = abs(E[1, :, 0] - E[0, :, 0])  # node displacement- first time step
    fts.sort()
    dx = fts[-10]
    Def = np.zeros(np.shape(E)[1])
    D = []
    N = []


    for i in range(1, d3plot.n_timesteps - 1):
        d = abs(E[i, :, 0] - E[0, :, 0] - i * dx)  # current x pos - initial x pos - time * velocity
        Def = np.vstack([Def, d])
        D.append(max(d))

        dl = d.tolist()
        ind = dl.index(max(dl))
        MyNode = n[ind]
        N.append(MyNode)
        # print(MyNode)
    return max(D)

    # print('__________________________\n__________________________\n')
    # indexes = find(Def, max(D))
    # print(indexes)
    # print('__________________________\n__________________________\n')
    # print(max(D))
    # print(round(max(D), 1))

    # for i in stuff[0]:
    #     X.append(i[0])

    # max_X = max(X)

    # for i in range(len(X)):
    #     if X[i] == max_X:
    #         index.append(i)

    # print(index)
