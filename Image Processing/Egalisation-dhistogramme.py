# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:08:02 2021

@author: Amina
"""

import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt

def Egaliastion_histogramme(img):

     y=np.array(img)

     # Calcule l'histogramme de l'image
     histo = np.zeros(256, int)      # prépare un vecteur de 256 zéros
     for i in range(0,img.size[1]):       # énumère les lignes
         for j in range(0,img.size[0]):   # énumère les colonnes
             histo[y[i,j]] = histo[y[i,j]] + 1

     plt.plot(histo,label="histogramme")
     plt.legend()
     plt.show()

     # Calcule l'histogramme cumulé hc
     hc = np.zeros(256, int)         
     hc[0] = histo[0]
     for i in range(1,256):
         hc[i] = histo[i] + hc[i-1]

     plt.plot(hc,label="histogramme cumulé")
     plt.legend()
     plt.show() 

     # Normalise l'histogramme cumulé
     nbpixels = y.size
     hc =hc / nbpixels * 255


     plt.plot(hc,label="histogramme cumulé apres normalisation")
     plt.legend()
     plt.show() 


     for i in range(0,y.shape[0]):       
        for j in range(0,y.shape[1]):   
            y[i,j] =hc[y[i,j]]


     # Calcule l'histogramme de l'image apres egalisation 
     histo2 = np.zeros(256, int)      
     for i in range(0,img.size[1]):       
         for j in range(0,img.size[0]): 
             histo2[y[i,j]] = histo2[y[i,j]] + 1

     plt.plot(histo2,label="histogramme apres egalisation")
     plt.legend()     
     plt.show()  

     Img=Image.fromarray(y)
     Img.save("ImgApresEgalisation.jpg")
     
 
img=Image.open("001_1_1.bmp")
Egaliastion_histogramme(img)
