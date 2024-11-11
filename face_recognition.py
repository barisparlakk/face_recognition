import cv2
faceCascade = cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml")
cam=cv2.VideoCapture(0)
while True:

    _, sqrc = cam.read()
    # sqrc = cv2.flip(sqrc, -1) # if the camera is flipped
    gray = cv2.cvtColor(sqrc, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,
                                         scaleFactor = 1.1,
                                         minNeighbors = 5,
                                         minSize = (20,20)
                                         )
    for (x, y, w, h) in faces:
        cv2.rectangle(sqrc, (x, y),(x+w, y+h), (255, 0, 0), 2)
    cv2.imshow("sqrc", sqrc)
    k = cv2.waitKey(1) & 0xff
    if k == 27 or k==ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
