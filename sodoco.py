import cv2
import numpy as np

img = cv2.imread('sodoco.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img=img[30:195,30:195]
img2 = img

height, width= img.shape

W_SIZE = 9
H_SIZE = 9

for ih in range(H_SIZE):
    for iw in range(W_SIZE):
        x = width / W_SIZE * iw
        y = height / H_SIZE * ih
        h = (height / H_SIZE)
        w = (width / W_SIZE)
        print(x, y, h, w)
        img1 = img[int(y):int(y + h), int(x):int(x + w)]
        for i in range(img1.shape[0]):
            for j in range(img1.shape[1]):
                print(img1[i][j])
                if img1[i][j]>0:
                    cv2.imshow('output',img1)
                    cv2.imwrite("Output Images\Output Images/" + str(ih)+str(iw)+".png", img1)
                    cv2.waitKey()
                    img = img2