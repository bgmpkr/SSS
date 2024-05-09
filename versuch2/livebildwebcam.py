# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os


from skimage.color import rgb2gray
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    grayscale = rgb2gray(frame)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.imshow(grayscale, cmap=plt.cm.gray)
    ax.set_title("Grayscale")
    plt.show()
cap.release()
cv2.destroyAllWindows()

cv2.imwrite('picture2_aufgabe1.png')



cap = cv2.VideoCapture(0)   
print("frame width: " + str(cap.get(3)))
print("frame height: " + str(cap.get(4)))
print("--------------------------------")
print("brightness: " + str(cap.get(10)))
print("contrast: " + str(cap.get(11)))
print("saturation: " + str(cap.get(12)))
print("--------------------------------")
print("gain: " + str(cap.get(14)))
print("exposure: " + str(cap.get(15)))
print("--------------------------------")
print("white balance: " + str(cap.get(17)))
cap.release()
