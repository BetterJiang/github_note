
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 09:25:46 2017

@author: HaiyanJiang

introduction of the Monte Carlo and some Python code exercise

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 1000)
y = x ** 2
plt.plot(x, y)
plt.fill_between(x, y, where=(y>0), color="red", alpha=0.5)
#plt.show()


#==============================================================================
# Create an array of the given shape and 
# populate it with random samples from a uniform distribution over [0, 1).
# np.random.rand(d0, d1) ## (d0, d1) the shape
#==============================================================================
### calculate integral ## 
N = 1000
points = [[xy[0]*2, xy[1]*4] for xy in np.random.rand(N, 2)]
plt.scatter([x[0] for x in points], [x[1] for x in points], s=5, c=np.random.rand(N),alpha=0.5)
plt.show()

count = 0
for xy in points:
    if xy[1] <= xy[0] **2:
        count += 1

print(count/N * (2*4))

import scipy as scipy
print(scipy.integrate.quad(lambda x: x ** 2, 0, 2)[0])



###########################################################
### figure out why we always miss the Ring-Toss game;

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
circle_target = mpatches.Circle([0,0], radius=5, edgecolor='r', fill=False)
plt.xlim(-80, 80)
plt.ylim(-80, 80)
plt.axes().add_patch(circle_target)
#plt.show()

N = 1000
u, sigma = 0, 20
points = sigma * np.random.randn(N, 2) + u
plt.scatter([x[0] for x in points], [x[1] for x in points], c=np.random.rand(N), alpha=0.5)
plt.show()

xyin = [xy for xy in points if xy[0]**2 + xy[1]**2 < (8-5) **2]
rt = len(xyin) / N
print(rt)


###########################################################
### calculate the value pi

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
circle_target = mpatches.Circle([0,0], radius=1, edgecolor='r', fill=False)
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.axes().add_patch(circle_target)
#plt.show()

N = 10000
points = np.random.rand(N, 2)*2 - 1 # change [0,1) to [-1,1)
plt.scatter([x[0] for x in points], [x[1] for x in points], c=np.random.rand(N), alpha=0.5)
plt.show()

xyin = [xy for xy in points if xy[0]**2 + xy[1]**2 <= 1]
rt = len(xyin) / N
print(rt * 4)



###########################################################
### calculate integrate ## 


