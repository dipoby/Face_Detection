import cv2
import os

directory = r"D:\\MyDocs\\Py\\Basics\\FaceDetect\\"

face_cascade=cv2.CascadeClassifier(directory+"haarcascade_frontalface_default.xml")

img = cv2.imread(directory+"news.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)



for x, y, w ,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),3)

print(type(faces))
print(faces)    

resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

#img = cv2.imread(r"D:\MyDocs\Py\Basics\OpenCV\galaxy.jpg",0)
cv2.imshow("Grey",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
print(type(img))

print(img)

print(img.shape)

print(img.ndim)

resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("Galaxy", resized_image)
cv2.imwrite(r"D:\MyDocs\Py\Basics\OpenCV\Galaxy_resized.jpg",resized_image)

print(resized_image.shape)
cv2.waitKey(0) # 0 button click other number  time in ms
cv2.destroyAllWindows()
"""