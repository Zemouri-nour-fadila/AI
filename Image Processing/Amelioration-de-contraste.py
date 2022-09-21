# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:08:02 2021

@author: Amina
"""


import numpy as np
from PIL import Image

def Amelioration_contraste(img):
    y=np.array(img)

    Lmax=np.max(y)
    Lmin=np.min(y)
    #des paramètres a choisir
    Kmin=0
    Kmax=255

    for i in range(0,img.size[1]):       
       for j in range(0,img.size[0]):   
           y[i,j]=Kmin+ (((Kmax-Kmin)/(Lmax-Lmin))*(y[i,j]-Lmin))
        
    Img=Image.fromarray(y)
    Img.save("ImageContrast.jpg")
    Img.show()
    



img=Image.open("001_1_1.bmp")
Amelioration_contraste(img)