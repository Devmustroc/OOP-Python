import cv2

detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
imp_img =cv2.VideoCapture('107149350-1668034438907-musk2.jpg')

res, img = imp_img.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = detect.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Elon Image', img)
cv2.waitKey(0)
imp_img.release()
cv2.destroyAllWindows()


