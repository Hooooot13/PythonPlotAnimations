import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random as r

V1 = [0,0]
V2 = [5,10]
V3 = [10, 0]
X1 = r.randint(0,11)
X2 = r.randint(0,11)
X = [X1, X2]

fig = plt.figure()
plt.plot(V1[0], V1[1], V2[0], V2[1], V3[0], V3[1])
plt.savefig('testPlot.png')

#def PickNewPoint(i=int):
#    r.randint(1,4)
    
