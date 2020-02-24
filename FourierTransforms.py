# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:39:27 2019

@author: ouille
"""
import numpy as np


def ift (x):
    return (np.fft.fftshift(np.fft.ifft(np.fft.ifftshift( x ))))


def ft(x):
    return (np.fft.fftshift(np.fft.fft(np.fft.ifftshift(x))))


def ftAxis(nPoints, nuMax):
    deltaT = 1/(2*nuMax)
    nu = np.arange(-nuMax,nuMax-(2*nuMax/nPoints),2*nuMax/nPoints)
    t = np.arange(-nPoints/2*deltaT,(nPoints/2-1)*deltaT,deltaT)
    return [nu, t]