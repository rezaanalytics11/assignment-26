import cv2


image = cv2.imread(r"C:\Users\Ariya Rayaneh\Desktop\obama.jpg")


alpha = 1.5
beta = 100

adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

cv2.imshow('adjusted', adjusted)
cv2.imwrite(r"C:\Users\Ariya Rayaneh\Desktop\picture_contrast_2.jpg",adjusted)
cv2.waitKey()
