# Logo Extractor Code (version 1):
# 	This is a simple python code for non-commercial purpose:
# 	This code extracts the logo from image (probably white or black background) by manually setting .
# 	The input image credit: https://digitalfellows.commons.gc.cuny.edu/2016/02/16/upcoming-workshop-223-collaboration-and-writing-workflows-with-git-and-github/
# 	Code statements are referred many online resources. Credit to all especially http://pythonprogramming.net  

import numpy as np
import cv2

img1 = cv2.imread('input.png',cv2.IMREAD_COLOR)


rows,cols,channels = img1.shape
roi = img1[0:rows,0:cols]
img2 = np.zeros([rows,cols,3],dtype=np.uint8)
img2.fill(255) # or img[:] = 255

t=219 # For sample image: manually set


img1gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img1gray,t,255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

# if background is white:
img_bg = cv2.bitwise_and(img2,img2, mask=mask_inv)
# if background is color, use following:
# img_bg = cv2.bitwise_and(img2,img2, mask=mask)

# if background is white:
img_fg = cv2.bitwise_and(roi,roi, mask=mask)
# if background is color, use following:
# img_fg = cv2.bitwise_and(roi,roi, mask=mask_inv)

final_img = cv2.add(img_bg, img_fg)

cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('img_bg',img_bg)
cv2.imshow('img_fg',img_fg)
cv2.imshow('final_img',final_img)

cv2.imwrite('output.png',final_img)

# Code to exit by pressing any key on output image:
cv2.waitKey(0)
cv2.destroyAllWindows()