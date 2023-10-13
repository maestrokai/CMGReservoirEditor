from toolbox import *
from faciesCodes import *
from reservoir import *

# import SPE 11 model
fname = "test.txt"
file = readFile(fname)
# convert to codes
rescode = prop_mapper(file, seven2four)

nrow = 120
ncol = 840
res = reservoir(rescode, nrow, ncol)

# Modify the reservoir from here
res.deleteRow(101,120)
# res.deleteCol(251,840)

# cover the upper fractures
res.copyTo([[60,80],[1,120]],[[30,50],[1,120]])
res.copyTo([[67,100],[500,700]],[[67,100],[250,450]])
res.copyTo([[67,100],[500,700]],[[67,100],[250,450]])

# make first fracture
res.copyTo([[15,26],[95,110]],[[26,37],[105,120]])
res.copyTo([[15,26],[95,110]],[[37,48],[115,130]])
res.copyTo([[15,26],[95,110]],[[75,86],[145,160]])
res.copyTo([[15,30],[95,110]],[[85,100],[155,170]])

# complete the first pattern
res.copyTo([[40,60],[135,250]],[[40,60],[1,116]])
res.copyTo([[40,60],[10,20]],[[40,60],[1,11]])

# repeate the first patter
res.copyTo([[1,100],[1,250]],[[1,100],[251,500]])
res.copyTo([[1,100],[1,250]],[[1,100],[501,750]])
res.copyTo([[1,100],[1,90]],[[1,100],[751,840]])

visualizer(res.coding, res.nrow, res.ncol)

# convert from facies to por, or permI
pors = prop_mapper(res.coding, facies2por)
