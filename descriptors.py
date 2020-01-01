import face_recognition
import numpy as np
import os

def getfacedescriptor(x):
    img = face_recognition.load_image_file('photos/'+x)
    face_encoding = face_recognition.face_encodings(img)[0]
    fname=x.replace('.jpg','')
    np.save('faces/'+fname, face_encoding)

def getfaces(x='photos'):
    files = os.listdir('photos')
    for x in files: 
        if x.find(".jpg") > 0:
            fname=x.replace('.jpg','')
            if (not(os.path.exists('faces/'+fname+'.npy'))): 
                getfacedescriptor(x)
                print(fname + " saved")
    print("Descriptors found in all photos")