import cv2

img_color=cv2.imread(r"C:\Users\Ariya Rayaneh\Desktop\football.jpg")
img_color1=cv2.imread(r"C:\Users\Ariya Rayaneh\Desktop\obama.jpg")


def facesticker(filename):
    img= cv2.imread(rf"C:\Users\Ariya Rayaneh\Desktop\{filename}")
    img = cv2.resize(img, (0, 0), fx=4, fy=4)
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sticker = cv2.imread(r"C:\Users\Ariya Rayaneh\Desktop\emoji.png")
    face_detector = cv2.CascadeClassifier(r"C:\Users\Ariya Rayaneh\Desktop\haarcascade_frontalface_alt.xml")
    faces=face_detector.detectMultiScale(img_grey,1.5)

    for i in range(len(faces)):
        x, y, w, h = faces[i]
        sticker_resized = cv2.resize(sticker, (w, h))
        b =cv2.subtract(img[y:y + h, x:x + w],sticker_resized)
        sticker_resized =sticker_resized+b
        img[y:y + h, x:x + w] = sticker_resized
    cv2.imwrite(r"C:\Users\Ariya Rayaneh\Desktop\picture8.jpg", img)
    cv2.imshow('output', img)
    cv2.waitKey()


def eyes_mouth_sticker(filename):
    img= cv2.imread(rf"C:\Users\Ariya Rayaneh\Desktop\{filename}")
    img = cv2.resize(img, (0, 0), fx=4, fy=4)
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    sticker = cv2.imread(r"C:\Users\Ariya Rayaneh\Desktop\emoji.png")
    eye_detector = cv2.CascadeClassifier(r"C:\Users\Ariya Rayaneh\Desktop\haarcascade_eye.xml")
    mouth_detector = cv2.CascadeClassifier(r"C:\Users\Ariya Rayaneh\Desktop\haarcascade_mcs_mouth.xml")

    eyes=eye_detector.detectMultiScale(img_grey,1.5)
    for i in range(len(eyes)):
        x, y, w, h = eyes[i]
        sticker_resized = cv2.resize(sticker, (w, h))
        b =cv2.subtract(img[y:y + h, x:x + w],sticker_resized)
        sticker_resized =sticker_resized+b
        img[y:y + h, x:x + w] = sticker_resized

    mouths=mouth_detector.detectMultiScale(img_grey,1.5)
    for i in range(len(mouths)):
        x, y, w, h = mouths[i]
        sticker_resized = cv2.resize(sticker, (w, h))
        b =cv2.subtract(img[y:y + h, x:x + w],sticker_resized)
        sticker_resized =sticker_resized+b
        img[y:y + h, x:x + w] = sticker_resized
    cv2.imwrite(r"C:\Users\Ariya Rayaneh\Desktop\picture10.jpg", img)
    cv2.imshow('output', img)
    cv2.waitKey()


def blur(filename):
    img= cv2.imread(rf"C:\Users\Ariya Rayaneh\Desktop\{filename}")
    img = cv2.resize(img, (0, 0), fx=4, fy=4)
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_detector = cv2.CascadeClassifier(r"C:\Users\Ariya Rayaneh\Desktop\haarcascade_frontalface_alt.xml")
    faces=face_detector.detectMultiScale(img_grey,1.5)

    for i in range(len(faces)):
        x, y, w, h = faces[i]

        img= cv2.blur(img[y:y + h, x:x + w],(100,100))

        cv2.imwrite(r"C:\Users\Ariya Rayaneh\Desktop\picture12.jpg", img)
        cv2.imshow('output', img)
        cv2.waitKey()



def checker(filename):
    img= cv2.imread(rf"C:\Users\Ariya Rayaneh\Desktop\{filename}")
    img = cv2.resize(img, (0, 0), fx=4, fy=4)
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_detector = cv2.CascadeClassifier(r"C:\Users\Ariya Rayaneh\Desktop\haarcascade_frontalface_alt.xml")
    faces=face_detector.detectMultiScale(img_grey,1.5)

    for i in range(len(faces)):
        x, y, w, h = faces[i]
        k=[]

        sticker_resized1 = cv2.blur(img[y:y + h//3, x:x + w//3],(100,100))
        sticker_resized2 = cv2.blur(img[y + h//3:y + h//3+h//3, x :x + w//3],(100,100))
        sticker_resized3 = cv2.blur(img[y + h // 3+h//3:y + h // 3 + h // 3+h//3, x:x + w // 3], (100, 100))
        sticker_resized4 = cv2.blur(img[y:y + h//3, x + w//3:x + w//3+w//3],(100,100))
        sticker_resized5 = cv2.blur(img[y + h//3:y + h//3+h//3, x + w//3:x + w//3+w//3],(100,100))
        sticker_resized6 = cv2.blur(img[y + h // 3+h//3:y + h // 3 + h // 3+h//3, x + w//3:x + w//3+w//3], (100, 100))
        sticker_resized7 = cv2.blur(img[y :y + h // 3 , x + w // 3+w//3:x + w // 3 + w // 3+w//3], (100, 100))
        sticker_resized8 = cv2.blur(img[y:y + h // 3+h//3, x + w // 3 + w // 3:x + w // 3 + w // 3 + w // 3], (100, 100))
        sticker_resized9 = cv2.blur(img[y:y + h // 3+h//3+h//3, x + w // 3 + w // 3:x + w // 3 + w // 3 + w // 3], (100, 100))


        img[y:y + h//3, x:x + w//3] = sticker_resized1
        img[y + h//3:y + h//3+h//3, x :x + w//3] = sticker_resized2
        img[y + h // 3+h//3:y + h // 3 + h // 3+h//3, x:x + w // 3] = sticker_resized3
        img[y:y + h//3, x + w//3:x + w//3+w//3]=sticker_resized4
        img[y + h // 3:y + h // 3 + h // 3, x + w // 3:x + w // 3 + w // 3]=sticker_resized5
        img[y + h // 3 + h // 3:y + h // 3 + h // 3 + h // 3, x + w // 3:x + w // 3 + w // 3]=sticker_resized6
        img[y:y + h // 3, x + w // 3 + w // 3:x + w // 3 + w // 3 + w // 3]=sticker_resized7
        img[y:y + h // 3 + h // 3, x + w // 3 + w // 3:x + w // 3 + w // 3 + w // 3]=sticker_resized8
        img[y:y + h // 3 + h // 3 + h // 3, x + w // 3 + w // 3:x + w // 3 + w // 3 + w // 3]=sticker_resized9

        cv2.imwrite(r"C:\Users\Ariya Rayaneh\Desktop\picture12.jpg", img)
        cv2.imshow('output', img)
        cv2.waitKey()

def flip(filename):
        img = cv2.imread(rf"C:\Users\Ariya Rayaneh\Desktop\{filename}")
        img = cv2.resize(img, (0, 0), fx=4, fy=4)
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img=cv2.flip(img,-90)
        cv2.imwrite(r"C:\Users\Ariya Rayaneh\Desktop\picture14.jpg", img)
        cv2.imshow('output', img)
        cv2.waitKey()





a=int(input('Input your choice: '))
b=input('Input file name & extension(e.g. football.jpg): ')
if a==1:
 facesticker(b)

elif a==2:
 eyes_mouth_sticker(b)

elif a==3:
 checker(b)

elif a==4:
 flip(b)

elif a==5:
 blur(b)








