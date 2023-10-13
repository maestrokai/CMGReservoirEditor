from toolbox import *
from faciesCodes import *
from reservoir import *

fname = "test.txt"
file = readFile(fname)
# convert to codes
rescode = prop_mapper(file, seven2four)
print(set(rescode))
nrow = 120
ncol = 840
res = reservoir(rescode, nrow, ncol)
visualizer(res.coding, res.nrow, res.ncol)