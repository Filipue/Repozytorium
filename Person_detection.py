import cv2 as cv
import imutils as im

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

def detect(photo: str):
    photo = cv.imread(photo)
    photo = im.resize(photo, width=min(900, photo.shape[1]))
    (regions, _) = hog.detectMultiScale(photo, winStride=(4, 4), padding=(8, 8), scale=1.05)

    register = 1
    for (x, y, w, h) in regions:
        cv.rectangle(photo, (x, y), (x + w, y + h), (0, 0, 255), 2)
        register += 1

    print(f'On the image are {register-1} human`s')
    cv.imshow("Photo", photo)
    cv.waitKey(0)
    cv.destroyAllWindows()
