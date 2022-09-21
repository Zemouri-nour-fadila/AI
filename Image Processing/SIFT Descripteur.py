# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 17:45:58 2021

@author: zemou
"""

import cv2 
import matplotlib.pyplot as plt
from PIL import ImageTk, Image 
import numpy as np

def distance(kpt1, kpt2):
     #Cree numpy array avec les keypoint positions
     arr = np.array([kpt1.pt, kpt2.pt])
     #calculer la distance
     dist = np.linalg.norm(arr[0]-arr[1])
     return dist

im = Image.open("image0.bmp").convert('RGB')

#transform the noised image into a matrix 
img1=np.array(im)
Bdd = cv2.imread('C:\\Users\\zemou\\Desktop\\ProjetTin\\Casia v1 ImageTraiter\\image2.bmp') 
#Transform image a une image au niveau gris
img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
Bdd = cv2.cvtColor(Bdd, cv2.COLOR_BGR2GRAY)

#Creé SIFT
sift = cv2.SIFT_create()
#Detection des points clés dans l'image
keypoints_1, descriptors_1 = sift.detectAndCompute(img,None)
keypoints_2, descriptors_2 = sift.detectAndCompute(Bdd,None)

#correspondance des points clés
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
matches = bf.match(descriptors_1,descriptors_2)
matches = sorted(matches, key = lambda x:x.distance)
#Dessiner des trait  de correspondance entre les points clé des deux images
img3 = cv2.drawMatches(img, keypoints_1, Bdd, keypoints_2, matches[:50], Bdd, flags=2)
print(keypoints_1[0])
print(keypoints_2[0])
for i,keypoint in enumerate(keypoints_1):
    dist=distance(keypoints_1[0], keypoints_2[0])
print (dist)
    
img3=Image.fromarray(img3)
img3.save('match.bmp')

