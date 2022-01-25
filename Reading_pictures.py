from Person_detection import detect
import os as o

def read_picture():
    data_format = [".jpg"]
    track = 'Photos/'
    for (track, dirs, data) in o.walk(track):
        for photo in data:
            if photo.endswith(tuple(data_format)):
                print(photo)
                photo = track + photo
                detect(photo)
