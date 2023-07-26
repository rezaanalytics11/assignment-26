import cv2

image = cv2.imread(r"C:\Users\Ariya Rayaneh\Desktop\obama.jpg")
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

equal=cv2.equalizeHist(img)


cv2.imwrite(r"C:\Users\Ariya Rayaneh\Desktop\picture_contrast3.jpg",equal)
cv2.waitKey()