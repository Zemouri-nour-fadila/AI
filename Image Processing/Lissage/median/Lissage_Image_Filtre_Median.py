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
img = Image.open("001_1_1.bmp").convert("L")

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



#/////////PART2 ***** APPICATION DU FILTRE MEDIAN ****** ///////
img = np.array(Img2)
filter_size=3
temp = []
indexer = filter_size // 2

n=I.shape[0] #lines numbers
m=I.shape[1] #columns numbers

#create the new matrix of the smoothed image
I2=np.ones([n,m])

for i in range(1,len(img)-1):
  for j in range(1,len(img[0])-1):
     for z in range(filter_size):
        for k in range(filter_size):
          temp.append(img[i + z - indexer][j + k - indexer])

     temp.sort()
     I2[i][j] = temp[len(temp) // 2]
     temp = []     

#transform the matrix to an image smoothed
Img2=Image.fromarray(I2)
if Img2 != 'RGB':
    Img2 = Img2.convert('RGB')
    
#save the smoothed image 
Img2.save("filtre_median.bmp")

#/////////***** FIN DE L'APPICATION DU FILTRE MEDIAN ****** ///////


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
Img3.save("filtre_moyenne_affter_triming.bmp")

#/////////***** FIN DEU TRIMMING ****** ///////
