import numpy as np
import cv2

img = cv2.imread(r"C:\Users\Ariya Rayaneh\Desktop\obama.jpg")

mask=np.zeros(img.shape,img.dtype)
contrast=3
bright=2

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
       for k in range(img.shape[2]):
        mask[i,j,k]=np.clip(contrast*img[i,j,k]+bright,0,255)

cv2.imwrite(r"C:\Users\Ariya Rayaneh\Desktop\picture_contrast1.jpg", mask)
cv2.imshow("output", mask)
cv2.waitKey()

