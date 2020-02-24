# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:05:25 2019

@author: ouille
"""

import numpy as np


def FWHM (x, y):
    ymax = np.max(y)
    #print('\n', ymax*0.5 , 'max*0.5')
    for i, value in enumerate (y):
        if value == ymax:
            index_max = i
   #         print(index_max)
    for i, value in enumerate ( y[0:index_max] ):
        if value >= 0.5*y[index_max]:
            low = i
            break
    #print(y[low] , 'y[low]')
    for i, value in enumerate (y):
        if i > index_max:
            if value <= 0.5*y[index_max]:
                high = i
                break    
   # print(y[high] , 'y[high]', '\n')
    return (x[high] - x[low])