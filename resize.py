# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:18:56 2018

@author: alexa

Rescale Application: Adapted from Speakeasy code by Robert Lodder

File includes the resize function
Input: List of 1D Spectra: eg. [[1,2,3,4,5],[4,5,6,7,8]]
Output: Scaled 1D Spectra

Example:

In[2]: resize([[0,1,2,3,4]],1,0)
Out[2]: [[0.0, 0.25, 0.5, 0.75, 1.0]]


"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import genfromtxt
from copy import *



def resize(spectra,maxval,minval):
    #Take each spectrum given
    copyofspectra = deepcopy(spectra)
    for i in range(len(copyofspectra)):
        S = copyofspectra[i]
        #Set zero value for spectrum
        for x in range(len(S)):
            S[x] = S[x] - min(S)
        #Determine range of values within the spectrum
        R1 = max(S) - min(S)

        #Determine range of max and min values
        R2 = maxval - minval


        #Resize ratio calculation.
        M = R2/R1
        for y in range(len(S)):

            #Multiply by ratio of range of spectrum over range of max and min value.
            S[y] = S[y] * M
            S[y] = S[y] + minval
    return copyofspectra
