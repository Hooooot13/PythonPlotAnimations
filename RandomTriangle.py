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
plt.plot(V1[0], V1[1],'o', V2[0], V2[1], 'o',  V3[0], V3[1], 'o')
#plt.savefig('testPlot.png')
plt.holdall
plt.plot(X[0], X[1])
def PickNewPoint(i=int):
    l = r.randint(1,4)
    if l == 1:
        X[0] = (X[0]+V1[0]) / 2
        X[1] = (X[1]+V1[1]) / 2
    elif l == 2:
        X[0] = (X[0]+V2[0]) / 2
        X[1] = (X[1]+V2[1]) / 2
    elif l == 3:
        X[0] = (X[0]+V3[0]) / 2
        X[1] = (X[0]+V3[1]) / 2
    else:
        print('error')
        
