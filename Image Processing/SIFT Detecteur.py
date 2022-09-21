# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:10:20 2021

@author: zemou
"""


import cv2 as cv
import numpy as np
from PIL import  Image

def detecteur_SIFT(img):
  #Transform image a une image au niveau gris
  gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
  #Crée un objet SIFT
  sift = cv.SIFT_create()
  #Trouver les points clé dans l'image
  kp = sift.detect(gray,None)
  #Dessiner des petit cercle sur les emplacement des points clé dans l'image
  img=cv.drawKeypoints(gray,kp,img)
  return img

im = Image.open("image0.bmp").convert('RGB')
#transform the noised image into a matrix 
img1=np.array(im)
img4=detecteur_SIFT(img1)
img5=Image.fromarray(img4)
img5.save('sift detect.bmp')