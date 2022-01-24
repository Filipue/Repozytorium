import os as o
import cv2 as cv
import imutils as im


hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())


def read_data():
    data_format = [".jpg"]
    track = 'Photos/'
    for (track, dirs, data) in o.walk(track):
        for photo in data:
            if photo.endswith(tuple(data_format)):
                print(photo)
                photo = track + photo
                detection(photo)


def detection(photo: str):
    photo = cv.imread(photo)
    photo = im.resize(photo, width=min(900, photo.shape[1]))
    (regions, _) = hog.detectMultiScale(photo, winStride=(4, 4), padding=(8, 8), scale=1.05)

    register = 1
    for (x, y, w, h) in regions:
        cv.rectangle(photo, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv.putText(photo, f'person {register}', (x, y), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0, 0, 255), 2)
        register += 1

    print(f'On the image are {register-1} human`s')
    cv.imshow("Photo", photo)
    cv.waitKey(0)
    cv.destroyAllWindows()


read_data()
