# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:18:56 2018

@author: alexa

Rescale Application: Adapted from Speakeasy code by Robert Lodder
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

thefile = genfromtxt("UVSpectraData.csv",delimiter=",",skip_header=1)

Wavelengths = thefile.T[0]

Spectra = thefile.T[1:]

#plot out data of original values
fig, (ax) = plt.subplots(1)

#Resize the data
Resized = resize(Spectra,1,0)

for each in thefile.T[0:]:
    ax.plot(Wavelengths,each,label="Original Spectrum")

#Plot out the resized data.
for each in Resized:
    ax.plot(Wavelengths,each,label="Resized Spectrum Maxval:0 Minval:0")

plt.xlabel("Wavelength nm")
plt.ylabel("Absorbance")
plt.axis([190, 500, -1, 1])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()