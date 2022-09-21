# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:00:51 2021

@author: zemou
"""

import numpy as np
from PIL import Image 





def Dilatation(I,F):
  cst=1
  #create the new matrix of the smoothed image
  I7=np.ones([n,m]) 
  for i in range(cst, n-cst):
   for j in range(cst,m-cst):
     temp= I[i-cst:i+cst+1, j-cst:j+cst+1]
     product= temp*F
     I7[i][j]= np.max(product)
  return I7

def Erosion(I,F):
  cst= (F.shape[0]-1)//2
  #create the new matrix of the smoothed image
  I8=np.ones([n,m])
  #Erosion without using inbuilt cv2 function for morphology
  for i in range(cst, n-cst):
    for j in range(cst,m-cst):
      temp= I[i-cst:i+cst+1, j-cst:j+cst+1]
      product= temp*F
      I8[i,j]= np.min(product)
      
  return I8
def Conversion(I):
  I_convert=I
  for i in range (0,I.shape[0],1) :
    for j in range (0,I.shape[1],1) :
      
      if I[i][j] >= 129 :
         I_convert[i][j] = 255
      else :
         I_convert[i][j] = 0
  return I_convert

    
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


#/////////PART2 *****TRANSFORMATION DE L'IMAGE EN NOIR ET BLANC ****** ///////

I6=Conversion(I)  
Img_n_b=Image.fromarray(I6)
if Img_n_b != 'RGB':
    Img_n_b = Img_n_b.convert('RGB')
    
#save the smoothed image 
Img_n_b.save("image_noir_blanc.bmp")

#/////////***** FIN DE LA TRANSFORMATION DE L'IMAGE EN NOIR ET BLANC ****** ///////
#/////////PART3 ***** APPICATION DU FILTRE NON LINEAIRE ****** ///////

#Creation du filtre
F=np.ones([3,3])*255
#pplication du filtre pour lissage
I7=Erosion(Dilatation(Dilatation(Erosion(I6,F),F),F),F)      

    

Img2=Image.fromarray(I7)
if Img2 != 'RGB':
    Img2 = Img2.convert('RGB')
    
#save the smoothed image 
Img2.save("filtre_non_linear.bmp")


#/////////***** FIN DE APPICATION DU FILTRE SUR L'IMAGE EN NOIR ET BLANC ****** ///////

#/////////PART3 ***** TRIMMING IMAGE  ****** ///////

#supprimer le ligne et colonne ajouter au debut pour appliquer le lissage
I7=np.delete(I7, 0, axis = 1)
I7=np.delete(I7, I7.shape[1]-1, axis = 1)
I7=np.delete(I7, 0, axis = 0)
I7=np.delete(I7, I7.shape[0]-1, axis = 0)


Img3=Image.fromarray(I7)
if Img3 != 'RGB':
    Img3 = Img3.convert('RGB')
    
#save the smoothed image after trimming
Img3.save("filtre_non_linear_affter_triming.bmp")

#/////////***** FIN DEU TRIMMING ****** ///////

