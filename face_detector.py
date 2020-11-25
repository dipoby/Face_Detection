import cv2
import glob
import os 


directory_out = r"D:\\MyDocs\\Py\\Basics\\FaceDetect\\"

print(os.getcwd())
os.chdir(directory_out)
print(os.getcwd())
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("photo.jpg")

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
