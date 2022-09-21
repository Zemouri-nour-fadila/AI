# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:01:02 2021

@author: zemou
"""
import numpy as np
from PIL import Image 


def Remplissage(I):
  n=I.shape[0] #lines numbers
  m=I.shape[1] #columns numbers

  collone1=np.array([I[:,0]]).T
  collone2=np.array([I[:,m-1]]).T


  I= np.c_[collone1,I,collone2]#ajout des 2 collones

  ligne1=np.array([I[0,:]])
  ligne2=np.array([I[n-1,:]])

  I= np.r_[ligne1,I,ligne2]    #ajout des 2 lignes

  
  return I

def Trim(I):
  I=np.delete(I, 0, axis = 1)
  I=np.delete(I, I.shape[1]-1, axis = 1)
  I=np.delete(I, 0, axis = 0)
  I=np.delete(I, I.shape[0]-1, axis = 0)
  return I

def Dilatation(I,F):
  n=I.shape[0] #lines numbers
  m=I.shape[1] #columns numbers
  cst=1
  #create the new matrix of the smoothed image
  I_dilate=np.ones([n,m]) 
  for i in range(1, n-1):
   for j in range(1,m-1):
     temp= I[i-1:i+1+1, j-1:j+1+1]
     product= temp*F
     I_dilate[i][j]= np.max(product)
  return I_dilate

def Erosion(I,F):
  n=I.shape[0] #lines numbers
  m=I.shape[1] #columns numbers
  cst= (F.shape[0]-1)//2
  #create the new matrix of the smoothed image
  I_erode=np.ones([n,m])
  #Erosion without using inbuilt cv2 function for morphology
  for i in range(cst, n-cst):
    for j in range(cst,m-cst):
      temp= I[i-cst:i+cst+1, j-cst:j+cst+1]
      product= temp*F
      I_erode[i,j]= np.min(product)
      
  return I_erode



def Conversion(I):
    
  I_convert=I
  for i in range (0,I.shape[0],1) :
    for j in range (0,I.shape[1],1) :
      
      if I[i][j] >= 129 :
         I_convert[i][j] = 255
      else :
         I_convert[i][j] = 0
  return I_convert   
   
         
def Ouverture(I,F):
  
  I_Ouverture=Erosion(Dilatation(I,F),F)
  return I_Ouverture


def Fermeture(I,F):
  
  I_Fermeture=Dilatation(Erosion(I,F),F)
     
  return I_Fermeture



#import the noised image 
img = Image.open("001_1_1.bmp").convert("L")

#transform the noised image into a matrix 
I=np.array(img)


#/////////PART1 *****REMPLISSAGE DE L'IMAGE EN NOIR ET BLANC ****** ///////


I=Remplissage(I)

#/////////***** FIN DU REMPLISSAGE DE L'IMAGE ****** ///////


#/////////PART2 *****TRANSFORMATION DE L'IMAGE EN NOIR ET BLANC ****** ///////

I_convert=Conversion(I)  


#/////////***** FIN DE LA TRANSFORMATION DE L'IMAGE EN NOIR ET BLANC ****** ///////
#/////////PART3 ***** APPICATION DU FILTRE NON LINEAIRE ****** ///////

#Creation du filtre
F=np.ones([3,3])*255
#pplication du filtre pour lissage
I_erosion=Erosion(I_convert,F)
I_dilatation=Dilatation(I_convert,F)
I_ouverture=Ouverture(I_convert,F)
I_fetmeture=Fermeture(I_convert,F)




#/////////***** FIN DE APPICATION DES OPERATION SUR L'IMAGE EN NOIR ET BLANC ****** ///////

#/////////PART3 ***** TRIMMING IMAGE  ****** ///////

#supprimer le ligne et colonne ajouter au debut pour appliquer le lissage

I_trim=Trim(I_erosion)
I_trim1=Trim(I_dilatation)
I_trim2=Trim(I_ouverture)
I_trim3=Trim(I_fetmeture)


Img_erosion=Image.fromarray(I_trim)    
Img_dialatation=Image.fromarray(I_trim1)
Img_ouverture=Image.fromarray(I_trim2)    
Img_fermeture=Image.fromarray(I_trim3)

if Img_erosion != 'RGB':
    Img_erosion = Img_erosion.convert('RGB')
    
#save the smoothed image after trimming
Img_erosion.save("EROSION.bmp")


if Img_dialatation != 'RGB':
    Img_dialatation = Img_dialatation.convert('RGB')
    
#save the smoothed image after trimming
Img_dialatation.save("DILATATION.bmp")


if Img_ouverture != 'RGB':
    Img_ouverture = Img_ouverture.convert('RGB')
    
#save the smoothed image after trimming
Img_ouverture.save("OUVERTURE.bmp")

if Img_fermeture != 'RGB':
    Img_fermeture = Img_fermeture.convert('RGB')
    
#save the smoothed image after trimming
Img_fermeture.save("FERMETURE.bmp")

Img_f=Image.fromarray(F)
if Img_f != 'RGB':
    Img_f = Img_f.convert('RGB')
    
Img_f.save("F.bmp")


#/////////***** FIN DEU TRIMMING ****** ///////

