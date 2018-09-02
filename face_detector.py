try:
    import cv2
    import numpy as np

except:
    print('error')

                                    #insert here the path to the xml file for the Cascade classifier
faceCascade = cv2.CascadeClassifier(r'C:\Users\Hp\Downloads\opencv\sources\data\haarcascades_cuda\haarcascade_frontalface_default.xml')

                    #insert here the name of the image you want to analyze
image  = cv2.imread('immagine4.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,                         
    minNeighbors=5,
    minSize=(30, 30)

)
print ("Found {0} faces!".format(len(faces)))

'''draw a rectangle around the faces in the image'''
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Faces found", image)
cv2.waitKey(0)
