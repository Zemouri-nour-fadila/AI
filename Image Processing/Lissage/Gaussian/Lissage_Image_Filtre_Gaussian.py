# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:00:51 2021

@author: zemou
"""

import numpy as np
from PIL import Image,ImageFilter 
import math

#def Amelioration_contraste(img):
    
#import the noised image 
img = Image.open("NoisedImage.bmp").convert("L")

#transform the noised image into a matrix 
I=np.array(img)

n=I.shape[0] #lines numbers
m=I.shape[1] #columns numbers


#/////////PART1 ***** REMPLISSAGE DE L'IMAGE ****** ///////

collone1=np.array([I[:,0]]).T
collone2=np.array([I[:,m-1]]).T

I= np.c_[collone1,I,collone2]#ajout des 2 collones

ligne1=np.array([I[0,:]])
ligne2=np.array([I[n-1,:]])

I= np.r_[ligne1,I,ligne2]    #ajout des 2 lignes


#transform the matrix to an image remplit
Img2=Image.fromarray(I)


#/////////***** FIN DU REMPLISSAGE DE L'IMAGE ****** ///////



#/////////PART2 ***** APPICATION DU FILTRE Gaussian ****** ///////
img = np.array(Img2)
#create gaussian filter
filter_size=3
temp = []
indexer = filter_size // 2
epsilon = 0.06
sigma = filter_size*1.0/math.sqrt(-2*math.log(epsilon))
h = np.zeros((2*filter_size+1,2*filter_size+1))
som = 0
for m in range(-filter_size,filter_size+1):
   for n in range(-filter_size,filter_size+1):
        h[m+filter_size][n+filter_size] = math.exp(-(n*n+m*m)/(2*sigma*sigma))
        som += h[m+filter_size][n+filter_size]
h = h/som
#apply gaussian filter on image
s = I.shape
py = (h.shape[0]-1)//2
px = (h.shape[1]-1)//2
#create the new matrix of the smoothed image
I2 = I.copy()

#Apply gaussian filter
for i in range(1,s[1]-px-1):
   for j in range(1,s[0]-py-1):
       somme = 0.0
       for k in range(-px,px+1):
         for l in range(-py,py+1):
            somme += I[j+l][i+k]*h[l+py][k+px]
         I2[j][i] = somme

#save the smoothed image 
Img2.save("filtre_gaussian.bmp")

#/////////***** FIN DE L'APPICATION DU FILTRE MEAN ****** ///////


#/////////PART3 ***** TRIMMING IMAGE  ****** ///////

#supprimer le ligne et colonne ajouter au debut pour appliquer le lissage
I2=np.delete(I2, 0, axis = 1)
I2=np.delete(I2, I2.shape[1]-1, axis = 1)
I2=np.delete(I2, 0, axis = 0)
I2=np.delete(I2, I2.shape[0]-1, axis = 0)


Img3=Image.fromarray(I2)
if Img3 != 'RGB':
    Img3 = Img3.convert('RGB')
    
#save the smoothed image after trimming
Img3.save("filtre_gaussian_affter_triming.bmp")

#/////////***** FIN DEU TRIMMING ****** ///////
