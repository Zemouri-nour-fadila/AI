# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 13:37:45 2021

@author: zemou
"""
from PIL import Image
import numpy as np


def converged(centroids, old_centroids):
	if len(old_centroids) == 0:
		return False

	if len(centroids) <= 5:
		a = 1
	elif len(centroids) <= 10:
		a = 2
	else:
		a = 4

	for i in range(0, len(centroids)):
		cent = centroids[i]
		old_cent = old_centroids[i]

		if ((int(old_cent[0]) - a) <= cent[0] <= (int(old_cent[0]) + a)) and ((int(old_cent[1]) - a) <= cent[1] <= (int(old_cent[1]) + a)) and ((int(old_cent[2]) - a) <= cent[2] <= (int(old_cent[2]) + a)):
			continue
		else:
			return False

	return True


def getMin(pixel, centroids):
	minDist = 9999
	minIndex = 0

	for i in range(0, len(centroids)):
       
		d = np.sqrt(int((centroids[i][0] - pixel[0]))**2 + int((centroids[i][1] - pixel[1]))**2 + int((centroids[i][2] - pixel[2]))**2)
		if d < minDist:
			minDist = d
			minIndex = i

	return minIndex


def assignPixels(centroids,img_width, img_height,px):
	clusters = {}

	for x in range(0, img_width):
		for y in range(0, img_height):
			p = px[x, y]
			minIndex = getMin(px[x, y], centroids)

			try:
				clusters[minIndex].append(p)
			except KeyError:
				clusters[minIndex] = [p]

	return clusters


def adjustCentroids(centroids, clusters):
	new_centroids = []
	keys = sorted(clusters.keys())
	#print(keys)

	for k in keys:
		n = np.mean(clusters[k], axis=0)
		new = (int(n[0]), int(n[1]), int(n[2]))
		new_centroids.append(new)

	return new_centroids




def startKmeans(someK,img_width,img_height,px):
	centroids = []
	old_centroids = []
	i = 1
	for k in range(0, someK):
		cent = px[np.random.randint(0, img_width), np.random.randint(0, img_height)]
		centroids.append(cent)
	while not converged(centroids, old_centroids) and i <= 20:
		i += 1
		old_centroids = centroids 								
		clusters = assignPixels(centroids,img_width,img_height,px) 						
		centroids = adjustCentroids(old_centroids, clusters) 	
	return centroids

def Segmentation_avec_clusstering(img):
    k = 3
    img = img.convert('RGB')
    img_width, img_height = img.size
    px = img.load()
    result = startKmeans(k,img_width, img_height,px)
    img = Image.new('RGB', (img_width, img_height), "white")
    p = img.load()
    for x in range(img.size[0]):
	    for y in range(img.size[1]):
		    RGB_value = result[getMin(px[x, y], result)]
		    p[x, y] = RGB_value
    return img


        