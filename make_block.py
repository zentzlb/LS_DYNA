from functions import *
import numpy as np

w = 1200
h = 1850
d = 400
size = 50

node_list = []
nid = int(1)
nw = w // size + 1
nh = h // size + 1
nd = d // size + 1

print('making node list...')
for x in np.linspace(0, w, nw):
    for y in np.linspace(0, h, nh):
        for z in np.linspace(0, d, nd):
            node_list.append([nid, x, y, z, 0, 0])
            nid += 1

node_array = np.array(node_list)
print('making nodes...')
node_text, nodes, xnodes, ynodes, znodes = make_nodes(node_list)
print('making solids...')
solid_text, solid_dict = make_solid(xnodes, ynodes, znodes)

final_text = node_text + solid_text + '*END\n'

with open('block.k', 'w') as my_text:
    my_text.write(final_text)  # save key file

# for x in np.linspace(0, w, nw):
#     for y in np.linspace(0, h, nh):
#         for z in np.linspace(0, d, nd):
#             node_list.append([nid, x, y, z, 0, 0])
#             nid += 1


