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
plt.plot(V1, V2, V3)
plt.savefig('testPlot.png')

#def PickNewPoint(i=int):
#    r.randint(1,4)
    
